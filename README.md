# 🚗 VIGIL-ROUTE: AI-Powered Road Defect Detection System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9-green.svg)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8-purple.svg)](https://github.com/ultralytics/ultralytics)
[![Accuracy](https://img.shields.io/badge/Accuracy-87.9%25-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-grey.svg)](LICENSE)
![Hugging Face](https://img.shields.io/badge/%20Hugging%20Face-Public%20Demo-yellow)

**Deep learning system for automated road defect detection with MobileNetV2.**  
*A privacy-focused Edge-AI solution for smart cities.*

Developed by **Persy Maki Ndombe** | AI/ML Engineering Student

---

🌐 **Language:** [🇬🇧 English](#) | [🇫🇷 Français](README.fr.md)

---

## 📌 Project Overview

VIGIL-ROUTE is a production-ready computer vision system that identifies road defects (potholes, pavement deformations) from images and videos with **87.9% accuracy**.

Designed to bridge the gap between reactive repairs (citizen complaints) and proactive maintenance, it introduces a novel **Danger Score Algorithm** that prioritizes repairs based on vehicle speed and defect severity.

### 🎯 Key Features

- **🧠 MobileNetV2 Architecture**: Lightweight CNN optimized for mobile/edge deployment
- **📸 Dual-Mode Operation**: 
  - **Citizen Mode**: Photo processing via 311 apps with EXIF GPS extraction
  - **Fleet Mode**: Real-time dashcam video analysis with HUD overlay
- **📊 Automated Reporting**: Color-coded urgency Excel reports + Interactive HTML maps
- **🌍 GPS Integration**: 
  - **Citizen**: EXIF metadata extraction (smartphone photos)
  - **Fleet**: OBD-II hardware integration (vehicle telemetry)
- **🚨 Adaptive Risk Score**: Speed-based prioritization algorithm
- **💧 Water Resistance**: Trained to detect water-filled potholes (rainy/winter conditions)
- **🗺️ Geospatial Visualization**: Interactive Folium maps with priority markers
- **🛡️ Privacy Architecture**: YOLOv8 detection layer (pedestrian blurring operational)

---

## 🧠 Engineering Choice: Why MobileNetV2?

We deliberately chose **Image Classification (MobileNetV2)** over Object Detection (YOLO) for the model's core. This is a strategic choice for **Ecology and Efficiency**:

1. **Ecological Impact**: MobileNetV2 consumes significantly less energy. This is crucial for battery-powered embedded devices running all day.
2. **Hardware Resources**: It runs perfectly on standard CPUs (Raspberry Pi, smartphones) without requiring expensive, energy-hungry graphics cards (GPUs).
3. **"Zone Alert" Logic**: Cities repair road *segments* (e.g., 100m), not pixels. Classification answers the question *"Is this segment damaged?"* in 12ms, while pixel-by-pixel detection is much heavier.

---

## 📊 Dataset & Performance (Model V10)

**Model Name:** `vigil_route_semifullseasonv10.keras`  
**Meaning:** Semi-Full Coverage (Spring, Summer, Fall, Early Winter).

**Dataset Methodology:**
- **Total Images:** 1,584 (Montreal, Oct-Dec 2025)
- **Conditions:** Dry, Wet (Nov Rain), Fall leaves, Light snow (<5cm), Road salt, Urban lighting (6 PM)
- **Split:** 80% Training / 10% Validation / 10% Test

**Distribution and Accuracy:**
- **Deformation:** ~650 images (41%)
- **Pothole:** ~580 images (37%)
- **Healthy Road:** ~354 images (22%)

**Note on accuracy (87.9%):**
This figure reflects the real data imbalance (there are fewer "perfect" potholes and more complex deformations). However, the model is tuned for safety: **Healthy Road detection is at 100%**, ensuring no false alerts waste municipal resources.

**Robustness by Condition:**
| Condition | Accuracy | Status |
| :--- | :--- | :--- |
| ☀️ **Dry Roads** | **92%** | ✅ Production Ready |
| 🌧️ **Rain/Wet** | **88%** | ✅ Validated |
| ❄️ **Light Snow (<5cm)** | **84%** | ✅ Validated |
| 🌆 **Evening (Lighting)** | **100%** | ✅ Validated (6:00 PM) |
| 🌨️ *Heavy Snow (>10cm)* | *N/A* | ⚠️ Planned for V11 |

---

## 🚀 Quick Start (Live Demo)

**Test the V10 Model Instantly** without installing code.  
We've deployed a public "Showcase" on Hugging Face connected to our secure brain.

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Launch%20Demo-yellow)](https://huggingface.co/spaces/PvanAI/vigilroute-brain)

**Perfect for:**
- Testing the model with your own road images
- Verifying accuracy (Pothole vs Deformation)

---

## 🎬 Evidence and Visuals

### Fleet Mode (Real-Time Video Analysis)
*Dashcam processing with HUD overlay and privacy protection*

![Fleet HUD Preview](demo_outputs/fleet_examples/fleet_frame_01.png)
![Fleet HUD Preview](demo_outputs/fleet_examples/fleet_frame_02.png)

📹 **Full demo video (2 min):** [View on LinkedIn](#) *(coming soon)*  
🎥 **Alternative:** [View on YouTube](https://youtube.com/...) *(unlisted - available on request)*

**Key Outputs:**
- Real-time defect detection with bounding boxes
- Danger score algorithm in action
- GPS trajectory mapping
- Frame-by-frame Excel analysis

### Citizen Mode (311 App Simulation)
*Smartphone photo processing with automatic geolocation*

**Detection Result Examples:**

| Input Image | AI Classification | Confidence | Risk Level | Action Required |
|-------------|------------------|-----------|------------|----------------|
| ![Photo 1](demo_outputs/citizen_examples/screenshot_01_pothole.png) | **POTHOLE** | 98.5% | 🔴 **CRITICAL** | Immediate Repair |
| ![Photo 2](demo_outputs/citizen_examples/screenshot_02_deformation.png)| **DEFORMATION** | 98% | 🟠 **HIGH** | Inspection Required |
| ![Photo 3](demo_outputs/citizen_examples/screenshot_03_healthy.png) | **HEALTHY ROAD** | 100% | 🟢 **NONE** | No Action |

### 🗺️ Visualizations (Generated Reports)
*Instead of raw files, here are captures of generated results:*

**Interactive Map (Clustering & Priority):**
![Map Capture](replace_with_your_map_screenshot.jpg)

**Automated Excel Report:**
![Excel Capture](replace_with_your_excel_screenshot.jpg)

---

## 🧠 The "Smart" Logic: Adaptive Risk Score

VIGIL-ROUTE doesn't just find holes; it assesses the **danger**. A deformation at 30 km/h is a nuisance; at 90 km/h, it's a safety risk.

### 1. Risk Calculation Formula

The system merges Computer Vision confidence with vehicle telemetry data:

**Defect Severity × Vehicle Speed = Intervention Priority**

### How Does It Work?

1. **AI identifies the defect**: A Pothole (severe) weighs more than a Deformation (moderate).
2. **System reads speed**: The faster the vehicle, the higher the danger score multiplier.
3. **Verdict is immediate**:

| Context | Result | Action Required |
|---------|--------|----------------|
| 🕳️ Pothole at 30 km/h | 🟡 MEDIUM | Monitoring |
| 🕳️ Same pothole at 50 km/h | 🟠 HIGH | Inspection |
| 🕳️ Same pothole at 90 km/h | 🔴 CRITICAL | Immediate Repair |

**Why is this revolutionary?** The same defect changes priority based on road context. Highways (high speed) are protected first, without wasting resources on residential roads at 30 km/h.

### 2. Adaptive Detection Thresholds

To reduce false positives at high speed (safety-first approach), the model dynamically adjusts its sensitivity:

| Speed Zone | Pothole Threshold | Deformation Threshold | Justification |
|:---|:---|:---|:---|
| High (≥70 km/h) | 45% confidence | 60% confidence | Highway speeds require conservative detection |
| Medium (50-69 km/h) | 50% confidence | 65% confidence | Urban arterial roads |
| Low (<50 km/h) | 60% confidence | 70% confidence | Residential zones allow stricter filtering |

**Why it matters:** A false positive on highway (70+ km/h) could cause dangerous braking. Lower thresholds = higher confidence required = fewer false alarms.

### 3. Customizable Configuration

Municipalities can adjust costs and parameters:
- **Unit Cost (Pothole):** 175 CAD (Default)
- **Surface Cost (Deformation):** 220 CAD/m²
- **Urgency Markup:** 1.8x (for P1 Critical)
- **Winter Markup:** +20% (Auto-detection Nov-Mar)

---

## 🚛 Pilot Program & Deployment

The system is ready for a **1-Month Pilot Deployment**.

**Pilot Scope:**
1. **Citizen Mode Priority:** Full integration with the city's existing 311 App API.
2. **Fleet Mode Test:** Equipping **1 Municipal Vehicle** (Garbage truck or patrol) for automated collection.

**Hardware Requirements (Fleet):**
- **GPS/Speed:** OBD-II reader
- **Vision:** Standard dashcam (1080p)
- **Compute:** Raspberry Pi 4 or Jetson Nano

⚠️ **Hardware Integration Requirements:**

While the software pipeline is fully functional, actual fleet deployment requires physical hardware integration:

| Component | Purpose | Status |
|:---|:---|:---|
| GPS OBD-II Reader | Real-time vehicle location + speed | ⚠️ Hardware integration pending |
| Dashcam | Video capture | ✅ Any MP4-compatible camera |
| Edge Device | Run AI inference | ✅ Raspberry Pi 4 / Jetson Nano tested |
| Data Sync | OBD-II ↔ Video timestamp alignment | ⚠️ Requires fleet management integration |

**Recommended Devices:**
- FreeMatrix OBD-II Bluetooth (~$60 USD)
- Verizon Hum OBD (~$10/month cellular)
- Automatic Pro (~$130 WiFi + 4G)

**Current Status:**
✅ Software pipeline ready  
⚠️ Hardware integration requires municipal fleet partnership

---

## 🛡️ Privacy & Ethics Module

Compliance with privacy laws (Quebec Bill 25 / GDPR) is a fundamental design principle.

**Architecture Overview:**
The system includes a YOLOv8 detection layer to identify personal data before storage:

| Feature | Technology | Status | Note |
|:---|:---|:---|:---|
| Pedestrian Protection | YOLOv8 (Class 0) | ✅ Operational | Human detection and full-body Gaussian blur functional |
| Vehicle Anonymization | YOLOv8 + Geometric Detection | ⚠️ Prototype | License plate detection implemented as Proof-of-Concept. Production deployment requires specialized OCR/Privacy solutions |

**What works:**
✅ YOLOv8 reliably detects humans  
✅ Gaussian blur applied to detected regions  
✅ Privacy-focused pipeline architecture

**What requires professional integration:**
⚠️ Certified license plate detection (OCR + blur)  
⚠️ Legal compliance audit (municipal legal teams)  
⚠️ GDPR/Bill 25 documentation for municipal procurement

---

## 🏗️ Technical Specifications

### Model Architecture (V10)

| Component | Details |
|:---|:---|
| Framework | TensorFlow 2.19.0 / Keras |
| Base Model | MobileNetV2 (ImageNet pre-trained, frozen) |
| Input Shape | 224×224×3 RGB |
| Classes | pothole, pavement_deformation, healthy_road |
| Dataset | 1,584 annotated images (Montreal, Oct-Dec 2025) |
| Test Accuracy | 87.90% |
| Test Loss | 0.3664 |
| Inference Time | ~12ms (T4 GPU) / ~120ms (Colab Pro CPU) |

### 🗂️ Dataset Methodology

**Collection Details:**
- **Period:** October - December 2025
- **Location:** Montreal, QC, Canada (various neighborhoods)
- **Conditions:** Winter transition (sun, rain, wet asphalt, light snow, road salt)
- **Device:** iPhone (simulating citizen 311 app usage)

**Why Winter Data Matters:**
Montreal's harsh climate creates unique challenges:
- 💧 Water-filled potholes (November rains)
- 🍂 Fall leaf coverage (October)
- ❄️ Early winter conditions (December salt/snow)

This seasonal diversity ensures the model works year-round, not just in ideal sunny conditions.

**Class Distribution (1,584 Images):**
pavement_deformation: ~650 images (41%)
pothole: ~580 images (37%)
healthy_road: ~354 images (22%)

text

**Performance by Class (Test Set):**

| Class | Precision | Recall | F1-Score |
|:---|:---|:---|:---|
| pavement_deformation | 85% | 91% | 88% |
| pothole | 83% | 74% | 79% |
| healthy_road | 100% | 100% | 100% |

**Key Finding:** Perfect healthy road detection = No false alerts wasting municipal resources.

---

## 📥 Resource Access (Model, Code, Datasets)

The **trained MobileNetV2 model** (`vigil_route_semifullseasonv10.keras` - 89 MB), complete training code, and original datasets are currently available **on request** for:

- 🎓 Academic research collaboration
- 🏙️ Smart city pilot projects
- 🔬 Technical evaluation by municipal engineering teams
- 💼 Recruitment assessment (recruiters/hiring managers)

### How to Request Access

📧 **Email:** [persy.maki.ml@gmail.com](mailto:persy.maki.ml@gmail.com)

**Please include in your request:**
1. Your name and affiliation (company/university)
2. Intended use case
3. Brief description of your project or evaluation goal

**⏱️ Response Time:** Access typically granted within 24-48h for legitimate requests.

### Future Public Release

The model will later be migrated to **🤗 Hugging Face Hub** for public access with appropriate licensing once the pilot validation phase is completed.

---

## 🔮 Roadmap

- **V11 (Full Season - 3-6 months):** Training on storms, black ice, and deep night (+500 images).
- **V12 (Segmentation - 6-12 months):** Transition to volumetric analysis (depth calculation) to estimate asphalt volume in liters via YOLOv8 Segmentation.
- **V13 (Deployment):** Full API integration and legal certifications.

---

## 🤝 Contact & Collaboration

This project is an Applied AI Research Prototype developed as part of my AI/ML engineering studies. I'm open to collaboration with:

- 🏙️ Smart city initiatives
- 🚗 Municipal fleet management departments
- 🔬 Research institutions (Computer Vision / Infrastructure)
- 💼 Engineering consulting firms

**Persy Maki Ndombe**  
AI/ML Engineering Student  
Specialized in Computer Vision & Smart Cities

📧 Email: [persy.maki.ml@gmail.com](mailto:persy.maki.ml@gmail.com)  
💼 LinkedIn: Persy Maki Ndombe  
🐙 GitHub: @Persyvan  
📍 Location: Montreal, QC, Canada

---

## 📄 License

MIT License - See LICENSE for details.

Copyright © 2026 Persy Maki Ndombe

---

## 🙏 Acknowledgments

A huge thank you to the members of **Civilians On Board AI** worldwide for their support and vision of human-centered AI.

⭐ **If this project interests you, please star the repository!**

---

🌐 **Read in other languages:** [🇬🇧 English](#) | [🇫🇷 Français](README.fr.md)

**Last Updated:** January 2026 | **Model Version:** V10
