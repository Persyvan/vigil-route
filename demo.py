#!/usr/bin/env python3
"""
VIGIL-ROUTE - Standalone Inference Demo Script
Developed by Persy Maki ND

Description:
    Standalone script for testing the VIGIL-ROUTE road defect detection model.
    Supports single image or batch processing with risk assessment.

Usage:
    python demo.py --image path/to/image.jpg
    python demo.py --image path/to/folder/ --speed 60
    python demo.py --image test.jpg --output results/
"""

import argparse
import os
import sys
import cv2
import numpy as np
import tensorflow as tf
from datetime import datetime
from pathlib import Path


# CONFIGURATION


# Model Classes (order matters!)
CLASS_NAMES = ['deformation_chaussee', 'nid_de_poule', 'route_saine']

# Class translations for display
CLASS_TRANSLATIONS = {
    'deformation_chaussee': 'Pavement Deformation',
    'nid_de_poule': 'Pothole',
    'route_saine': 'Healthy Road'
}

# Risk level colors (for terminal output)
COLORS = {
    'CRITICAL': '\033[91m',  # Red
    'HIGH': '\033[93m',      # Yellow
    'MEDIUM': '\033[94m',    # Blue
    'LOW': '\033[92m',       # Green
    'NONE': '\033[92m',      # Green
    'RESET': '\033[0m'
}



# CORE FUNCTIONS (adapted from vigil_brain.py)


def predict_defect(image, model, threshold=0.40):
    """
    Predict road defect from image.
    
    Args:
        image: OpenCV image (BGR format)
        model: Loaded Keras model
        threshold: Minimum confidence threshold
        
    Returns:
        tuple: (defect_class, confidence, all_detections)
    """
    # Resize to model input size
    img_resized = cv2.resize(image, (224, 224))
    img_array = tf.keras.utils.img_to_array(img_resized)
    img_batch = np.expand_dims(img_array, 0)
    
    # Predict
    predictions = model.predict(img_batch, verbose=0)
    scores = tf.nn.softmax(predictions[0])
    
    # Find all detections above threshold
    detections = []
    for idx, score in enumerate(scores):
        class_name = CLASS_NAMES[idx]
        confidence = float(score)
        
        # Skip healthy road unless it's the top prediction
        if class_name == 'route_saine' and confidence < 0.80:
            continue
            
        if confidence >= threshold:
            detections.append((class_name, confidence))
    
    # Sort by confidence
    detections.sort(key=lambda x: x[1], reverse=True)
    
    # If no defects found, return healthy road
    if not detections:
        detections = [('route_saine', float(scores[2]))]
    
    primary_class, primary_conf = detections[0]
    
    return primary_class, primary_conf, detections


def calculate_adaptive_threshold(defect_class, speed):
    """
    Calculate confidence threshold based on speed zone.
    
    Args:
        defect_class: Detected defect type
        speed: Vehicle speed (km/h)
        
    Returns:
        float: Required confidence threshold
    """
    if defect_class == 'route_saine':
        return 0.80
    
    thresholds = {
        'nid_de_poule': {
            'high': 0.45,    # ≥70 km/h
            'medium': 0.50,  # 50-69 km/h
            'low': 0.60      # <50 km/h
        },
        'deformation_chaussee': {
            'high': 0.60,
            'medium': 0.65,
            'low': 0.70
        }
    }
    
    defect_thresholds = thresholds.get(defect_class, thresholds['deformation_chaussee'])
    
    if speed >= 70:
        return defect_thresholds['high']
    elif speed >= 50:
        return defect_thresholds['medium']
    else:
        return defect_thresholds['low']


def analyze_risk(defect_class, confidence, speed):
    """
    Calculate risk level based on defect type, confidence, and speed.
    
    Args:
        defect_class: Detected defect type
        confidence: AI confidence score (0-1)
        speed: Vehicle speed (km/h)
        
    Returns:
        tuple: (risk_level, recommended_action)
    """
    if defect_class == 'route_saine':
        return "NONE", "No action required"
    
    # Base severity score
    base_score = 1.0 if defect_class == 'nid_de_poule' else 0.7
    
    # Speed multiplier (danger increases exponentially with speed)
    speed_factor = 1.0 + (speed / 50.0) ** 1.2
    
    # Final danger score
    danger_score = (confidence * base_score) * speed_factor
    
    # Risk classification
    if danger_score >= 1.5:
        return "CRITICAL", "Immediate repair required"
    elif danger_score >= 1.0:
        return "HIGH", "Inspection required within 1 week"
    elif danger_score >= 0.7:
        return "MEDIUM", "Monitoring recommended"
    else:
        return "LOW", "Preventive maintenance"


def draw_detection_box(image, defect_class, confidence, risk_level):
    """
    Draw detection box and label on image.
    
    Args:
        image: OpenCV image
        defect_class: Detected class
        confidence: Confidence score
        risk_level: Risk assessment
        
    Returns:
        Annotated image
    """
    h, w = image.shape[:2]
    output = image.copy()
    
    # Color based on risk
    colors = {
        'CRITICAL': (0, 0, 255),    # Red
        'HIGH': (0, 165, 255),      # Orange
        'MEDIUM': (0, 255, 255),    # Yellow
        'LOW': (0, 255, 0),         # Green
        'NONE': (0, 255, 0)
    }
    color = colors.get(risk_level, (255, 255, 255))
    
    # Draw bounding box (central region)
    margin_x = int(w * 0.2)
    margin_y = int(h * 0.15)
    pt1 = (margin_x, margin_y)
    pt2 = (w - margin_x, h - margin_y)
    
    if defect_class != 'route_saine':
        cv2.rectangle(output, pt1, pt2, color, 3)
    
    # Label
    label = f"{CLASS_TRANSLATIONS[defect_class]} - {confidence:.1%}"
    label_size = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)[0]
    
    # Label background
    cv2.rectangle(output, 
                  (pt1[0], pt1[1] - label_size[1] - 20),
                  (pt1[0] + label_size[0] + 10, pt1[1]),
                  color, -1)
    
    # Label text
    cv2.putText(output, label, 
                (pt1[0] + 5, pt1[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    
    # Risk level badge
    risk_text = f"RISK: {risk_level}"
    cv2.putText(output, risk_text,
                (20, h - 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
    
    return output

# MAIN INFERENCE FUNCTION


def run_inference(model_path, image_path, output_dir, speed, save_output):
    """
    Run inference on image(s).
    
    Args:
        model_path: Path to Keras model
        image_path: Path to image or directory
        output_dir: Output directory for annotated images
        speed: Simulated vehicle speed
        save_output: Whether to save annotated images
    """
    # Load model
    print("\n" + "="*80)
    print("🤖 VIGIL-ROUTE - Road Defect Detection System")
    print("="*80)
    print(f"\n📦 Loading model from: {model_path}")
    
    try:
        model = tf.keras.models.load_model(model_path)
        print("✅ Model loaded successfully (MobileNetV2 - 87.9% accuracy)\n")
    except Exception as e:
        print(f"❌ Error loading model: {e}")
        sys.exit(1)
    
    # Check if path is file or directory
    path = Path(image_path)
    
    if path.is_file():
        images = [path]
    elif path.is_dir():
        # Get all image files
        extensions = ['*.jpg', '*.jpeg', '*.png', '*.JPG', '*.JPEG', '*.PNG']
        images = []
        for ext in extensions:
            images.extend(path.glob(ext))
    else:
        print(f"❌ Invalid path: {image_path}")
        sys.exit(1)
    
    if not images:
        print(f"⚠️  No images found in: {image_path}")
        sys.exit(1)
    
    print(f"📸 Processing {len(images)} image(s) at {speed} km/h speed zone\n")
    print("="*80)
    
    # Create output directory if saving
    if save_output:
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)
    
    # Process each image
    results = []
    
    for idx, img_path in enumerate(images, 1):
        print(f"\n📷 Image {idx}/{len(images)}: {img_path.name}")
        
        # Load image
        image = cv2.imread(str(img_path))
        if image is None:
            print(f"   ❌ Failed to load image")
            continue
        
        # Run prediction
        defect_class, confidence, all_detections = predict_defect(image, model)
        
        # Calculate adaptive threshold
        threshold = calculate_adaptive_threshold(defect_class, speed)
        
        # Analyze risk
        risk_level, action = analyze_risk(defect_class, confidence, speed)
        
        # Display results
        color = COLORS.get(risk_level, COLORS['RESET'])
        print(f"   🔍 Detected: {CLASS_TRANSLATIONS[defect_class]}")
        print(f"   📊 Confidence: {confidence:.1%} (threshold: {threshold:.1%})")
        print(f"   {color}⚠️  Risk Level: {risk_level}{COLORS['RESET']}")
        print(f"   📋 Action: {action}")
        
        # Show all detections if multiple
        if len(all_detections) > 1:
            print(f"   ℹ️  All detections:")
            for cls, conf in all_detections:
                print(f"      • {CLASS_TRANSLATIONS[cls]}: {conf:.1%}")
        
        # Validation
        if confidence >= threshold:
            print(f"   ✅ VALIDATED (above threshold)")
            validated = True
        else:
            print(f"   ⚠️  Below confidence threshold")
            validated = False
        
        # Save annotated image
        if save_output and validated:
            annotated = draw_detection_box(image, defect_class, confidence, risk_level)
            output_filename = f"annotated_{img_path.stem}_{risk_level}.jpg"
            output_file = output_path / output_filename
            cv2.imwrite(str(output_file), annotated)
            print(f"   💾 Saved: {output_filename}")
        
        # Store results
        results.append({
            'image': img_path.name,
            'defect': CLASS_TRANSLATIONS[defect_class],
            'confidence': confidence,
            'risk': risk_level,
            'action': action,
            'validated': validated
        })
    
    # Summary
    print("\n" + "="*80)
    print("📊 DETECTION SUMMARY")
    print("="*80)
    
    validated_count = sum(1 for r in results if r['validated'])
    critical_count = sum(1 for r in results if r['risk'] == 'CRITICAL')
    high_count = sum(1 for r in results if r['risk'] == 'HIGH')
    
    print(f"\nTotal images processed: {len(results)}")
    print(f"Validated detections:   {validated_count}")
    print(f"Critical defects:       {critical_count}")
    print(f"High priority defects:  {high_count}")
    
    if save_output:
        print(f"\n💾 Annotated images saved to: {output_dir}")
    
    print("\n" + "="*80 + "\n")



# COMMAND LINE INTERFACE


def main():
    parser = argparse.ArgumentParser(
        description='VIGIL-ROUTE - Road Defect Detection Demo',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Single image analysis
  python demo.py --image test.jpg
  
  # Batch processing with custom speed
  python demo.py --image images/ --speed 70
  
  # Save annotated outputs
  python demo.py --image test.jpg --output results/ --save
  
  # Specify custom model path
  python demo.py --image test.jpg --model models/custom_model.keras
        '''
    )
    
    parser.add_argument(
        '--image',
        type=str,
        required=True,
        help='Path to input image or directory of images'
    )
    
    parser.add_argument(
        '--model',
        type=str,
        default='models/vigil_route_classifier_v9_open_world.keras',
        help='Path to trained model (default: models/vigil_route_classifier_v9_open_world.keras)'
    )
    
    parser.add_argument(
        '--output',
        type=str,
        default='output',
        help='Output directory for annotated images (default: output)'
    )
    
    parser.add_argument(
        '--speed',
        type=int,
        default=50,
        help='Simulated vehicle speed in km/h (default: 50)'
    )
    
    parser.add_argument(
        '--save',
        action='store_true',
        help='Save annotated images to output directory'
    )
    
    args = parser.parse_args()
    
    # Run inference
    run_inference(
        model_path=args.model,
        image_path=args.image,
        output_dir=args.output,
        speed=args.speed,
        save_output=args.save
    )


if __name__ == '__main__':
    main()
