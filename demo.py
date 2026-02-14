#!/usr/bin/env python3
"""
VIGIL-ROUTE - Standalone Inference Demo Script
Developed by Persy Maki ND

⚠️ RECOMMENDED: Use our interactive Hugging Face Space instead!
🚀 Try it now: https://huggingface.co/spaces/pvanAI/vigilroute-brain

This script is for local testing only. For full features, use the online demo.

Usage:
    python demo.py --image path/to/image.jpg
    python demo.py --image path/to/folder/ --speed 60
"""

import argparse
import sys
import cv2
import numpy as np
import tensorflow as tf
from pathlib import Path

CLASS_NAMES = ['deformation_chaussee', 'nid_de_poule', 'route_saine']
CLASS_TRANSLATIONS = {
    'deformation_chaussee': 'Pavement Deformation',
    'nid_de_poule': 'Pothole',
    'route_saine': 'Healthy Road'
}

def main():
    print("\n" + "="*80)
    print("🤖 VIGIL-ROUTE - Road Defect Detection System v10")
    print("="*80)
    print("\n⚠️  For the best experience, use our interactive demo:")
    print("🚀 https://huggingface.co/spaces/pvanAI/vigilroute-brain")
    print("\nThis local script provides basic inference only.\n")
    print("="*80 + "\n")
    
    parser = argparse.ArgumentParser(description='VIGIL-ROUTE Local Demo (v10)')
    parser.add_argument('--image', type=str, required=True, help='Path to image')
    parser.add_argument('--model', type=str, 
                       default='models/vigil_route_classifier_v10_open_world.keras',
                       help='Path to model')
    args = parser.parse_args()
    
    # Load model
    print(f"📦 Loading model: {args.model}")
    try:
        model = tf.keras.models.load_model(args.model)
        print("✅ Model loaded (MobileNetV2 | 87.9% accuracy)\n")
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n💡 Model file not found? Request access:")
        print("📧 persy.maki.ml@gmail.com")
        sys.exit(1)
    
    # Load and process image
    image = cv2.imread(args.image)
    if image is None:
        print(f"❌ Cannot load image: {args.image}")
        sys.exit(1)
    
    img_resized = cv2.resize(image, (224, 224))
    img_array = tf.keras.utils.img_to_array(img_resized)
    img_batch = np.expand_dims(img_array, 0)
    
    # Predict
    predictions = model.predict(img_batch, verbose=0)
    scores = tf.nn.softmax(predictions[0])
    
    top_idx = np.argmax(scores)
    defect_class = CLASS_NAMES[top_idx]
    confidence = float(scores[top_idx])
    
    # Display result
    print(f"📷 Image: {Path(args.image).name}")
    print(f"🔍 Detected: {CLASS_TRANSLATIONS[defect_class]}")
    print(f"📊 Confidence: {confidence:.1%}")
    
    if defect_class != 'route_saine' and confidence > 0.6:
        print(f"⚠️  Defect detected!")
    else:
        print(f"✅ Road appears healthy")
    
    print("\n" + "="*80)
    print("🚀 For advanced features (risk analysis, GPS, reports):")
    print("   Visit: https://huggingface.co/spaces/pvanAI/vigilroute-brain")
    print("="*80 + "\n")

if __name__ == '__main__':
    main()
