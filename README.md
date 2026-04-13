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

| Step           | Description                                                                             |
| -------------- | --------------------------------------------------------------------------------------- |
| Load Data      | Inertial sensor signals (accelerometer & gyroscope) are loaded from the UCI HAR dataset |
| Data Cleaning  | Data is checked for consistency and missing values                                      |
| Normalization  | Standard scaling is applied (important for SVM)                                         |
| Label Encoding | Activity labels are converted into numerical classes (1–6)                              |

---

### Feature Engineering

#### Handcrafted Features (SVM & Random Forest)

| Aspect         | Details                                        |
| -------------- | ---------------------------------------------- |
| Total Features | 561                                            |
| Feature Types  | Time-domain and Frequency-domain               |
| Examples       | Mean, Standard Deviation, Energy, FFT features |

#### Raw Time-Series Input (LSTM)

| Aspect            | Details                                     |
| ----------------- | ------------------------------------------- |
| Window Size       | 128 timesteps                               |
| Features per Step | 6 (3-axis accelerometer + 3-axis gyroscope) |
| Approach          | Sliding window segmentation                 |
| Feature Learning  | Automatic (no manual extraction)            |

---

### Model Training

| Model         | Type          | Input           | Key Advantage                         |
| ------------- | ------------- | --------------- | ------------------------------------- |
| SVM           | Classical ML  | 561 features    | Works well with high-dimensional data |
| Random Forest | Classical ML  | 561 features    | Robust to noise and overfitting       |
| LSTM          | Deep Learning | 128×6 sequences | Captures temporal dependencies        |

---

### Evaluation Metrics

| Metric           | Purpose                              |
| ---------------- | ------------------------------------ |
| Accuracy         | Overall performance                  |
| Precision        | Correctness of positive predictions  |
| Recall           | Ability to identify actual positives |
| F1-score         | Balance between precision and recall |
| Confusion Matrix | Class-wise performance analysis      |

---

### Generalization Testing

| Step                     | Description                                               |
| ------------------------ | --------------------------------------------------------- |
| Unseen Data Testing      | Models are evaluated on subjects not seen during training |
| Cross-Subject Validation | Ensures robustness and real-world applicability           |
| Model Comparison         | Performance of SVM, Random Forest, and LSTM is analyzed   |
# Live Streamlit Deployment
https://humanactivityrecognitionproj1-ayeoz2sbtfwgstmhxy5xtl.streamlit.app

