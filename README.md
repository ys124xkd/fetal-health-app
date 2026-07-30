# 👶 Fetal Health Prediction App

Fetal Health Prediction App is a web-based application developed using **Python Flask** to predict fetal health conditions based on **Cardiotocography (CTG)** data. The application utilizes multiple **Machine Learning** algorithms to classify fetal health into **Normal**, **Suspect**, or **Pathological** conditions.

---

## 📖 Overview

Cardiotocography (CTG) is a medical technique used to monitor fetal well-being during pregnancy by recording fetal heart rate and uterine contractions.

This application enables users to enter CTG parameters through a web interface. The input data is processed using trained machine learning models to predict fetal health conditions, providing an early decision-support tool for healthcare analysis.

---

## ✨ Features

- CTG data input through a web interface
- Automatic fetal health prediction
- Real-time classification results
- Feature selection using **SelectKBest**
- Comparison of multiple machine learning algorithms
- Model performance evaluation
- Flask-based web application

---

## 🤖 Machine Learning Algorithms

The project implements and compares the following classification algorithms:

- Decision Tree
- Naive Bayes
- Random Forest

Among these models, **Random Forest** achieved the best overall performance and was selected as the primary prediction model used in the application.

---

## 🛠️ Technologies

- Python
- Flask
- Scikit-learn
- Pandas
- NumPy
- HTML
- CSS

---

## 📂 Project Structure

```text
fetal-health-prediction/
│
├── app.py
├── README.md
├── requirements.txt
│
├── assets/
├── data/
├── templates/
│
├── decision_tree_model.pkl
├── naive_bayes_model.pkl
├── random_forest_model.pkl
├── model_accuracies.pkl
├── rf_accuracy.pkl
│
├── selected_features.json
└── selected_features.pkl
```

---

## 📊 Dataset

This project uses the **Fetal Health Dataset**, which is based on **Cardiotocography (CTG)** recordings.

The dataset includes features such as:

- Baseline value
- Accelerations
- Fetal movement
- Uterine contractions
- Light decelerations
- Severe decelerations
- Prolonged decelerations
- Abnormal short-term variability
- Mean value of short-term variability
- Percentage of time with abnormal long-term variability
- Histogram mean
- Histogram median
- Histogram variance

Target classes:

| Label | Condition |
|------:|-----------|
| 1 | Normal |
| 2 | Suspect |
| 3 | Pathological |

---

## 📈 Model Evaluation

The models were evaluated using the following performance metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

These metrics were used to compare the performance of Decision Tree, Naive Bayes, and Random Forest in classifying fetal health conditions.

### Decision Tree

- Classification Report
- Confusion Matrix

### Naive Bayes

- Classification Report
- Confusion Matrix

### Random Forest

- Classification Report
- Confusion Matrix

---

## 🏆 Model Comparison

The experimental results show that **Random Forest** outperformed Decision Tree and Naive Bayes across all evaluation metrics.

Random Forest achieved higher **accuracy, precision, recall, and F1-score**, while producing fewer classification errors in the confusion matrix. Therefore, it was selected as the final prediction model for the application.

---

## 📷 Prediction Examples

The application predicts one of three fetal health conditions:

- ✅ Normal
- ⚠️ Suspect
- 🚨 Pathological

After users submit CTG parameters, the selected machine learning model processes the input and displays the predicted fetal health condition immediately.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/username/fetal-health-prediction.git
cd fetal-health-prediction
```

### 2. Create a virtual environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## 🎯 Project Objective

The objective of this project is to develop a web-based machine learning application capable of predicting fetal health conditions from Cardiotocography (CTG) data. By comparing multiple classification algorithms, the project aims to identify the most accurate model for supporting early fetal health assessment.

---

## 📄 License

This project was developed for educational purposes and portfolio demonstration.
