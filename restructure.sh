#!/bin/bash

echo "🚀 VIGIL-ROUTE Repository Restructure Script"
echo "=============================================="
echo ""

# 1. Supprimer obsolètes
echo "📁 Step 1/8: Removing obsolete folders..."
git rm -rf demo_outputs/fleet_examples.old 2>/dev/null || echo "   ⚠️  fleet_examples.old not found (skip)"
echo "   ✅ Done"
echo ""

# 2. Nettoyer models/ (garde structure)
echo "🧠 Step 2/8: Cleaning models/ folder..."
cd models || { echo "   ❌ models/ folder not found"; exit 1; }
git rm *.keras 2>/dev/null || echo "   ⚠️  No .keras files to remove"

cat > README.md << 'ENDOFFILE'
# 🧠 Model Files

The trained MobileNetV2 model is NOT stored in this repository due to file size constraints.

## Model Access

Available on request for municipal pilot programs, academic research, or technical evaluation.

Contact: persy.maki.ml@gmail.com

## Model Storage

The production model is hosted on:
- HuggingFace Space: vigilroute-brain (demo)
- Google Drive: Secure vault (production model)

Model Version: V10 (February 2026)
ENDOFFILE

cat > .gitignore << 'ENDOFFILE'
*.keras
*.h5
*.weights
*.pb
!.gitignore
!README.md
ENDOFFILE

cd ..
echo "   ✅ models/README.md created"
echo "   ✅ models/.gitignore created"
echo ""

# 3. Réorganiser notebooks
echo "📓 Step 3/8: Reorganizing notebooks/ folder..."
cd notebooks || { echo "   ❌ notebooks/ folder not found"; exit 1; }
mkdir -p 01_training 02_inference 03_evaluation

cat > README.md << 'ENDOFFILE'
# Notebooks

Jupyter notebooks for VIGIL-ROUTE development and testing.

Structure:
- 01_training: Model training scripts
- 02_inference: Demo notebooks (Citizen & Fleet modes)
- 03_evaluation: Performance analysis

Contact: persy.maki.ml@gmail.com
ENDOFFILE

mv Vigil_Route_Demo.ipynb 02_inference/ 2>/dev/null || echo "   ⚠️  Notebook already moved"

echo "   ✅ notebooks/ reorganized"
cd ..
echo ""

# 4. Créer CONTRIBUTING.md
echo "🤝 Step 4/8: Creating CONTRIBUTING.md..."
cat > CONTRIBUTING.md << 'ENDOFFILE'
# Contributing to VIGIL-ROUTE

This project is currently in Pilot Evaluation Phase. Public contributions will be enabled after Q2-Q3 2026.

Contact: persy.maki.ml@gmail.com
LinkedIn: linkedin.com/in/persy-maki-ndombe

Areas of Interest:
- Municipal partnerships
- Academic collaboration
- Dataset contributions
- Edge deployment optimizations

Last Updated: February 2026
ENDOFFILE

echo "   ✅ CONTRIBUTING.md created"
echo ""

# 5. Créer .github/
echo "🔧 Step 5/8: Creating .github/ templates..."
mkdir -p .github/ISSUE_TEMPLATE

cat > .github/ISSUE_TEMPLATE/pilot_inquiry.md << 'ENDOFFILE'
---
name: Municipal Pilot Inquiry
about: Request pilot program information
title: '[PILOT] '
---

## Organization Information
- Municipality/City:
- Department:
- Contact Name:
- Email:

## Pilot Details
- Fleet Size:
- Duration (months):
- Budget Range:
- Target Start Date:
ENDOFFILE

echo "   ✅ .github/ISSUE_TEMPLATE/ created"
echo ""

# 6. Vérifier demo_outputs
echo "📸 Step 6/8: Checking demo_outputs..."
echo "   ✅ demo_outputs/ OK"
echo ""

# 7. Vérifier LICENSE
echo "📄 Step 7/8: Checking LICENSE..."
echo "   ✅ LICENSE OK"
echo ""

# 8. Staging
echo "📦 Step 8/8: Staging changes..."
git add .
echo "   ✅ All changes staged"
echo ""

echo "=============================================="
echo "✅ Repository restructure COMPLETE!"
echo ""

