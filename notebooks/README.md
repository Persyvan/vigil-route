# 📓 Notebooks

Jupyter notebooks for **VIGIL-ROUTE** development, training, inference, and evaluation.

---

## 📂 Structure

### 🎯 Main Notebook

**`Vigil_Route_Demo.ipynb`**
- Complete demonstration notebook
- Model loading and inference
- Image classification examples
- Visualization of predictions
- **Ready for Google Colab**

### 📁 Organized by Function

#### `02_inference/`
Demo notebooks for both deployment modes:
- **Citizen Mode:** Smartphone-based 311 app simulation
- **Fleet Mode:** Dashcam HUD overlay for fleet vehicles
- Real-time inference examples
- Batch processing demonstrations

---

## 🚀 Quick Start

### Option 1: Google Colab (Recommended)

1. Open `Vigil_Route_Demo.ipynb` in this repository
2. Click **"Open in Colab"** badge at the top
3. Follow the instructions to upload the model file
4. Run all cells to see the demo

### Option 2: Local Jupyter


# Clone the repository
git clone https://github.com/Persyvan/vigil-route.git
cd vigil-route/notebooks

# Install dependencies
pip install -r ../requirements.txt

# Launch Jupyter
jupyter notebook Vigil_Route_Demo.ipynb
📋 Prerequisites
Required:

Python 3.8+

TensorFlow 2.x

OpenCV

NumPy, Matplotlib

For inference:

Trained model file (vigil_route_classifier_v10_open_world.keras)

See models/README.md for access

🧪 What's Included
Demo Notebook Features:
✅ Model architecture visualization

✅ Single image inference

✅ Batch processing

✅ Confidence score visualization

✅ Class activation maps (CAM)

✅ Performance metrics display

Inference Examples:
Road defect detection (potholes, deformations)

Healthy road classification

Multi-image batch processing

GPS-tagged results for mapping

📊 Expected Outputs
When running the notebooks, you'll generate:

Annotated images with predictions

Confidence score charts

Detection statistics

Geographic visualizations (if GPS data provided)

🔧 Troubleshooting
Model File Not Found
Make sure the model file is placed in the models/ directory. See models/README.md for access instructions.

GPU Support
For faster inference, ensure TensorFlow can access your GPU:

python
import tensorflow as tf
print("GPU Available:", tf.config.list_physical_devices('GPU'))
Dependency Issues
bash
pip install --upgrade tensorflow opencv-python numpy matplotlib
📧 Contact
For notebook issues, model access, or collaboration:

📧 Email: persy.maki.ml@gmail.com

💼 LinkedIn: Persy Maki Ndombe

🐙 GitHub: @Persyvan

Last updated: February 2026 | Model Version: V10
