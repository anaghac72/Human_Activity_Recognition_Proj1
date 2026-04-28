# Project Title:-Human Activity Recognition(HAR)
# Team Members:-
| Name            | Course       | Register Number |
|:----------------|:------------:|:---------------:|
| ANAGHA C        | DACS         |     253126      |   
| BEN FLIS ZIYA   | CSDA         |     253018      |
| LANIYA MOHAN    | BioAI        |     253218      |

# Problem Statement :-
Human Activity Recognition (HAR) using smartphone sensor data is an essential predictive analytics task which provides benefits to healthcare and fitness tracking and smart environments. The sensors inside modern smartphones which include accelerometers and gyroscopes create continuous motion data through their measurement functions. This process of converting raw sensor data into accurate activity classifications presents on-going difficulties for researchers in the field.
<br>
The objective of this project is to develop a robust system that can accurately classify human physical activities—such as walking, sitting, standing, running, and stair climbing-using sensor data from smartphones. The project requires researchers to extract time-domain and frequency-domain features from the dataset and use Support Vector Machines (SVM), Random Forest and Long Short-Term Memory (LSTM) networks as machine learning models.

# Dataset Details:-

Dataset: UCI Human Activity Recognition (HAR) Dataset

Source: UCI Machine Learning Repository

Total Samples: ~10,000

Features:
Accelerometer (X, Y, Z)
Gyroscope (x, y, z)
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

# Methdology Overview:-

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

# Results
|     Model               |    Accuracy   |
| ----------------------- |  ------------ |
|     SVM                 |    ~ 95%      |
|   Random Forest         |    ~ 93%      |
|   LSTM                  |    ~ 92%      |

## Evaluation Metrics

---

###  Random Forest

####  Classification Report

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/8e9842e1-d3cf-4da4-b09e-5eeadf8794ce" width="500"/>
</p>

<br>

####  Confusion Matrix

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/611af314-c6d7-40d5-aa58-e749d449ffc1" width="500"/>
</p>

<br><br>

---

###  SVM (Support Vector Machine)

#### Classification Report

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/e0cb976f-8190-46e2-adad-58d25d7f9e13" width="500" />
</p>

<br>

####  Confusion Matrix

<br>

<p align="center">
  <img src="https://github.com/user-attachments/assets/ab7187fc-5b48-4580-8ca9-9107353d05ad" width="500"/>
</p>

<br>

###  LSTM (Long Short Term Memory)

#### Classification Report

<br>

<p align="center">
   <img width="663" height="501" alt="image" src="https://github.com/user-attachments/assets/741a999f-9e92-49cf-b6e6-48f9239ff1f4" />

</p> 

<br>

####  Confusion Matrix

<br>

<p align="center">
  <img width="649" height="547" alt="image" src="https://github.com/user-attachments/assets/dd3f40a4-9ced-4428-b9b1-82c5272681dc" />

</p>

<br>





##  Model Comparison

<br>

<p align="center">
  <img width="630" height="470" alt="image" src="https://github.com/user-attachments/assets/5b610fc8-4df7-4502-af93-202c6baa22ae" />

</p>

<br><br>

##  Accuracy Comparison

<br>

<p align="center">
  <img width="630" height="470" alt="image" src="https://github.com/user-attachments/assets/5e9c2a3a-474a-48bf-b1f2-5da36f1a8b8d" />

</p>
<br>

## Summary 

Support Vector Machine (SVM)
- Achieved the highest accuracy (~95%)
- Performed best across most evaluation metrics

Random Forest
- Delivered strong and stable performance
- Slightly lower accuracy compared to SVM

LSTM
- Captures temporal patterns effectively
- Performance was slightly lower due to need for further tuning
### Conclusion

Among the three models, Support Vector Machine (SVM) achieved the best performance with the highest accuracy and strong evaluation metrics. Its effectiveness can be attributed to its ability to handle high-dimensional feature spaces efficiently.

Random Forest also performed well and provided robust predictions, but slightly underperformed compared to SVM. The LSTM model, although suitable for time-series data, did not outperform classical machine learning models in this implementation, likely due to limited tuning and dataset size.

Overall, SVM proved to be the most suitable model for this Human Activity Recognition task.


#  Application Screenshots

<br>

###  Live Application
 https://humanactivityrecognitionproj1-ayeoz2sbtfwgstmhxy5xtl.streamlit.app/

<br>

###  Home Interface

<p align="center">
  <img width="1600" height="730" alt="image" src="https://github.com/user-attachments/assets/e3af3d2e-6e4f-4c80-b9fd-64aeadcd1d5a" />

</p>

<br>

###  File Upload & Prediction

<p align="center">
  <img width="1600" height="199" alt="image" src="https://github.com/user-attachments/assets/ad9c0e95-b9fa-4aff-a970-a1f8b738567d" />

</p>
<p>
  <img width="1600" height="422" alt="image" src="https://github.com/user-attachments/assets/c2af27c8-e0d5-4055-91be-71b2be74c7e0" />

</p>

<br>

### 📊 Prediction Output & Visualization

<p align="center">
  <img width="1767" height="457" alt="image" src="https://github.com/user-attachments/assets/482b4bbe-eb35-4d76-9cac-a1acc007575a" />

</p>
<p align="center">
  <img width="1600" height="570" alt="image" src="https://github.com/user-attachments/assets/bf46d5e2-50e1-45ad-b449-e7501e4b4dba" />

</p>

<br>

<br>


#  Setup Instructions

<br>

### 1. Clone the Repository
 ⁠bash
git clone https://github.com/anaghac72/Human_Activity_Recognition_Proj1.git
cd Human_Activity_Recognition_Proj1
⁠ `

<br>

### 2. Create Virtual Environment

 ⁠bash
python -m venv venv


⁠ * Windows:

 ⁠bash
venv\Scripts\activate


⁠ * Mac/Linux:

 ⁠bash
source venv/bin/activate


⁠ <br>
### 3. Install Dependencies

 ⁠bash
pip install -r requirements.txt


⁠ <br>

### 4. Run the Application

 ⁠bash
streamlit run app/app.py


<br>

### 5. Open in Browser

[http://localhost:8501](http://localhost:8501)

##  Project Structure

```
Human_Activity_Recognition_Proj1/
├── app/
│   └── app.py
├── models/
│   ├── rf_model.pkl
│   ├── svm_model.pkl
│   └── lstm_model.keras
├── data/
│   ├── train/
│   └── test/
├── results/
│   ├── reports/
│   │   ├── svm_report.txt
│   │   ├── rf_report.txt
│   │   └── lstm_report.txt
│   └── plots/
│       ├── confusion_matrix_rf.png
│       ├── confusion_matrix_svm.png
│       ├── confusion_matrix_lstm.png
│       ├── model_comparison.png
│       └── accuracy_comparison.png
├── notebooks/
│   ├── svm_model.ipynb
│   ├── rf_model.ipynb
│   └── lstm_model.ipynb
├── requirements.txt
└── README.md
```

Presentation Link
https://canva.link/g5gw8s63yeqyumd



# Live Streamlit Deployment
https://humanactivityrecognitionproj1-ayeoz2sbtfwgstmhxy5xtl.streamlit.app

