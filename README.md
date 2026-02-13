🚗 VIGIL-ROUTE: AI Road Defect Detection System

![alt text](https://img.shields.io/badge/Python-3.10+-blue.svg)

![alt text](https://img.shields.io/badge/TensorFlow-2.19-orange.svg)

![alt text](https://img.shields.io/badge/OpenCV-4.9-green.svg)

![alt text](https://img.shields.io/badge/YOLO-v8-purple.svg)

![alt text](https://img.shields.io/badge/Accuracy-87.9%25-brightgreen.svg)

![alt text](https://img.shields.io/badge/License-MIT-grey.svg)

![alt text](https://img.shields.io/badge/%20Hugging%20Face-Public%20Demo-yellow)

Deep Learning system for automated road defect detection using MobileNetV2.
A Privacy-First, Edge-AI solution for Smart Cities.

Developed by Persy Maki Ndombe | AI/ML Engineering Student

🌐 Language: 🇬🇧 English | 🇫🇷 Français

📌 Project Overview

VIGIL-ROUTE is a production-ready computer vision system that identifies road defects (potholes, pavement deformations) from images and videos with 87.9% accuracy.

Designed to bridge the gap between reactive repairs (citizen complaints) and proactive maintenance, it introduces a novel Danger Scoring Algorithm that prioritizes repairs based on vehicle speed and defect severity.

🎯 Key Features

🧠 MobileNetV2 Architecture: Lightweight CNN optimized for mobile/edge deployment.

📸 Dual-Mode Operation:

Citizen Mode: Processes photos from 311 reporting apps with EXIF GPS extraction.

Fleet Mode: Real-time dashcam video analysis with HUD overlay.

📊 Automated Reporting: Excel reports with color-coded urgency + Interactive HTML maps.

🌍 GPS Integration:

Citizen: EXIF metadata extraction (smartphone photos).

Fleet: OBD-II hardware integration (vehicle telemetry).

🚨 Adaptive Risk Scoring: Speed-based urgency prioritization algorithm.

💧 Water Resistance: Trained to detect water-filled potholes (rainy/winter conditions).

🗺️ Geospatial Visualization: Interactive Folium maps with priority markers.

🛡️ Privacy Architecture: YOLOv8-based detection layer (pedestrian blur operational).

🧠 Engineering Choice: Why MobileNetV2?

We deliberately chose Image Classification (MobileNetV2) over Object Detection (YOLO) for the core defect model. This is a strategic Green AI & Efficiency choice:

Ecological Impact: MobileNetV2 consumes significantly less energy. This is critical for battery-powered edge devices running all day.

Hardware Resources: It runs smoothly on standard CPUs (Raspberry Pi, Smartphones) without requiring expensive, power-hungry GPUs.

"Zone Alert" Logic: Municipalities repair road segments (e.g., 100m), not individual pixels. Classification answers the question "Is this segment damaged?" in 12ms, whereas pixel-by-pixel detection is much heavier.

📊 Dataset & Performance (Model V10)

Model Name: vigil_route_semifullseasonv10.keras
Meaning: Semi-Full Season Coverage (Spring, Summer, Autumn, Early Winter).

Dataset Methodology:

Total Images: 1,584 (Montreal, Oct-Dec 2025)

Conditions: Dry, Wet (Nov rain), Autumn leaves, Light snow (<5cm), Road salt, Urban lighting (18h).

Split: 80% Training / 10% Validation / 10% Test.

Distribution and Accuracy:

Deformation: ~650 images (41%)

Pothole: ~580 images (37%)

Healthy Road: ~354 images (22%)

Note on Accuracy (87.9%):
This figure reflects the real-world data imbalance (fewer "perfect" potholes and more complex deformations). However, the model is tuned for safety: Healthy Road detection is 100%, ensuring NO false alarms waste municipal resources.

Robustness by Condition:
| Condition | Accuracy | Status |
| :--- | :--- | :--- |
| ☀️ Dry Roads | 92% | ✅ Production Ready |
| 🌧️ Wet/Rain | 88% | ✅ Validated |
| ❄️ Light Snow (<5cm)| 84% | ✅ Validated |
| 🌆 Evening (Lighting) | 100% | ✅ Validated (18h00) |
| 🌨️ Heavy Snow (>10cm) | N/A | ⚠️ Planned for V11 |

🚀 Quick Start (Live Demo)

Test the V10 Model Instantly without installing any code.
We have deployed a public "Showcase" on Hugging Face that connects to our secure private backend.

![alt text](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Try%20Public%20Demo-yellow)

Perfect for:

Testing the model with your own road images.

Verifying detection accuracy (Pothole vs Deformation).

🎬 Proofs and Visuals
Fleet Mode (Real-Time Video Analysis)

Dashcam processing with HUD overlay and privacy protection

![alt text](demo_outputs/fleet_examples/fleet_frame_01.png)


![alt text](demo_outputs/fleet_examples/fleet_frame_02.png)

📹 Full demo video (2 min): Watch on LinkedIn (coming soon)
🎥 Alternative: Watch on YouTube (unlisted - available upon request)

Key Outputs:

Real-time defect detection with bounding boxes

Danger scoring algorithm in action

GPS trajectory mapping

Frame-by-frame Excel analysis

Citizen Mode (311 App Simulation)

Processing smartphone photos with automatic geolocation

Example Detection Results:

Input Image	AI Classification	Confidence	Risk Level	Action Required

![alt text](demo_outputs/citizen_examples/screenshot_01_pothole.png)
	POTHOLE	98.5%	🔴 CRITICAL	Immediate Repair

![alt text](demo_outputs/citizen_examples/screenshot_02_deformation.png)
	DEFORMATION	98%	🟠 HIGH	Inspection Required

![alt text](demo_outputs/citizen_examples/screenshot_03_healthy.png)
	HEALTHY ROAD	100%	🟢 NONE	No Action
🗺️ Visualizations (Generated Reports)

Instead of raw files, here are screenshots of the generated outputs:

Interactive Map (Clustering & Priority):

![alt text](replace_with_your_map_screenshot.jpg)

Automated Excel Report:

![alt text](replace_with_your_excel_screenshot.jpg)

🧠 The "Smart" Logic: Adaptive Risk Scoring

VIGIL-ROUTE doesn't just find holes; it assesses danger. A deformation at 30 km/h is a nuisance; at 90 km/h, it is a safety hazard.

1. Risk Calculation Formula

The system fuses Computer Vision confidence with vehicle telemetry data:

🧠 Decision Logic: The Danger Score

VIGIL-ROUTE doesn't just find holes, it assesses real-world danger. A deformation at 30 km/h is a nuisance; the same deformation at 90 km/h is a fatal risk.

The system calculates urgency with a simple equation:

Defect Severity × Vehicle Speed = Intervention Priority

How it works?

AI identifies the defect: A Pothole (severe) weighs more than a Deformation (moderate).

System reads the speed: The faster the vehicle, the more the danger score is amplified.

The verdict is instant:

Context	Result	Action Required
🕳️ Pothole at 30 km/h	🟡 MEDIUM	Monitoring
🕳️ Same pothole at 50 km/h	🟠 HIGH	Inspection
🕳️ Same pothole at 90 km/h	🔴 CRITICAL	Immediate Repair

Why this is revolutionary: The same defect changes priority based on road context. Highways (high speed) are protected first, without wasting resources on 30 km/h residential streets.

2. Adaptive Detection Thresholds

To reduce false positives at high speeds (safety-first approach), the model dynamically adjusts its sensitivity:

Speed Zone	Pothole Threshold	Deformation Threshold	Rationale
High (≥70 km/h)	45% confidence	60% confidence	Highway speeds require conservative detection
Medium (50-69 km/h)	50% confidence	65% confidence	Urban arterial roads
Low (<50 km/h)	60% confidence	70% confidence	Residential zones allow stricter filtering

Why this matters: A false positive on a highway (70+ km/h) could cause dangerous braking. Lower thresholds = higher confidence required = fewer false alarms.

3. Customizable Configuration

Municipalities can adjust cost and urgency parameters:

Unit Cost (Pothole): 175 CAD (Default)

Surface Cost (Deformation): 220 CAD/m²

Emergency Surcharge: 1.8x (for P1 Critical)

Winter Surcharge: +20% (Auto-detected Nov-Mar)

🚛 Pilot Program & Deployment

The system is ready for a 1-Month Pilot Deployment.

Pilot Scope:

Citizen Mode Priority: Full integration with the existing Municipal 311 App API.

Fleet Mode Test: Equipment of 1 Municipal Vehicle (Garbage truck or Patrol car) for automated collection.

Hardware Requirements (Fleet):

GPS/Speed: OBD-II Reader.

Vision: Standard Dashcam (1080p).

Compute: Raspberry Pi 4 or Jetson Nano.

⚠️ Hardware Integration Requirements:

While the software pipeline is fully functional, real-world fleet deployment requires physical hardware integration:

Component	Purpose	Status
OBD-II GPS Reader	Real-time vehicle location + speed	⚠️ Hardware integration pending
Dashcam	Video capture	✅ Any MP4 camera compatible
Edge Device	Run AI inference	✅ Raspberry Pi 4 / Jetson Nano tested
Data Sync	OBD-II ↔ Video timestamp alignment	⚠️ Requires fleet management integration

Recommended Devices:

FreeMatrix OBD-II Bluetooth (~$60 USD)

Verizon Hum OBD (~$10/month cellular)

Automatic Pro (~$130 WiFi + 4G)

Current Status:
✅ Software pipeline ready
⚠️ Hardware integration requires municipal fleet partnership

🛡️ Privacy & Ethics Module
Compliance with privacy laws (Quebec Law 25 / GDPR) is a core design principle.

Architecture Overview
The system includes a YOLOv8 detection layer to identify personal data before storage:

Feature	Technology	Status	Note
Pedestrian Protection	YOLOv8 (Class 0)	✅ Operational	Human detection and full-body Gaussian blur functional
Vehicle Anonymization	YOLOv8 + Geometric Detection	⚠️ Prototype	License plate detection implemented as Proof-of-Concept. Production deployment requires specialized OCR/Privacy solutions

What works:

✅ YOLOv8 detects humans reliably

✅ Gaussian blur applied to detected regions

✅ Privacy-first pipeline architecture

What requires professional integration:

⚠️ Certified license plate detection (OCR + blur)

⚠️ Legal compliance audit (city legal teams)

⚠️ GDPR/Law 25 documentation for municipal procurement

🏗️ Technical Specifications
Model Architecture (V10)
| Component | Details |
| :--- | :--- |
| Framework | TensorFlow 2.19.0 / Keras |
| Base Model | MobileNetV2 (ImageNet pretrained, frozen) |
| Input Shape | 224×224×3 RGB |
| Classes | pothole, road_deformation, healthy_road |
| Dataset | 1,584 annotated images (Montreal, Oct-Dec 2025) |
| Test Accuracy | 87.90% |
| Test Loss | 0.3664 |
| Inference Time | ~12ms (GPU T4) / ~120ms (CPU Colab pro) |

🗂️ Dataset Methodology
Collection Details
Period: October - December 2025
Location: Montreal, QC, Canada (various neighborhoods)
Conditions: Winter transition (sun, rain, wet asphalt, light snow, road salt)
Device: iPhone (simulating citizen 311 app usage)

Why Winter Data Matters:

Montreal's harsh climate creates unique challenges:

💧 Water-filled potholes (November rains)

🍂 Autumn leaf coverage (October)

❄️ Early winter conditions (salt/snow December)

This seasonal diversity ensures the model works year-round, not just in ideal sunny conditions.

Class Distribution (1,584 Images)
text
road_deformation: ~650 images (41%)
pothole: ~580 images (37%)
healthy_road: ~354 images (22%)
Per-Class Performance (Test Set):

Class	Precision	Recall	F1-Score
road_deformation	85%	91%	88%
pothole	83%	74%	79%
healthy_road	100%	100%	100%

Key Insight: Perfect detection of healthy roads = No false alarms wasting municipal resources.

📥 Access to Resources (Model, Code, Datasets)

The trained MobileNetV2 model (vigil_route_semifullseasonv10.keras - 89 MB), full training code, and original datasets are currently available upon request only for:

🎓 Academic research collaboration

🏙️ Smart city pilot projects

🔬 Technical evaluation by municipal engineering teams

💼 Employment screening (recruiters/hiring managers)

How to Request Access

📧 Email: persy.maki.ml@gmail.com

Please include in your request:

Your name and affiliation (company/university)

Intended use case

Brief description of your project or evaluation purpose

⏱️ Response time: Access is typically granted within 24-48 hours for legitimate requests.

Future Public Release

The model will eventually be migrated to the 🤗 Hugging Face Hub for public access with the appropriate license.

🔮 Roadmap

V11 (Full Season - 3-6 months): Training on heavy snow, ice storms, and deep night conditions (+500 images).

V12 (Segmentation - 6-12 months): Moving to Volumetric Analysis (Depth calculation) to estimate asphalt volume in liters using YOLOv8 Segmentation.

V13 (Deployment): Full API integration and legal certification.

🤝 Contact & Collaboration
This project is an Applied AI Research Prototype developed as part of my AI/ML engineering studies. I am open to collaboration with:

🏙️ Smart City initiatives

🚗 Municipal fleet management departments

🔬 Research institutions (Computer Vision / Infrastructure)

💼 Engineering consulting firms

Persy Maki Ndombe
AI/ML Engineering Student
Specialized in Computer Vision & Smart Cities

📧 Email: persy.maki.ml@gmail.com

💼 LinkedIn: Persy Maki Ndombe

🐙 GitHub: @Persyvan

📍 Location: Montreal, QC, Canada

📄 License
MIT License - See LICENSE for details.

Copyright © 2026 Persy Maki Ndombe

🙏 Acknowledgments

Special thanks to the members of Civilians On Board AI worldwide for their support and vision of Human-Centric AI.

⭐ If this project interests you, please star the repository!

🌐 Read in other languages: 🇬🇧 English

Last updated: January 2026 | Model Version: V10
