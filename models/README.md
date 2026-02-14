# 🤖 VIGIL-ROUTE Model Weights

## Overview

This directory contains the trained AI model for road defect detection. The model file is not included in this repository due to GitHub's file size limitations (89 MB).

---

## 📊 Model Specifications

| Attribute | Details |
|-----------|---------|
| Architecture | MobileNetV2 (transfer learning) |
| Framework | TensorFlow 2.19 / Keras |
| Input Size | 224×224×3 RGB |
| Output Classes | 3 (deformation_chaussee, nid_de_poule, route_saine) |
| Accuracy | 87.9% on test set |
| File Size | 89 MB |
| Format | .keras (Keras native format) |
| Version | v10 (open world deployment) |

---

## 📥 How to Access the Model

The trained model (`vigil_route_classifier_v10_open_world.keras`) is available on request for:

- 🎓 Academic research collaboration
- 🏙️ Smart city pilot projects
- 🔬 Technical evaluation by municipal engineering teams
- 💼 Recruitment assessment (recruiters/hiring managers)

### Request Access

📧 **Email:** persy.maki.ml@gmail.com

**Please include:**
- Your name and affiliation (company/university)
- Intended use case
- Brief description of your project or evaluation goal

⏱️ **Response time:** Access typically granted within 24-48 hours for legitimate requests.

---

## 🔄 Alternative: Use Pre-trained MobileNetV2

If you want to test the codebase without the trained weights, you can use a standard pre-trained MobileNetV2:


from tensorflow.keras.applications import MobileNetV2

# Load base model (ImageNet weights)
base_model = MobileNetV2(
    input_shape=(224, 224, 3),
    include_top=False,
    weights='imagenet'
)

# Note: This won't detect road defects, but validates the architecture
📦 Expected File Structure
Once you obtain the model, place it here:

text
vigil-route/
└── models/
    ├── README.md (this file)
    └── vigil_route_classifier_v10_open_world.keras  ← Place model here
🚀 Using the Model
Option 1: Standalone Script
bash
python demo.py --image test.jpg --model models/vigil_route_classifier_v10_open_world.keras
Option 2: Google Colab
Upload the model file when prompted in the Colab notebook.

Option 3: Python Code
python
import tensorflow as tf

# Load model
model = tf.keras.models.load_model('models/vigil_route_classifier_v10_open_world.keras')

# Run inference
import cv2
import numpy as np

image = cv2.imread('road_image.jpg')
image_resized = cv2.resize(image, (224, 224))
image_array = tf.keras.utils.img_to_array(image_resized)
image_batch = np.expand_dims(image_array, 0)

predictions = model.predict(image_batch)
🧪 Model Training Details
The model was trained on:

Dataset: 1,584 road images from Montreal, QC

Period: October - December 2025

Conditions: Varied weather (rain, snow, dry)

Annotations: Manual labeling with quality control

Augmentation: Rotation, flip, brightness, contrast

Validation: 80/20 train-test split

Class Distribution
deformation_chaussee: ~650 images (41%)

nid_de_poule: ~580 images (37%)

route_saine: ~354 images (22%)

Performance by Class
Class	Precision	Recall	F1-Score
Pavement Deformation	85%	91%	88%
Pothole	83%	74%	79%
Healthy Road	100%	100%	100%
🔒 Model Security & Privacy
✅ No personal data embedded in model weights

✅ Trained only on infrastructure imagery (no faces/plates)

✅ Compliant with academic research ethics

✅ MIT License (see LICENSE)

🌐 Future Public Release
Once the project reaches significant adoption, the model will be migrated to 🤗 Hugging Face Hub for public access with appropriate licensing.

Planned repository: Persyvan/vigil-route-mobilenetv2

📞 Questions?
For model access, technical questions, or collaboration:

📧 Email: persy.maki.ml@gmail.com

💼 LinkedIn: Persy Maki Ndombe

🐙 GitHub: @Persyvan

Last updated: February 2026 | Model Version: V10
