🚗 VIGIL-ROUTE : Système IA de Détection des Défauts Routiers

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9-green.svg)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8-purple.svg)](https://github.com/ultralytics/ultralytics)
[![Précision](https://img.shields.io/badge/Pr%C3%A9cision-87.9%25-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-grey.svg)](LICENSE)

**Système d'apprentissage profond pour la détection automatisée des défauts routiers avec MobileNetV2.**  
*Une solution Edge-AI axée sur la confidentialité pour les villes intelligentes.*

Développé par **Persy Maki ND** | Étudiant en Ingénierie IA/ML

---

**🌐 Langue :** [🇬🇧 English](README.md) | [🇫🇷 Français](#)

---

## 📌 Aperçu du Projet

VIGIL-ROUTE est un système de vision par ordinateur prêt pour la production qui identifie les défauts routiers (nids-de-poule, déformations de chaussée) à partir d'images et de vidéos avec une **précision de 87,9%**.

Conçu pour combler l'écart entre les réparations réactives (plaintes citoyennes) et la maintenance proactive, il introduit un nouvel **Algorithme de Score de Danger** qui priorise les réparations en fonction de la vitesse du véhicule et de la gravité du défaut.

### 🎯 Fonctionnalités Clés

- **🧠 Architecture MobileNetV2** : CNN léger optimisé pour déploiement mobile/edge
- **📸 Fonctionnement Dual-Mode** : 
  - **Mode Citoyen** : Traitement de photos via applications 311 avec extraction GPS EXIF
  - **Mode Flotte** : Analyse vidéo dashcam en temps réel avec overlay HUD
- **📊 Rapports Automatisés** : Rapports Excel avec codes couleur d'urgence + Cartes HTML interactives
- **🌍 Intégration GPS** : 
  - **Citoyen** : Extraction métadonnées EXIF (photos smartphone)
  - **Flotte** : Intégration matérielle OBD-II (télémétrie véhicule)
- **🚨 Score de Risque Adaptatif** : Algorithme de priorisation basé sur la vitesse
- **💧 Résistance à l'Eau** : Entraîné pour détecter les nids-de-poule remplis d'eau (conditions pluvieuses/hivernales)
- **🗺️ Visualisation Géospatiale** : Cartes Folium interactives avec marqueurs de priorité
- **🛡️ Architecture Confidentialité** : Couche de détection YOLOv8 (floutage piétons opérationnel)

---

## 🎬 Démo & Visuels

### Mode Flotte (Analyse Vidéo Temps Réel)
*Traitement dashcam avec overlay HUD et protection de la vie privée*

📹 **Vidéo démo complète** : [Voir sur LinkedIn](#) *(à venir)*

**Sorties Clés :**
- Vidéo annotée avec boîtes de détection
- Score de danger en temps réel
- Cartographie trajectoire GPS
- Rapports Excel avec analyse image par image

### Mode Citoyen (Simulation App 311)
*Traitement de photos smartphone avec géolocalisation automatique*

**Exemples de Résultats :**

| Image d'Entrée | Classification IA | Confiance | Niveau de Risque | Action Requise |
|----------------|-------------------|-----------|------------------|----------------|
| `IMG_2826.jpg` | DÉFORMATION | 98% | 🟠 **ÉLEVÉ** | Inspection Requise |
| `IMG_3288.jpg` | NID-DE-POULE | 96% | 🔴 **CRITIQUE** | Réparation Immédiate |
| `IMG_3052.jpg` | ROUTE SAINE | 100% | 🟢 **AUCUN** | Aucune Action |

---

## 🧠 La Logique "Intelligente" : Score de Risque Adaptatif

VIGIL-ROUTE ne trouve pas seulement des trous ; il évalue le **danger**. Une déformation à 30 km/h est une nuisance ; à 90 km/h, c'est un risque de sécurité.

### 1. Formule de Calcul du Risque

Le système fusionne la confiance de la Vision par Ordinateur avec les données de télémétrie du véhicule :

```python
def analyser_risque(classe, confiance, vitesse):
    """
    Calcule l'urgence basée sur :
    - Type de défaut (nid-de-poule = risque plus élevé)
    - Confiance de l'IA
    - Vitesse du véhicule (vitesse élevée = danger accru)
    """
    if classe == 'route_saine':
        return "🟢 Aucun Défaut", "AUCUNE"
    
    # Score de sévérité de base
    score_base = 1.0 if classe == 'nid_de_poule' else 0.7
    
    # Facteur d'amplification vitesse (exponentiel)
    facteur_vitesse = 1.0 + (vitesse / 50.0) ** 1.2
    
    # Score de danger final
    score_danger = (confiance * score_base) * facteur_vitesse
    
    # Seuils d'urgence
    if score_danger >= 1.5:
        return "🔴 CRITIQUE", "INTERVENTION IMMÉDIATE"
    elif score_danger >= 1.0:
        return "🟠 ÉLEVÉE", "INSPECTION REQUISE"
    elif score_danger >= 0.7:
        return "🟡 MOYENNE", "SURVEILLANCE"
    else:
        return "🟢 FAIBLE", "MONITORING"
2. Seuils de Détection Adaptatifs
Pour réduire les faux positifs à haute vitesse (approche sécurité d'abord), le modèle ajuste dynamiquement sa sensibilité :

Zone de Vitesse	Seuil Nid-de-Poule	Seuil Déformation	Justification
Élevée (≥70 km/h)	45% confiance	60% confiance	Vitesses autoroute nécessitent détection conservatrice
Moyenne (50-69 km/h)	50% confiance	65% confiance	Routes artérielles urbaines
Faible (<50 km/h)	60% confiance	70% confiance	Zones résidentielles permettent filtrage plus strict
Pourquoi c'est important : Un faux positif sur autoroute (70+ km/h) pourrait causer un freinage dangereux. Seuils inférieurs = confiance requise plus élevée = moins de fausses alarmes.

🚛 Modes de Déploiement & Exigences Matérielles
Mode 1 : CITOYEN (Intégration App)
Fonctionnement :

Utilisateurs soumettent photos via applications mobiles 311

Système extrait GPS des métadonnées EXIF (iPhone/Android)

IA classifie type de défaut et urgence

Génère rapport géoréférencé pour dispatch municipal

Matériel : Smartphone uniquement (iOS/Android)
Précision GPS : ±10-50 mètres (GPS grand public)
Statut : ✅ Pleinement Opérationnel

Mode 2 : FLOTTE (Véhicules Municipaux)
Fonctionnement :

Dashcam capture vidéo pendant trajets réguliers

IA analyse images en temps réel (ou post-traitement)

Lecteur OBD-II fournit données vitesse pour score risque

Sorties : vidéo annotée + rapports Excel géoréférencés

⚠️ Exigences Intégration Matérielle :

Bien que le pipeline logiciel soit pleinement fonctionnel, le déploiement flotte réel nécessite intégration matérielle physique :

Composant	Objectif	Statut
Lecteur GPS OBD-II	Localisation véhicule temps réel + vitesse	⚠️ Intégration matérielle en attente
Dashcam	Capture vidéo	✅ Toute caméra MP4 compatible
Appareil Edge	Exécuter inférence IA	✅ Raspberry Pi 4 / Jetson Nano testé
Synchro Données	Alignement horodatage OBD-II ↔ Vidéo	⚠️ Nécessite intégration gestion flotte
Appareils Recommandés :

FreeMatrix OBD-II Bluetooth (~60 $ USD)

Verizon Hum OBD (~10 $/mois cellulaire)

Automatic Pro (~130 $ WiFi + 4G)

Statut Actuel :
✅ Pipeline logiciel prêt
⚠️ Intégration matérielle nécessite partenariat flotte municipale

🛡️ Module Confidentialité & Éthique
La conformité aux lois sur la vie privée (Loi 25 du Québec / RGPD) est un principe de conception fondamental.

Aperçu de l'Architecture
Le système inclut une couche de détection YOLOv8 pour identifier les données personnelles avant stockage :

Fonctionnalité	Technologie	Statut	Note
Protection Piétons	YOLOv8 (Classe 0)	✅ Opérationnel	Détection humaine et flou Gaussien corps entier fonctionnel
Anonymisation Véhicules	YOLOv8 + Détection Géométrique	⚠️ Prototype	Détection plaques immatriculation implémentée comme Preuve-de-Concept. Déploiement production nécessite solutions OCR/Confidentialité spécialisées
Note de Transparence
En tant que projet étudiant en ingénierie IA, VIGIL-ROUTE fournit l'architecture logique pour la protection de la vie privée. Le système de floutage piétons est pleinement fonctionnel, mais l'anonymisation des plaques d'immatriculation nécessiterait collaboration avec spécialistes technologies confidentialité (ex. Brighter AI, D-ID) pour déploiement commercial.

Ce qui fonctionne :

✅ YOLOv8 détecte humains de manière fiable

✅ Flou Gaussien appliqué aux régions détectées

✅ Architecture pipeline axée confidentialité

Ce qui nécessite intégration professionnelle :

⚠️ Détection plaques certifiée (OCR + flou)

⚠️ Audit conformité légale (équipes juridiques municipales)

⚠️ Documentation RGPD/Loi 25 pour approvisionnement municipal

🏗️ Spécifications Techniques
Architecture Modèle (V9)
Composant	Détails
Framework	TensorFlow 2.19.0 / Keras
Modèle de Base	MobileNetV2 (pré-entraîné ImageNet, gelé)
Forme d'Entrée	224×224×3 RGB
Classes	nid_de_poule, deformation_chaussee, route_saine
Dataset	1 584 images annotées (Montréal, oct-déc 2025)
Précision Test	87,90%
Perte Test	0,3664
Temps d'Inférence	~12ms (GPU T4) / ~120ms (CPU Colab)
Pourquoi MobileNetV2 Plutôt que Détection d'Objets ?
Justification Choix de Conception :

Nous avons choisi Classification d'Images (MobileNetV2) plutôt que Détection d'Objets (YOLOv8) pour le modèle de défauts principal afin de maximiser l'efficacité sur appareils edge.

Approche	Modèle	Taille	Inférence	Cas d'Usage
Classification	MobileNetV2	14 Mo	120ms (CPU)	"Y a-t-il un défaut dans ce segment routier ?"
Détection	YOLOv8	44 Mo	200ms (CPU)	"Où exactement est le défaut pixel par pixel ?"
Pourquoi la Classification est Suffisante :

Les municipalités réparent des segments routiers (sections de 100m), pas des pixels individuels. MobileNetV2 fournit l'«Alerte de Zone» nécessaire à 1/3 du coût de calcul et 1/4 de la taille du modèle.

Amélioration Future (V10) : Segmentation YOLOv8 prévue pour estimation précise de profondeur (calcul volume nid-de-poule).

🗂️ Méthodologie du Dataset
Détails de Collecte
Période : Octobre - Décembre 2025
Lieu : Montréal, QC, Canada (divers quartiers)
Conditions : Transition hivernale (pluie, asphalte mouillé, neige légère, sel de route)
Appareil : iPhone (simulation usage app 311 citoyenne)

Pourquoi les Données Hivernales Comptent :

Le climat rigoureux de Montréal crée défis uniques :

💧 Nids-de-poule remplis d'eau (pluies novembre)

🍂 Couverture feuilles automne (octobre)

❄️ Conditions début hiver (sel/neige décembre)

Cette diversité saisonnière assure que le modèle fonctionne toute l'année, pas seulement en conditions ensoleillées idéales.

Distribution des Classes (1 584 Images)
text
deformation_chaussee : ~650 images (41%)
nid_de_poule :         ~580 images (37%)
route_saine :          ~354 images (22%)
Performance par Classe (Jeu de Test) :

Classe	Précision	Rappel	F1-Score
deformation_chaussee	85%	91%	88%
nid_de_poule	83%	74%	79%
route_saine	100%	100%	100%
Constat Clé : Détection parfaite routes saines = Aucune fausse alarme gaspillant ressources municipales.

🚀 Démarrage Rapide
Installation
bash
git clone https://github.com/Persyvan/vigil-route.git
cd vigil-route
pip install -r requirements.txt
Utilisation (Inférence)
python
from scripts.vigil_brain import VigilBrain

# Charger Modèle
brain = VigilBrain('models/vigil_route_classifier_v9.keras')

# Analyser une image
result = brain.analyze('test_images/pothole_01.jpg', speed=60)
print(result)
# Sortie : {'class': 'nid_de_poule', 'confidence': 0.96, 'urgency': 'CRITICAL'}
🔮 Feuille de Route & Travaux Futurs
Statut Actuel (V9 - MVP)
✅ Cœur MobileNetV2 entraîné (87,9% précision)

✅ Pipeline dual-mode opérationnel

✅ Architecture confidentialité implémentée (flou piétons)

✅ Algorithme score risque validé

✅ Génération Excel + carte HTML

Prochaines Étapes
V1.1 (Intégration Matérielle) - 3-6 mois

 Tests GPS OBD-II avec flotte municipale

 Intégration données vitesse temps réel

 Déploiement cloud (AWS Lambda / Google Cloud Run)

V2.0 (Détection Avancée) - 6-12 mois

 Segmentation YOLOv8 pour analyse volumétrique (profondeur nid-de-poule)

 Intégration module confidentialité certifié

 Expansion dataset multi-villes (Toronto, Québec)

V3.0 (Pilote Commercial) - 12+ mois

 Intégration API 311 (Ville de Montréal)

 Programme pilote municipal complet (flotte 10 véhicules)

 Étude validation monde réel

🤝 Contact & Collaboration
Ce projet est un Prototype de Recherche IA Appliquée développé dans le cadre de mes études en ingénierie IA/ML. Je suis ouvert à collaboration avec :

🏙️ Initiatives villes intelligentes

🚗 Départements gestion flottes municipales

🔬 Institutions recherche (Vision par Ordinateur / Infrastructures)

💼 Firmes ingénierie conseil

Persy Maki ND
Étudiant en Ingénierie IA/ML
Spécialisé en Vision par Ordinateur & Villes Intelligentes

📧 Courriel : persy.maki.ml@gmail.com

💼 LinkedIn : Persy Maki ND

🐙 GitHub : @Persyvan

📍 Localisation : Montréal, QC, Canada

📄 Licence
Licence MIT - Voir LICENSE pour détails.

Copyright © 2026 Persy Maki ND

🙏 Remerciements
Dataset : Images routes Montréal auto-collectées (oct-déc 2025)

Framework : TensorFlow, Keras, OpenCV, Ultralytics (YOLOv8)

Plateforme : Google Colab Pro

Inspiration : Systèmes 311 municipaux, surveillance infrastructures villes intelligentes

⭐ Si ce projet vous intéresse, merci d'ajouter une étoile au dépôt !

🌐 Lire dans d'autres langues : 🇬🇧 English

Dernière mise à jour : Janvier 2026 | Version Modèle : V9
