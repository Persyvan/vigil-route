🚗 VIGIL-ROUTE : Système IA de Détection des Défauts Routiers

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19-orange.svg)](https://www.tensorflow.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.9-green.svg)](https://opencv.org/)
[![YOLOv8](https://img.shields.io/badge/YOLO-v8-purple.svg)](https://github.com/ultralytics/ultralytics)
[![Précision](https://img.shields.io/badge/Pr%C3%A9cision-87.9%25-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-MIT-grey.svg)](LICENSE)
![Hugging Face](https://img.shields.io/badge/%20Hugging%20Face-Démo%20Publique-yellow)

**Système d'apprentissage profond pour la détection automatisée des défauts routiers avec MobileNetV2.**  
*Une solution Edge-AI axée sur la confidentialité pour les villes intelligentes.*

Développé par **Persy Maki Ndombe** | Étudiant en Ingénierie IA/ML

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

## 🧠 Choix Ingénierie : Pourquoi MobileNetV2 ?

Nous avons délibérément choisi la **Classification d'Images (MobileNetV2)** plutôt que la Détection d'Objets (YOLO) pour le cœur du modèle. C'est un choix stratégique d'**Écologie et d'Efficacité** :

1.  **Impact Écologique :** MobileNetV2 consomme nettement moins d'énergie. C'est crucial pour des appareils embarqués sur batterie qui tournent toute la journée.
2.  **Ressources Matérielles :** Il fonctionne parfaitement sur des CPU standards (Raspberry Pi, Smartphones) sans nécessiter de cartes graphiques (GPU) coûteuses et énergivores.
3.  **Logique "Alerte de Zone" :** Les villes réparent des *segments* de route (ex: 100m), pas des pixels. La classification répond à la question *"Ce segment est-il endommagé ?"* en 12ms, alors que la détection pixel par pixel est beaucoup plus lourde.

---
## 📊 Dataset & Performance (Modèle V10)

**Nom du Modèle :** `vigil_route_semifullseasonv10.keras`
**Signification :** Couverture Semi-Complète (Printemps, Été, Automne, Début Hiver).

**Méthodologie du Dataset :**
*   **Total Images :** 1 584 (Montréal, Oct-Déc 2025)
*   **Conditions :** Sec, Mouillé (Pluie Nov), Feuilles automne, Neige légère (<5cm), Sel routier, Éclairage urbain (18h).
*   **Split :** 80% Entraînement / 10% Validation / 10% Test.

**Répartition et Précision :**
*   **Déformation :** ~650 images (41%)
*   **Nid-de-poule :** ~580 images (37%)
*   **Route Saine :** ~354 images (22%)

**Note sur la précision (87,9%) :**
Ce chiffre reflète le déséquilibre réel des données (il y a moins de nids-de-poule "parfaits" et plus de déformations complexes). Cependant, le modèle est réglé pour la sécurité : **La détection des Routes Saines est à 100%**, garantissant qu'aucune fausse alerte ne gaspille les ressources municipales.

**Robustesse par Condition :**
| Condition | Précision | Statut |
| :--- | :--- | :--- |
| ☀️ **Routes Sèches** | **92%** | ✅ Prêt pour Production |
| 🌧️ **Pluie/Mouillé** | **88%** | ✅ Validé |
| ❄️ **Neige Légère (<5cm)**| **84%** | ✅ Validé |
| 🌆 **Soir (Éclairage)** | **100%** | ✅ Validé (18h00) |
| 🌨️ *Neige Forte (>10cm)* | *N/A* | ⚠️ Prévu pour V11 |

---
## 🚀 Démarrage Rapide (Démo Live)

**Testez le Modèle V10 Instantanément** sans installer de code.
Nous avons déployé une "Vitrine" publique sur Hugging Face connectée à notre cerveau sécurisé.

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Lancer%20la%20Démo-yellow)](https://huggingface.co/spaces/PvanAI/vigilroute-brain)
**Parfait pour :**
*   Tester le modèle avec vos propres images de route.
*   Vérifier la précision (Nid-de-poule vs Déformation).

---

## 🎬 Preuves et Visuels

### Mode Flotte (Analyse Vidéo Temps Réel)
*Traitement dashcam avec overlay HUD et protection vie privée*

![Aperçu HUD Flotte](demo_outputs/fleet_examples/fleet_frame_01.png)
![Aperçu HUD Flotte](demo_outputs/fleet_examples/fleet_frame_02.png)

📹 **Vidéo démo complète (2 min) :** [Voir sur LinkedIn](#) *(à venir)*  
🎥 **Alternative :** [Voir sur YouTube](https://youtube.com/...) *(non répertorié - disponible sur demande)*

**Sorties Clés :**
- Détection défauts temps réel avec boîtes délimitation
- Algorithme score danger en action
- Cartographie trajectoire GPS
- Analyse Excel image par image

### Mode Citoyen (Simulation App 311)
*Traitement photos smartphone avec géolocalisation automatique*

**Exemples Résultats Détection :**

| Image d'Entrée | Classification IA | Confiance | Niveau Risque | Action Requise |
|----------------|-------------------|-----------|---------------|----------------|
| ![Photo 1](demo_outputs/citizen_examples/screenshot_01_pothole.png) | **NID-DE-POULE** | 98.5% | 🔴 **CRITIQUE** | Réparation Immédiate |
| ![Photo 2](demo_outputs/citizen_examples/screenshot_02_deformation.png)| **DÉFORMATION** | 98% | 🟠 **ÉLEVÉ** | Inspection Requise |
| ![Photo 3](demo_outputs/citizen_examples/screenshot_03_healthy.png) | **ROUTE SAINE** | 100% | 🟢 **AUCUN** | Aucune Action |


### 🗺️ Visualisations (Rapports Générés)
*Au lieu de fichiers bruts, voici des captures des résultats générés :*

**Carte Interactive (Clustering & Priorité) :**
![Capture Carte](replace_with_your_map_screenshot.jpg)

**Rapport Excel Automatisé :**
![Capture Excel](replace_with_your_excel_screenshot.jpg)

---

## 🧠 La Logique "Intelligente" : Score de Risque Adaptatif

VIGIL-ROUTE ne trouve pas seulement des trous ; il évalue le **danger**. Une déformation à 30 km/h est une nuisance ; à 90 km/h, c'est un risque de sécurité.

### 1. Formule de Calcul du Risque

Le système fusionne la confiance de la Vision par Ordinateur avec les données de télémétrie du véhicule :
## 🧠 Logique de Décision : Le Score de Danger

VIGIL-ROUTE ne se contente pas de trouver des trous, il **évalue le danger réel**. Une déformation à 30 km/h est une nuisance ; la même déformation à 90 km/h est un risque mortel.

Le système calcule l'urgence selon une équation simple :

**Gravité du défaut × Vitesse du véhicule = Priorité d'Intervention**

### Comment ça marche ?

1. **L'IA identifie le défaut** : Un Nid-de-poule (sévère) pèse plus lourd qu'une Déformation (modérée).
2. **Le système lit la vitesse** : Plus le véhicule roule vite, plus le score de danger est multiplié.
3. **Le verdict est immédiat** :

| Contexte | Résultat | Action Requise |
|----------|----------|----------------|
| 🕳️ Nid-de-poule à 30 km/h | 🟡 MOYEN | Surveillance |
| 🕳️ Même nid-de-poule à 50 km/h | 🟠 ÉLEVÉ | Inspection |
| 🕳️ Même nid-de-poule à 90 km/h | 🔴 CRITIQUE | Réparation Immédiate |

**Pourquoi c'est révolutionnaire ?** Un même défaut change de priorité selon le contexte routier. Les autoroutes (vitesse élevée) sont protégées en priorité, sans gaspiller de ressources sur des routes résidentielles à 30 km/h.

### 2. Seuils de Détection Adaptatifs
Pour réduire les faux positifs à haute vitesse (approche sécurité d'abord), le modèle ajuste dynamiquement sa sensibilité :

Zone de Vitesse	Seuil Nid-de-Poule	Seuil Déformation	Justification
Élevée (≥70 km/h)	45% confiance	60% confiance	Vitesses autoroute nécessitent détection conservatrice
Moyenne (50-69 km/h)	50% confiance	65% confiance	Routes artérielles urbaines
Faible (<50 km/h)	60% confiance	70% confiance	Zones résidentielles permettent filtrage plus strict
Pourquoi c'est important : Un faux positif sur autoroute (70+ km/h) pourrait causer un freinage dangereux. Seuils inférieurs = confiance requise plus élevée = moins de fausses alarmes.

### 3. Configuration Personnalisable**
Les municipalités peuvent ajuster les coûts et paramètres :
*   **Coût Unitaire (Nid-de-poule) :** 175 CAD (Défaut)
*   **Coût Surface (Déformation) :** 220 CAD/m²
*   **Majoration Urgence :** 1.8x (pour P1 Critique)
*   **Majoration Hiver :** +20% (Détection auto Nov-Mars)
---

## 🚛 Programme Pilote & Déploiement

Le système est prêt pour un **Déploiement Pilote d'1 Mois**.

**Périmètre du Pilote :**
1.  **Priorité Mode Citoyen :** Intégration complète avec l'API de l'App 311 existante de la ville.
2.  **Test Mode Flotte :** Équipement d'**1 Véhicule Municipal** (Camion poubelle ou patrouille) pour la collecte automatisée.

**Prérequis Matériels (Flotte) :**
*   **GPS/Vitesse :** Lecteur OBD-II.
*   **Vision :** Dashcam Standard (1080p).
*   **Calcul :** Raspberry Pi 4 ou Jetson Nano.

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

Ce qui fonctionne :

✅ YOLOv8 détecte humains de manière fiable

✅ Flou Gaussien appliqué aux régions détectées

✅ Architecture pipeline axée confidentialité

Ce qui nécessite intégration professionnelle :

⚠️ Détection plaques certifiée (OCR + flou)

⚠️ Audit conformité légale (équipes juridiques municipales)

⚠️ Documentation RGPD/Loi 25 pour approvisionnement municipal

🏗️ Spécifications Techniques
Architecture Modèle (V10)
Composant	Détails
Framework	TensorFlow 2.19.0 / Keras
Modèle de Base	MobileNetV2 (pré-entraîné ImageNet, gelé)
Forme d'Entrée	224×224×3 RGB
Classes	nid_de_poule, deformation_chaussee, route_saine
Dataset	1 584 images annotées (Montréal, oct-déc 2025)
Précision Test	87,90%
Perte Test	0,3664
Temps d'Inférence	~12ms (GPU T4) / ~120ms (CPU Colab pro)

🗂️ Méthodologie du Dataset
Détails de Collecte
Période : Octobre - Décembre 2025
Lieu : Montréal, QC, Canada (divers quartiers)
Conditions : Transition hivernale (soleil, pluie, asphalte mouillé, neige légère, sel de route)
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

# 🚗 VIGIL-ROUTE : Système IA de Détection des Défauts Routiers

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.19.0-orange)
![MobileNetV2](https://img.shields.io/badge/Architecture-MobileNetV2-green)
![Hugging Face](https://img.shields.io/badge/🤗%20Hugging%20Face-Démo%20Publique-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

**Système d'apprentissage profond pour la détection automatisée des défauts routiers avec MobileNetV2.**
*Une solution Edge-AI axée sur la confidentialité pour les villes intelligentes.*

**Développé par Persy Maki Ndombe** | Étudiant en Génie IA/ML
**Organisation :** CIVILIANS ON BOARD AI

🌐 **Langue :** [🇬🇧 English](#-english-version) | [🇫🇷 Français](#-version-française)

---

## 📌 Aperçu du Projet
VIGIL-ROUTE est un système de vision par ordinateur prêt pour la production qui identifie les défauts routiers (nids-de-poule, déformations de chaussée) à partir d'images et de vidéos avec une **précision de 87,9%**.

Conçu pour combler l'écart entre les réparations réactives (plaintes citoyennes) et la maintenance proactive, il introduit un nouvel **Algorithme de Score de Danger** qui priorise les réparations en fonction de la vitesse du véhicule et de la gravité du défaut.

---

## 🎯 Fonctionnalités Clés
*   **🧠 Architecture MobileNetV2 :** CNN léger optimisé pour déploiement mobile/edge.
*   **📸 Fonctionnement Dual-Mode :**
    *   **Mode Citoyen :** Traitement de photos via applications 311 avec extraction GPS EXIF.
    *   **Mode Flotte :** Analyse vidéo dashcam en temps réel avec overlay HUD.
*   **📊 Rapports Automatisés :** Rapports Excel avec codes couleur d'urgence + Cartes HTML interactives.
*   **🌍 Intégration GPS :**
    *   *Citoyen :* Extraction métadonnées EXIF (photos smartphone).
    *   *Flotte :* Intégration matérielle OBD-II (télémétrie véhicule).
*   **🚨 Score de Risque Adaptatif :** Algorithme de priorisation basé sur la vitesse.
*   **💧 Résistance à l'Eau :** Entraîné pour détecter les nids-de-poule remplis d'eau (conditions pluvieuses/hivernales).
*   **🗺️ Visualisation Géospatiale :** Cartes Folium interactives avec marqueurs de priorité.
*   **🛡️ Architecture Confidentialité :** Couche de détection YOLOv8 (floutage piétons opérationnel).

---

## 🧠 Choix Ingénierie : Pourquoi MobileNetV2 ?

Nous avons délibérément choisi la **Classification d'Images (MobileNetV2)** plutôt que la Détection d'Objets (YOLO) pour le cœur du modèle. C'est un choix stratégique d'**Écologie et d'Efficacité** :

1.  **Impact Écologique :** MobileNetV2 consomme nettement moins d'énergie. C'est crucial pour des appareils embarqués sur batterie qui tournent toute la journée.
2.  **Ressources Matérielles :** Il fonctionne parfaitement sur des CPU standards (Raspberry Pi, Smartphones) sans nécessiter de cartes graphiques (GPU) coûteuses et énergivores.
3.  **Logique "Alerte de Zone" :** Les villes réparent des *segments* de route (ex: 100m), pas des pixels. La classification répond à la question *"Ce segment est-il endommagé ?"* en 12ms, alors que la détection pixel par pixel est beaucoup plus lourde.

---

## 📊 Dataset & Performance (Modèle V10)

**Nom du Modèle :** `vigil_route_semifullseasonv10.keras`
**Signification :** Couverture Semi-Complète (Printemps, Été, Automne, Début Hiver).

**Méthodologie du Dataset :**
*   **Total Images :** 1 584 (Montréal, Oct-Déc 2025)
*   **Conditions :** Sec, Mouillé (Pluie Nov), Feuilles automne, Neige légère (<5cm), Sel routier, Éclairage urbain (18h).
*   **Split :** 80% Entraînement / 10% Validation / 10% Test.

**Répartition et Précision :**
*   **Déformation :** ~650 images (41%)
*   **Nid-de-poule :** ~580 images (37%)
*   **Route Saine :** ~354 images (22%)

**Note sur la précision (87,9%) :**
Ce chiffre reflète le déséquilibre réel des données (il y a moins de nids-de-poule "parfaits" et plus de déformations complexes). Cependant, le modèle est réglé pour la sécurité : **La détection des Routes Saines est à 100%**, garantissant qu'aucune fausse alerte ne gaspille les ressources municipales.

**Robustesse par Condition :**
| Condition | Précision | Statut |
| :--- | :--- | :--- |
| ☀️ **Routes Sèches** | **92%** | ✅ Prêt pour Production |
| 🌧️ **Pluie/Mouillé** | **88%** | ✅ Validé |
| ❄️ **Neige Légère (<5cm)**| **84%** | ✅ Validé |
| 🌆 **Soir (Éclairage)** | **100%** | ✅ Validé (18h00) |
| 🌨️ *Neige Forte (>10cm)* | *N/A* | ⚠️ Prévu pour V11 |

---

## 🚀 Démarrage Rapide (Démo Live)

**Testez le Modèle V10 Instantanément** sans installer de code.
Nous avons déployé une "Vitrine" publique sur Hugging Face connectée à notre cerveau sécurisé.

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Lancer%20la%20Démo-yellow)](https://huggingface.co/spaces/PvanAI/vigilroute-demo)

**Parfait pour :**
*   Tester le modèle avec vos propres images de route.
*   Vérifier la précision (Nid-de-poule vs Déformation).
*   Voir les scores de confiance en action.

*(Note : Le code téléchargeable dans ce dépôt concerne l'architecture et la logique. Les poids du modèle sont sécurisés via l'API de démo).*

---

## 🎬 Preuves et Visuels

### 📸 Exemples Mode Citoyen
*Captures d'écran de détection sur smartphone.*

![Preuve Mode Citoyen 1](replace_with_your_citizen_image_1.jpg)
*Détection d'un nid-de-poule rempli d'eau sous la pluie.*

![Preuve Mode Citoyen 2](replace_with_your_citizen_image_2.jpg)
*Détection d'une déformation de la chaussée.*

### 🚗 Exemples Mode Flotte
*Analyse temps réel depuis dashcam véhicule.*

![Preuve Mode Flotte 1](replace_with_your_fleet_image_1.jpg)
*Overlay HUD montrant l'évaluation du risque en direct.*

### 🗺️ Visualisations (Rapports Générés)
*Au lieu de fichiers bruts, voici des captures des résultats générés :*

**Carte Interactive (Clustering & Priorité) :**
![Capture Carte](replace_with_your_map_screenshot.jpg)

**Rapport Excel Automatisé :**
![Capture Excel](replace_with_your_excel_screenshot.jpg)

---

## 🧠 La Logique "Intelligente" : Score de Risque

VIGIL-ROUTE ne trouve pas seulement des trous ; il évalue le danger. Une déformation à 30 km/h est une nuisance ; à 90 km/h, c'est un risque mortel.

**1. Formule de Calcul**
Le système calcule l'urgence :
`Gravité du défaut × Vitesse du véhicule = Priorité d'Intervention`

**Le verdict est immédiat :**
| Contexte | Résultat | Action Requise |
| :--- | :--- | :--- |
| 🕳️ Nid-de-poule à 30 km/h | 🟡 MOYEN | Surveillance |
| 🕳️ Même défaut à 50 km/h | 🟠 ÉLEVÉ | Inspection |
| 🕳️ Même défaut à 90 km/h | 🔴 CRITIQUE | Réparation Immédiate |

**2. Configuration Personnalisable**
Les municipalités peuvent ajuster les coûts et paramètres :
*   **Coût Unitaire (Nid-de-poule) :** 175 CAD (Défaut)
*   **Coût Surface (Déformation) :** 220 CAD/m²
*   **Majoration Urgence :** 1.8x (pour P1 Critique)
*   **Majoration Hiver :** +20% (Détection auto Nov-Mars)

---

## 🚛 Programme Pilote & Déploiement

Le système est prêt pour un **Déploiement Pilote d'1 Mois**.

**Périmètre du Pilote :**
1.  **Priorité Mode Citoyen :** Intégration complète avec l'API de l'App 311 existante de la ville.
2.  **Test Mode Flotte :** Équipement d'**1 Véhicule Municipal** (Camion poubelle ou patrouille) pour la collecte automatisée.

**Prérequis Matériels (Flotte) :**
*   **GPS/Vitesse :** Lecteur OBD-II.
*   **Vision :** Dashcam Standard (1080p).
*   **Calcul :** Raspberry Pi 4 ou Jetson Nano.

---

## 🛡️ Module Confidentialité & Éthique
La conformité aux lois sur la vie privée (Loi 25 du Québec / RGPD) est fondamentale.

*   **Protection Piétons :** YOLOv8 (Classe 0) détecte les humains et applique un flou gaussien intégral *avant* la sauvegarde des données.
*   **Minimisation des Données :** Les images de routes saines sont écartées pour économiser le stockage et protéger la vie privée.

---

## 📥 Accès aux Ressources (Modèle, Code, Datasets)

Le **modèle MobileNetV2 entraîné** (`vigil_route_semifullseasonv10.keras` - 89 Mo), le code d'entraînement complet et les datasets originaux ne sont pour le moment disponibles que **sur demande** pour :

- 🎓 Collaboration de recherche académique
- 🏙️ Projets pilotes de villes intelligentes
- 🔬 Évaluation technique par équipes d'ingénierie municipale
- 💼 Évaluation de recrutement (recruteurs/gestionnaires d'embauche)

### Comment Demander l'Accès

📧 **Courriel :** persy.maki.ml@gmail.com

**Veuillez inclure dans votre demande :**
1. Votre nom et affiliation (entreprise/université)
2. Cas d'utilisation prévu
3. Brève description de votre projet ou objectif d'évaluation

**⏱️ Délai de réponse :** Accès généralement accordé sous 24-48h pour les demandes légitimes.

### Publication Publique Future
Le modèle sera ultérieurement migré vers le **🤗 Hugging Face Hub** pour un accès public avec la licence appropriée une fois la phase de validation pilote terminée.

---
## 🔮 Feuille de Route (Roadmap)

*   **V11 (Full Season - 3-6 mois) :** Entraînement sur tempêtes, verglas et nuit profonde (+500 images).
*   **V12 (Segmentation - 6-12 mois) :** Passage à l'analyse volumétrique (calcul profondeur) pour estimer le volume d'asphalte en litres via Segmentation YOLOv8.
*   **V13 (Déploiement) :** Intégration API complète et certifications légales.

---
🤝 Contact & Collaboration
Ce projet est un Prototype de Recherche IA Appliquée développé dans le cadre de mes études en ingénierie IA/ML. Je suis ouvert à collaboration avec :

🏙️ Initiatives villes intelligentes

🚗 Départements gestion flottes municipales

🔬 Institutions recherche (Vision par Ordinateur / Infrastructures)

💼 Firmes ingénierie conseil

Persy Maki Ndombe
Étudiant en Ingénierie IA/ML
Spécialisé en Vision par Ordinateur & Villes Intelligentes

📧 Courriel : persy.maki.ml@gmail.com

💼 LinkedIn : Persy Maki Ndombe

🐙 GitHub : @Persyvan

📍 Localisation : Montréal, QC, Canada

📄 Licence
Licence MIT - Voir LICENSE pour détails.

Copyright © 2026 Persy Maki Ndombe

🙏 Remerciements

Un grand merci aux membres de **Civilians On Board AI** à travers le monde pour leur soutien et leur vision d'une IA centrée sur l'humain.

⭐ Si ce projet vous intéresse, merci d'ajouter une étoile au dépôt !

🌐 Lire dans d'autres langues : 🇬🇧 English

Dernière mise à jour : Janvier 2026 | Version Modèle : V10
