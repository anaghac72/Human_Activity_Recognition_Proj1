# Project Title:-Human Activity Recognition(HAR)
# Team Members:-
| Name            | Course       | Register Number |
|:----------------|:------------:|:---------------:|
| ANAGHA C        | DACS         |     253126      |   
| BEN FLIS ZIYA   | CSDA         |     253018      |
| LANIYA MOHAN    | BioAI        |     253218      |

# Problem Statement :-
Human Activity Recognition (HAR) using smartphone sensor data is an essential predictive analytics task which provides benefits to healthcare and fitness tracking and smart environments. The sensors inside modern smartphones which include accelerometers and gyroscopes create continuous motion data through their measurement functions. The process of converting raw sensor data into accurate activity classifications presents ongoing difficulties for researchers in the field.
The objective of this project is to develop a robust system that can accurately classify human physical activities—such as walking, sitting, standing, running, and stair climbing-using sensor data from smartphones. The project requires researchers to extract time-domain and frequency-domain features from the dataset and use Support Vector Machines (SVM), Random Forest and Long Short-Term Memory (LSTM) networks as machine learning models.

# Dataset Details:-
Dataset Description:-

Dataset: UCI Human Activity Recognition (HAR) Dataset
Source: UCI Machine Learning Repository
Total Samples: ~10,000
Features:
Accelerometer (X, Y, Z)
Gyroscope (X, Y, Z)
Activities (Classes):
- Walking
- Walking Upstairs
- Walking Downstairs
- Sitting
- Standing
- Laying

Class Distribution:-
The dataset is fairly balanced across all six activities.

Dataset link:- https://drive.google.com/drive/folders/14wQNbXFOY0CyP2ej2WcB5WXsz8El4YFV?usp=drive_link

# Methdology Overview:

### Data Preprocessing

| Step | Description |
|------|-------------|
| Load Signals | Inertial sensor signals loaded from raw dataset |
| Normalize | Feature scaling applied to sensor readings |
| Encode Labels | Activity labels converted to numerical format |

---

### Feature Engineering
- Time-series sliding windows
- **128 timesteps × 6 features** (3-axis accelerometer + 3-axis gyroscope)
- Time-domain and frequency-domain features extracted

---

### Model Training

| Model | Type | Feature Input |
|-------|------|---------------|
| Support Vector Machine (SVM) | Classical ML | Handcrafted features |
| Random Forest | Classical ML | Handcrafted features |
| Long Short-Term Memory (LSTM) | Deep Learning | Raw sequence (learned features) |

> Compares handcrafted feature engineering vs. deep learning-based feature extraction.

---

### Evaluation Metrics

| Metric | Purpose |
|--------|---------|
| Accuracy | Overall classification performance |
| Precision | Correctness of positive predictions |
| Recall | Coverage of actual positives |
| F1-Score | Harmonic mean of Precision & Recall |
| Confusion Matrix | Per-class prediction breakdown |

---

###  Generalization Testing
- Models evaluated on **unseen subjects**
- Cross-subject validation to test real-world generalizability
- Final comparison of SVM vs. Random Forest vs. LSTM

---

## 🔁 Pipeline Summary

```
UCI HAR Dataset
      ↓
Data Preprocessing (Normalize → Encode Labels)
      ↓
Feature Engineering (128 timesteps × 6 features)
      ↓
 ┌─────────┬──────────────┬────────┐
 │   SVM   │ Random Forest│  LSTM  │
 └─────────┴──────────────┴────────┘
      ↓
Evaluation (Accuracy · Precision · Recall · F1 · Confusion Matrix)
      ↓
Generalization on Unseen Subjects
      ↓
Model Comparison & Insights

```
# Streamlit App
link : http://192.168.1.4:8502

