# Project Title:-Human Activity Recognition(HAR)
# Team Members:-
| Name            | Course       | Register Number |
|:----------------|:------------:|:---------------:|
| ANAGHA C        | DACS         |     253126      |   
| BEN FLIS ZIYA   | CSDA         |     253018      |
| LANIYA MOHAN    | BioAI        |     253218      |

# Problem Statement :-
Human Activity Recognition (HAR) using smartphone sensor data is an essential predictive analytics task which provides benefits to healthcare and fitness tracking and smart environments. The sensors inside modern smartphones which include accelerometers and gyroscopes create continuous motion data through their measurement functions. The process of converting raw sensor data into accurate activity classifications presents ongoing difficulties for researchers in the field.
<br>
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
### LSTM(Long Short Term Memory)





##  Model Comparison

<br>

<p align="center">
  <img width="630" height="470" alt="Model Comparison"
  src="https://github.com/user-attachments/assets/f1cb7fcc-68bc-44c8-8dcb-4d82335cbefb" />
</p>

<br><br>

##  Accuracy Comparison

<br>

<p align="center">
  <img width="567" height="455" alt="Accuracy Comparison"
  src="https://github.com/user-attachments/assets/8ffc85d4-7260-4b1b-aa50-6f7770248ea0" />
</p>
<br>

## Summary 

Random Forest
     - Achieved the highest accuracy
     - Best overall performance across metrics
SVM
     - Good performance but slightly lower than RF
LSTM
     - Captures temporal patterns but requires more tuning
### Conclusion

Random Forest performed best in this project, achieving the highest accuracy and overall evaluation metrics. It effectively handled high-dimensional features and provided robust predictions. Although LSTM is suitable for time-series data, it did not outperform Random Forest in this implementation.

## 📸 Application Screenshots

<br>
`md
## ⚙️ Setup Instructions

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


```
### 🔗 Live Application
👉 https://humanactivityrecognitionproj1-ayeoz2sbtfwgstmhxy5xtl.streamlit.app/

<br>

### 🖥️ Home Interface

<p align="center">
  <img width="1600" height="730" alt="WhatsApp Image 2026-04-17 at 8 40 15 PM" src="https://github.com/user-attachments/assets/b9fabc70-2e4e-45ac-b0ed-573a182d6df2" />

</p>

<br>

### 📂 File Upload & Prediction

<p align="center">
  <img width="1600" height="199" alt="WhatsApp Image 2026-04-17 at 8 40 41 PM" src="https://github.com/user-attachments/assets/02a8da3c-8516-48c6-ad72-8bd8cd851015" />

</p>
<p align="center">
   <img width="1600" height="422" alt="WhatsApp Image 2026-04-17 at 8 41 19 PM" src="https://github.com/user-attachments/assets/f3544c4a-8feb-4d1e-98d5-c3f2cb6eca85" />


</p>
<br>

### 📊 Prediction Output & Visualization

<p align="center">

</p>
<p align="center">
  <img width="1600" height="570" alt="WhatsApp Image 2026-04-17 at 8 41 38 PM" src="https://github.com/user-attachments/assets/923f5b40-3ed4-428f-a84e-9467e31b87e7" />

</p>

<br>


# Live Streamlit Deployment
https://humanactivityrecognitionproj1-ayeoz2sbtfwgstmhxy5xtl.streamlit.app

