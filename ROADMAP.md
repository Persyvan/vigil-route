# 🗺️ VIGIL-ROUTE Development Roadmap

**Project Status:** Pilot Phase (Q1 2026)  
**Current Version:** v10 (87.9% accuracy)  
**Last Updated:** February 2026

---

## 📍 Current Phase: Pilot & Validation

### ✅ Completed Milestones

- [x] **Core AI Model** - MobileNetV2 trained on 1,584 Montreal road images
- [x] **Dual-Mode Architecture** - Citizen (311 app) + Fleet (dashcam) modes
- [x] **Hugging Face Deployment** - Live demo at [pvanAI/vigilroute-brain](https://huggingface.co/spaces/pvanAI/vigilroute-brain)
- [x] **Geographic Visualization** - Interactive map with clustering and priority
- [x] **Automated Reporting** - Excel export with risk analysis
- [x] **Open Source Documentation** - Complete README (FR/EN), contributing guidelines
- [x] **MIT License** - Open source with commercial flexibility

---

## 🎯 Roadmap by Quarter

### **Q1 2026 (Current) - Pilot Validation**

**Status:** 🔄 In Progress

- [x] Model v10 deployment (87.9% accuracy)
- [x] Hugging Face Space launch
- [x] Complete documentation (GitHub + demo)
- [ ] Collect user feedback from Hugging Face community
- [ ] Initial pilot discussions with Montreal municipalities
- [ ] Performance benchmarking on diverse road conditions

**Goal:** Validate system with 100+ real-world tests

---

### **Q2 2026 - Municipal Pilot Program**

**Status:** ⏳ Planned

#### Technical Enhancements
- [ ] **Model v11** - Expand training dataset to 3,000+ images
- [ ] **Multi-weather optimization** - Improve snow/rain detection
- [ ] **Edge deployment** - TensorFlow Lite for mobile devices
- [ ] **Real-time video processing** - Frame-by-frame dashcam analysis

#### Partnerships
- [ ] Partner with 1-2 Quebec municipalities for pilot
- [ ] Fleet vehicle integration (taxi/bus companies)
- [ ] Citizen beta testing program (311 app prototype)

#### Infrastructure
- [ ] Backend API development (FastAPI/Flask)
- [ ] Database for detection storage (PostgreSQL + PostGIS)
- [ ] User authentication system
- [ ] Privacy compliance audit (GDPR/Quebec Law 25)

**Goal:** Deploy with 50-100 active users (citizens + fleet vehicles)

---

### **Q3 2026 - Scale & Monetization**

**Status:** ⏳ Planned

#### Product Development
- [ ] **Mobile app MVP** - iOS/Android native apps
- [ ] **Fleet dashboard** - Real-time monitoring for transport companies
- [ ] **Municipal portal** - Analytics dashboard for city engineers
- [ ] **API access** - Developer-friendly API for integrations

#### Business Model
- [ ] **Freemium for citizens** - Free 311 reporting, premium features
- [ ] **Fleet subscriptions** - $X/vehicle/month for companies
- [ ] **Municipal licensing** - Annual contracts with cities
- [ ] **Data partnerships** - Anonymized road data sales

#### Geographic Expansion
- [ ] Expand to Toronto, Ontario
- [ ] Expand to other Quebec cities (Quebec City, Laval, Gatineau)
- [ ] Pilot discussions with US cities (cold climate zones)

**Goal:** 500+ active users, 2-3 paying municipal contracts

---

### **Q4 2026 - Enterprise & AI Improvements**

**Status:** ⏳ Planned

#### AI/ML Advancements
- [ ] **YOLOv8 integration** - Object detection for defect localization
- [ ] **Model v12** - Target 92%+ accuracy
- [ ] **Severity classification** - Fine-grained risk levels (5 categories)
- [ ] **Predictive maintenance** - ML model for defect progression

#### Enterprise Features
- [ ] **White-label solution** - Rebrandable for municipalities
- [ ] **Multi-tenant architecture** - City-specific data isolation
- [ ] **Advanced analytics** - Budget optimization recommendations
- [ ] **Integration APIs** - Connect with existing city work order systems

#### Infrastructure
- [ ] **Cloud scalability** - AWS/GCP deployment for high traffic
- [ ] **CDN for maps** - Fast geographic visualizations
- [ ] **Redundancy & backups** - 99.9% uptime SLA

**Goal:** 1,000+ users, 5-10 municipal contracts, $100K+ ARR

---

## 🚀 Long-Term Vision (2027+)

### **2027 - National Expansion**

- [ ] Expand across Canada (all provinces)
- [ ] Launch in US cold climate states (Northeast, Midwest)
- [ ] Partnerships with national fleet operators (FedEx, UPS, Canada Post)
- [ ] **Model v13** - Multi-country training data (Canada, US, Europe)

### **2028 - AI Research & Innovation**

- [ ] **Real-time AI repair recommendations** - Cost estimation automation
- [ ] **Climate impact modeling** - Predict seasonal defect patterns
- [ ] **Integration with autonomous vehicles** - Real-time hazard alerts
- [ ] **Public dataset release** - Contribute to open research community

### **2030 - Smart City Platform**

- [ ] Full infrastructure monitoring suite (roads, bridges, sidewalks)
- [ ] IoT sensor integration (vibration, temperature)
- [ ] Blockchain for transparent maintenance records
- [ ] International standard for road defect classification

---

## 📊 Success Metrics

### **Technical KPIs**
- Model accuracy: 87.9% → 95% by end of 2026
- Detection latency: <2 seconds per image
- System uptime: 99.5% → 99.9%
- Mobile app rating: 4.5+ stars

### **Business KPIs**
- Active users: 100 → 5,000 by end of 2026
- Municipal contracts: 0 → 10 by Q4 2026
- Annual Recurring Revenue: $0 → $500K by 2027
- Fleet vehicles monitored: 0 → 500 by Q3 2026

### **Impact KPIs**
- Road defects reported: 1,000+ by Q4 2026
- Estimated cost savings for cities: $1M+ by 2027
- Citizen safety incidents prevented: Measurable by 2027

---

## 🤝 Partnership Opportunities

We're actively seeking partnerships in:

### **Municipalities**
- Pilot programs for road monitoring
- Integration with existing 311 systems
- Data sharing agreements (anonymized)

### **Fleet Operators**
- Taxi companies (dashcam integration)
- Public transit (buses with onboard cameras)
- Delivery fleets (UPS, FedEx, Amazon)

### **Academic Institutions**
- Dataset contributions
- Computer vision research collaboration
- Internship/co-op programs

### **Technology Partners**
- Mobile app development
- Cloud infrastructure (AWS/GCP credits)
- Mapping platforms (Google Maps API, Mapbox)

---

## 📧 Get Involved

**Interested in piloting Vigil Route AI?**

- 🏙️ **Municipalities:** Contact for pilot program details
- 🚚 **Fleet Operators:** Beta access for dashcam integration
- 🎓 **Researchers:** Collaboration on dataset and publications
- 💼 **Investors:** Pitch deck available on request

**Contact:**  
📧 persy.maki.ml@gmail.com  
💼 [LinkedIn: Persy Maki Ndombe](https://linkedin.com/in/persy-maki-ndombe)  
🐙 [GitHub: @Persyvan](https://github.com/Persyvan)

---

## 📜 Version History

| Version | Date | Key Features | Accuracy |
|---------|------|--------------|----------|
| v10 | Feb 2026 | Hugging Face deployment, dual-mode, interactive maps | 87.9% |
| v9 | Jan 2026 | Open world deployment, risk analysis | 87.2% |
| v8 | Dec 2025 | Transfer learning optimization | 85.4% |
| v7 | Nov 2025 | Multi-weather training | 83.1% |
| v6 | Oct 2025 | Initial prototype | 78.5% |

---

**Last Updated:** February 14, 2026  
**Project Lead:** Persy Maki Ndombe | AI/ML Engineering Student  
**Status:** 🟢 Active Development
