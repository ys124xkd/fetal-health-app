# 👶 Fetal Health Prediction App

Fetal Health Prediction App is a web-based application developed using **Python Flask** to predict fetal health conditions based on **Cardiotocography (CTG)** data. The application compares multiple machine learning algorithms to classify fetal health into **Normal**, **Suspect**, and **Pathological** conditions, helping support early fetal health assessment.

---

## 📖 Overview

Cardiotocography (CTG) is a medical technique used to monitor fetal well-being during pregnancy by recording fetal heart rate and uterine contractions.

This application allows users to input CTG parameters through a web interface. The entered data is processed using trained machine learning models to predict fetal health conditions. The project also compares several classification algorithms to determine the most accurate model for fetal health prediction.

---

## ✨ Features

- CTG data input through a web interface
- Automatic fetal health prediction
- Real-time prediction results
- Feature selection using **SelectKBest**
- Comparison of multiple machine learning algorithms
- Model performance evaluation
- Flask-based web application

---

## 🤖 Machine Learning Algorithms

The following classification algorithms were implemented and evaluated:

- Decision Tree
- Naive Bayes
- Random Forest

After comparing all models, **Random Forest** achieved the best overall performance and was selected as the final prediction model.

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
│   ├── classification_report_dt.png
│   ├── classification_report_nb.png
│   ├── classification_report_rf.png
│   ├── confusion_matrix_dt.png
│   ├── confusion_matrix_nb.png
│   ├── confusion_matrix_rf.png
│   ├── prediksi_normal.png
│   ├── prediksi_suspect.png
│   └── prediksi_pathological.png
│
├── data/
│   └── dataset.csv
│
├── templates/
│   ├── index.html
│   ├── dataset.html
│   ├── prediksi.html
│   └── profile.html
│
├── decision_tree_model.pkl
├── naive_bayes_model.pkl
├── random_forest_model.pkl
├── model_accuracies.pkl
├── rf_accuracy.pkl
├── selected_features.json
└── selected_features.pkl
```

---

## 📊 Dataset

This project uses the **Fetal Health Dataset**, which is based on **Cardiotocography (CTG)** recordings.

The dataset contains several clinical features, including:

- Baseline Value
- Accelerations
- Fetal Movement
- Uterine Contractions
- Light Decelerations
- Severe Decelerations
- Prolonged Decelerations
- Abnormal Short-Term Variability
- Mean Value of Short-Term Variability
- Percentage of Time with Abnormal Long-Term Variability
- Histogram Mean
- Histogram Median
- Histogram Variance

The target variable consists of three classes:

| Label | Condition |
|------:|-----------|
| 1 | Normal |
| 2 | Suspect |
| 3 | Pathological |

---

## 📈 Model Evaluation

The machine learning models were evaluated using the following performance metrics:

- Accuracy
- Precision
- Recall
- F1-Score
- Confusion Matrix

The evaluation results showed that **Random Forest** outperformed Decision Tree and Naive Bayes by achieving higher accuracy, precision, recall, and F1-score while producing fewer classification errors.

---

## 📸 Application Preview

### Home Page

![Home Page](assets/home.png)

### Prediction Page

![Prediction Page](assets/prediction.png)

### Prediction Result

![Prediction Result](assets/prediksi_normal.png)

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/username/fetal-health-prediction.git
cd fetal-health-prediction
```

### 2. (Optional) Create a virtual environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows**

```bash
venv\Scripts\activate
```

**macOS / Linux**

```bash
source venv/bin/activate
```

### 3. Install the required dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

Open your browser and navigate to:

```text
http://127.0.0.1:5000
```

---

## 🎯 Project Objective

The objective of this project is to develop a web-based machine learning application capable of predicting fetal health conditions using Cardiotocography (CTG) data. By comparing multiple classification algorithms, the project identifies the most effective model for supporting early fetal health assessment.

---

## 📄 License

This project was developed for educational purposes and portfolio demonstration.
