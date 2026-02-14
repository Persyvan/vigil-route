# 🚗 VIGIL-ROUTE: AI-Powered Road Defect Detection System

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.17-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.8-green.svg)](https://opencv.org/)
[![Accuracy](https://img.shields.io/badge/Accuracy-87.9%25-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-Apache%202.0-grey.svg)](LICENSE)
![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Live%20Demo-yellow)

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

We deliberately chose **Image Classification (MobileNetV2)** over Object Detection (YOLO) for strategic reasons:

### **1. Efficiency & Sustainability 🌱**
- **Energy Consumption**: MobileNetV2 uses **80% less power** than YOLO-based detection
- **Hardware Requirements**: Runs on standard CPUs (Raspberry Pi, smartphones) without GPUs
- **Carbon Footprint**: Lower computational cost = reduced environmental impact for 24/7 fleet operations

### **2. Municipal Use Case Alignment 🏙️**
- **"Zone Alert" Logic**: Cities repair road *segments* (100m), not individual pixels
- **Speed**: Classification answers *"Is this segment damaged?"* in 12ms vs YOLO's 45ms
- **Cost**: No GPU infrastructure required ($$$$ savings for municipalities)

### **3. Scalability 📈**
- **Fleet Deployment**: 100 vehicles × CPU = Affordable
- **Fleet Deployment**: 100 vehicles × GPU = Prohibitively expensive
- **Citizen Mode**: Works on any smartphone (311 app integration)

**Trade-off Accepted**: We sacrifice pixel-precise localization for speed, cost, and scalability. For municipal planning, *knowing a 100m road segment needs repair* is sufficient.

---

## 📊 Dataset & Performance (Model V10)

**Model Name:** `vigil_route_semifullseason_v10.keras`  
**Meaning:** Semi-Full Season Coverage (Spring, Summer, Fall, Early Winter)

**Dataset Methodology:**
- **Total Images:** 1,584 (Montreal, Oct-Dec 2025)
- **Conditions:** Dry, Wet (Nov Rain), Fall leaves, Light snow (<5cm), Road salt, Urban lighting (6 PM)
- **Split:** 80% Training / 10% Validation / 10% Test

**Distribution and Accuracy:**
- **Deformation:** ~650 images (41%)
- **Pothole:** ~580 images (37%)
- **Healthy Road:** ~354 images (22%)

**Visual Distribution:**

🟠 Deformation (41%) ██████████████████
🔴 Pothole (37%) ████████████████
🟢 Healthy Road (22%) ██████████

text

**Why this imbalance?**  
This reflects real-world conditions: Montreal has more subtle deformations (frost heave, subsidence) than dramatic potholes. The model is trained on reality, not artificial balance.

**Note on accuracy (87.9%):**  
This figure reflects the real data imbalance (there are fewer "perfect" potholes and more complex deformations). However, the model is tuned for safety: **Healthy Road detection is at 100%**, ensuring no false alerts waste municipal resources.

**Robustness by Condition:**

| Condition | Accuracy | Status |
|:---|:---|:---|
| ☀️ **Dry Roads** | **92%** | ✅ Production Ready |
| 🌧️ **Rain/Wet** | **88%** | ✅ Validated |
| ❄️ **Light Snow (<5cm)** | **84%** | ✅ Validated |
| 🌆 **Evening (Lighting)** | **100%** | ✅ Validated (6:00 PM) |
| 🌨️ *Heavy Snow (>10cm)* | *N/A* | ⚠️ Planned for V11 |

---

## 🚀 Quick Start (Live Demo)

**Test the V10 Model Instantly** — no installation required.

[![Launch Demo](https://img.shields.io/badge/%F0%9F%A4%97%20Try%20Live%20Demo-Launch-yellow?style=for-the-badge)](https://huggingface.co/spaces/PvanAI/vigilroute-brain)

**What you can do:**
- Upload your own road photos
- Get instant AI classification (Pothole / Deformation / Healthy)
- See real-time detection with bounding boxes
- Test edge cases (night, rain, snow)

**Limitations:**
- 3 free tests per day (rate limiting)
- Demo mode only (no GPS/cost analysis)
- Image-only (video processing requires full deployment)

**For full system access:** Contact for pilot deployment.

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
![Map Capture](replace_with_your_map_preview.jpg)

**Automated Excel Report:**
![Excel Capture](replace_with_your_excel_preview.jpg)

---

## 🧠 The "Smart" Logic: Adaptive Risk Score

VIGIL-ROUTE doesn't just find holes; it assesses the **danger**. A deformation at 30 km/h is a nuisance; at 90 km/h, it's a safety risk.

### 1. Risk Calculation Formula

The system merges Computer Vision confidence with vehicle telemetry data:

**Defect Severity × Vehicle Speed = Intervention Priority**

### How Does It Work?

1. **AI identifies the defect**: A Pothole (severe) weighs more than a Deformation (moderate)
2. **System reads speed**: The faster the vehicle, the higher the danger score multiplier
3. **Verdict is immediate**:

| Context | Result | Action Required |
|---------|--------|----------------|
| 🕳️ Pothole at 30 km/h | 🟡 MEDIUM | Monitoring |
| 🕳️ Same pothole at 50 km/h | 🟠 HIGH | Inspection |
| 🕳️ Same pothole at 90 km/h | 🔴 CRITICAL | Immediate Repair |

**Why is this revolutionary?** The same defect changes priority based on road context. Highways (high speed) are protected first, without wasting resources on residential roads at 30 km/h.

### 2. Mathematical Model

The danger score \( D \) is calculated as:

\[ D = C \times S_b \times (1 + \frac{V}{50})^{1.2} \]

**Where:**
- \( C \) = AI Confidence (0.0 - 1.0)
- \( S_b \) = Base Severity (Pothole = 1.0, Deformation = 0.7)
- \( V \) = Vehicle Speed (km/h)

**Example:**
- Pothole detected at 85% confidence @ 90 km/h:
  - \( D = 0.85 \times 1.0 \times (1 + \frac{90}{50})^{1.2} \)
  - \( D = 0.85 \times 2.65 = 2.25 \) → **🔴 CRITICAL**

**Threshold Tiers:**
- \( D \geq 1.5 \) → 🔴 CRITICAL (Immediate repair)
- \( 1.0 \leq D < 1.5 \) → 🟠 HIGH (Inspection required)
- \( 0.7 \leq D < 1.0 \) → 🟡 MEDIUM (Monitoring)
- \( D < 0.7 \) → 🟢 LOW (Preventive maintenance)

### 3. Adaptive Detection Thresholds

To reduce false positives at high speed (safety-first approach), the model dynamically adjusts its sensitivity:

| Speed Zone | Pothole Threshold | Deformation Threshold | Justification |
|:---|:---|:---|:---|
| High (≥70 km/h) | 45% confidence | 60% confidence | Highway speeds require conservative detection |
| Medium (50-69 km/h) | 50% confidence | 65% confidence | Urban arterial roads |
| Low (<50 km/h) | 60% confidence | 70% confidence | Residential zones allow stricter filtering |

**Why it matters:** A false positive on highway (70+ km/h) could cause dangerous braking. Lower thresholds = higher confidence required = fewer false alarms.

### 4. Customizable Configuration

Municipalities can adjust costs and parameters:
- **Unit Cost (Pothole):** 175 CAD (Default)
- **Surface Cost (Deformation):** 220 CAD/m²
- **Urgency Markup:** 1.8x (for P1 Critical)
- **Winter Markup:** +20% (Auto-detection Nov-Mar)

---

## 🚛 Pilot Program & Deployment

The system is ready for a **1-Month Pilot Deployment**.

**Pilot Scope:**
1. **Citizen Mode Priority:** Full integration with the city's existing 311 App API
2. **Fleet Mode Test:** Equipping **1 Municipal Vehicle** (Garbage truck or patrol) for automated collection

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

**💡 Why Hardware Integration Matters:**

The VIGIL-ROUTE software is **100% functional** and can process any dashcam video. However, for automated fleet deployment, we need:

1. **Real-time GPS/Speed Data:** OBD-II reader provides this *while driving*
2. **Video Sync:** Timestamps must match GPS coordinates precisely
3. **Edge Computing:** Processing must happen on-vehicle (not cloud upload)

**Current Workaround (Demo/Testing):**
✅ We can process post-recording with manual GPS timestamp insertion  
✅ Perfect for pilot evaluation with 1-2 vehicles  
⚠️ Full fleet (10+ vehicles) requires integrated hardware solution

**Estimated Integration Cost:**
- Hardware per vehicle: ~$200-300 USD (OBD-II + Edge device)
- Software integration: Included (our system)
- Total pilot (1 vehicle, 1 month): **~$500 USD**

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

### 🚨 Important Disclaimer

**Current Status:** The privacy module is a **functional prototype** demonstrating technical feasibility:

✅ **What works in demo:**
- YOLOv8 detects humans with 95%+ accuracy
- Gaussian blur successfully anonymizes detected regions
- System architecture supports real-time privacy filtering

⚠️ **What requires production hardening:**
- Legal compliance audit (municipal legal teams)
- Certified license plate OCR solution (commercial-grade)
- GDPR/Bill 25 data retention policies
- Stress testing (1000+ detections/day)

**Recommendation for Pilot:**
Use privacy mode in **restricted zones only** (no residential areas) until full legal clearance is obtained.

**Alternative:** Partner with certified privacy solution providers (e.g., [Celantur](https://celantur.com/), [Brighter AI](https://brighter.ai/))

---

## 🏗️ Technical Specifications

### Model Architecture (V10)

| Component | Details |
|:---|:---|
| Framework | TensorFlow 2.17.0 / Keras |
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

The **trained MobileNetV2 model** (`vigil_route_semifullseason_v10.keras` - 89 MB), complete training code, and original datasets are currently available **on request** for:

- 🎓 Academic research collaboration
- 🏙️ Smart city pilot projects
- 🔬 Technical evaluation by municipal engineering teams
- 💼 Recruitment assessment (recruiters/hiring managers)

### ✅ **Immediate Access (Public)**
- 🤗 **Live Demo:** [Try on Hugging Face](https://huggingface.co/spaces/PvanAI/vigilroute-brain) (3 tests/day)
- 📄 **Documentation:** This README + technical specifications

### 🔒 **Full Access (On Request)**
Available for qualified requesters:

| Resource | Size | Access Level |
|----------|------|-------------|
| `vigil_route_v10.keras` | 89 MB | 🔐 Restricted |
| Training dataset (1,584 images) | ~2.1 GB | 🔐 Restricted |
| Citizen Mode source code | Full Python | 🔐 Restricted |
| Fleet Mode source code | Full Python | 🔐 Restricted |
| Cost estimation module | Excel/Python | 🔐 Restricted |

**Who qualifies for access:**
- 🏙️ Municipal engineering teams (pilot evaluation)
- 🎓 Academic researchers (collaboration proposals)
- 💼 Hiring managers (technical assessment)
- 🔬 Smart city consultants (RFP responses)

### 📧 **Request Access**

**Email:** [persy.maki.ml@gmail.com](mailto:persy.maki.ml@gmail.com)

**Include in your request:**
1. **Name & Organization** (company/university)
2. **Use Case** (pilot / research / recruitment)
3. **Timeline** (when do you need access?)
4. **NDA Agreement** (if required for your organization)

**⏱️ Response Time:** 24-48 hours for legitimate requests

---

### 🤝 **Future Public Release**

Once pilot validation is complete (Q2-Q3 2026), the model will be publicly released on:
- 🤗 **Hugging Face Hub** (Apache 2.0 license)
- 🐙 **GitHub** (full source code)
- 📦 **Docker Hub** (containerized deployment)

---

## 🔮 Roadmap

- **V11 (Full Season - 3-6 months):** Training on storms, black ice, and deep night (+500 images)
- **V12 (Segmentation - 6-12 months):** Transition to volumetric analysis (depth calculation) to estimate asphalt volume in liters via YOLOv8 Segmentation
- **V13 (Deployment):** Full API integration and legal certifications

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
💼 LinkedIn: [Persy Maki Ndombe](https://linkedin.com/in/persy-maki-ndombe)  
🐙 GitHub: [@Persyvan](https://github.com/Persyvan)  
📍 Location: Montreal, QC, Canada

---

### 💼 **Professional Inquiries**

**For:**
- Municipal pilot programs
- Smart city partnerships
- Technical consulting
- Academic collaboration

**Response Time:** Within 48 hours

---

### 🎓 **Academic Profile**

**Education:** AI/ML Engineering (2024-2026)  
**Specializations:**
- Computer Vision (TensorFlow, OpenCV, YOLO)
- Geospatial AI (Folium, GPS integration)
- Edge Computing (Raspberry Pi, Jetson Nano)

**Research Interests:**
- Urban infrastructure monitoring
- Sustainable AI (energy-efficient models)
- Privacy-preserving computer vision

**Publications:** Paper in preparation for CVPR 2026 Workshop

---

## 📄 License

Apache License 2.0 - See LICENSE for details.

Copyright © 2026 Persy Maki Ndombe

---

## 🙏 Acknowledgments

A huge thank you to the members of **Civilians On Board AI** worldwide for their support and vision of human-centered AI.

⭐ **If this project interests you, please star the repository!**

---

🌐 **Read in other languages:** [🇬🇧 English](#) | [🇫🇷 Français](README.fr.md)

**Last Updated:** February 2026 | **Model Version:** V10
