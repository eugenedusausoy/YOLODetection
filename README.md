# YOLO11 Video Object Detection Project

## Overview
This project utilizes a fine-tuned **YOLO11n** model to perform object detection on videos. The output includes a video annotated with detection results and a JSON file containing detailed detection data (e.g., class name, confidence score, and bounding box coordinates). The project supports customization of frame intervals for JSON extraction and includes GPU acceleration for faster inference.

## Key Features
- Fine-tuned **YOLO11n** model for enhanced detection accuracy.
- Processes video frame by frame and saves annotated output.
- Generates a JSON file containing detection information for selected frames.
- Configurable frame interval for JSON generation.
- Designed for high-performance inference using GPU.

## Training Details
- **Model**: YOLO11n, fine-tuned on **COCO8**, a subset of the COCO dataset.
- **Dataset for Fine-Tuning**: [COCO8 Dataset](https://cocodataset.org).
- **Video Dataset**: Training and testing videos are sourced from the [ImageNet-VidVRD](https://xdshang.github.io/docs/imagenet-vidvrd.html) dataset.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/yolo11-video-object-detection.git
   cd yolo11-video-object-detection
   ```
2. Install dependencies:
   ```bash
   pip install ultralytics opencv-python-headless
   ```

## How to Use
1. Place your input video in the working directory.
2. Update the `input_video_path` variable in the script to point to your video file.
3. Run the script:
   ```bash
   python yolo_video_detection.py
   ```
4. The script will output:
   - An annotated video (`output_video.mp4`) saved in the working directory.
   - A JSON file (`detections.json`) containing detection details.

## Example JSON Output
```json
{
  "frame": 90,
  "fps_time": 3.0,
  "detections": [
    {
      "confidence": 0.92,
      "class_id": 0,
      "class_name": "car"
    },
    {
      "confidence": 0.85,
      "class_id": 1,
      "class_name": "person"
    }
  ]
}
```

## Configuration
- **Frame Interval for JSON Extraction**: Adjust the `interval_seconds` variable to change how frequently detection data is saved to the JSON file.
- **Video Properties**: The script dynamically retrieves FPS and frame size to adapt to the input video.

## Dataset Sources
- **Training Images**: [COCO8 Dataset](https://cocodataset.org)
- **Training and Testing Videos**: [ImageNet-VidVRD Dataset](https://xdshang.github.io/docs/imagenet-vidvrd.html)

## Acknowledgments
- YOLOv11 Model: [Ultralytics YOLO](https://github.com/ultralytics)
- Video Dataset: [ImageNet-VidVRD](https://xdshang.github.io/docs/imagenet-vidvrd.html)
- Training Dataset: [COCO8](https://cocodataset.org)

---

# Projet de Détection d'Objets Vidéo avec YOLO11

## Vue d'ensemble
Ce projet utilise un modèle **YOLO11n** affiné pour effectuer la détection d'objets dans des vidéos. Le résultat inclut une vidéo annotée avec les détections et un fichier JSON contenant des données détaillées (par exemple, nom de la classe, score de confiance, et coordonnées des boîtes englobantes). Le projet permet de personnaliser l'intervalle des images pour l'extraction JSON et inclut l'accélération GPU pour une inférence rapide.

## Principales fonctionnalités
- Modèle **YOLO11n** affiné pour une meilleure précision de détection.
- Traite les vidéos image par image et sauvegarde les résultats annotés.
- Génère un fichier JSON contenant les informations de détection pour les images sélectionnées.
- Intervalle configurable pour la génération JSON.
- Conçu pour une inférence performante avec un GPU.

## Détails de l'entraînement
- **Modèle** : YOLO11n, affiné avec **COCO8**, un sous-ensemble du dataset COCO.
- **Dataset pour Affinement** : [Dataset COCO8](https://cocodataset.org).
- **Dataset Vidéo** : Les vidéos d'entraînement et de test proviennent du dataset [ImageNet-VidVRD](https://xdshang.github.io/docs/imagenet-vidvrd.html).

## Installation
1. Clonez ce dépôt :
   ```bash
   git clone https://github.com/yourusername/yolo11-video-object-detection.git
   cd yolo11-video-object-detection
   ```
2. Installez les dépendances :
   ```bash
   pip install ultralytics opencv-python-headless
   ```

## Comment Utiliser
1. Placez votre vidéo d'entrée dans le répertoire de travail.
2. Mettez à jour la variable `input_video_path` dans le script pour indiquer votre fichier vidéo.
3. Exécutez le script :
   ```bash
   python yolo_video_detection.py
   ```
4. Le script produira :
   - Une vidéo annotée (`output_video.mp4`) sauvegardée dans le répertoire de travail.
   - Un fichier JSON (`detections.json`) contenant les détails de détection.

## Exemple de sortie JSON
```json
{
  "frame": 90,
  "fps_time": 3.0,
  "detections": [
    {
      "confidence": 0.92,
      "class_id": 0,
      "class_name": "car"
    },
    {
      "confidence": 0.85,
      "class_id": 1,
      "class_name": "person"
    }
  ]
}
```

## Configuration
- **Intervalle des Images pour l'Extraction JSON** : Ajustez la variable `interval_seconds` pour modifier la fréquence d'enregistrement des données de détection dans le fichier JSON.
- **Propriétés Vidéo** : Le script récupère dynamiquement les FPS et la taille des images pour s'adapter à la vidéo d'entrée.

## Sources des Datasets
- **Images d'entraînement** : [Dataset COCO8](https://cocodataset.org)
- **Vidéos d'entraînement et de test** : [Dataset ImageNet-VidVRD](https://xdshang.github.io/docs/imagenet-vidvrd.html)

## Remerciements
- Modèle YOLOv11 : [Ultralytics YOLO](https://github.com/ultralytics)
- Dataset Vidéo : [ImageNet-VidVRD](https://xdshang.github.io/docs/imagenet-vidvrd.html)
- Dataset d'entraînement : [COCO8](https://cocodataset.org)
