# 🧠 Mental Health Chat Classifier

A machine learning-powered web app that classifies user-submitted chat messages into mental health categories such as **Normal**, **Anxious**, **Depressed**, etc. Built using **Streamlit** for the frontend and **Scikit-learn** with **TF-IDF** for classification.

![Mental Health Classifier](https://img.shields.io/badge/Streamlit-Enabled-green?style=flat-square&logo=streamlit)  
![License](https://img.shields.io/badge/license-MIT-blue.svg)  
![Made with ❤️](https://img.shields.io/badge/made%20with-%E2%9D%A4-red)

---

## 🚀 Features

- 🧠 Predicts mental health status from text input
- 📊 Uses TF-IDF + ML model (e.g., Logistic Regression / SVM)
- 🎨 Beautiful Streamlit UI with custom styling
- 🔒 Optional Firebase backend for logging
- 🔍 Modular and beginner-friendly code

---

## 📦 Tech Stack

| Component     | Technology          |
|---------------|---------------------|
| Frontend UI   | Streamlit           |
| ML Model      | Scikit-learn        |
| Text Vectorization | TF-IDF         |
| Deployment    | Streamlit Cloud / Localhost |
| Backend (optional) | FastAPI or Firebase |

---

## 📁 Directory Structure

```
📦 mental-health-chat-classifier/
├── streamlit_app.py # Main Streamlit app
├── mental_health_classifier.pkl # Trained ML model (not uploaded)
├── tfidf_vectorizer.pkl # TF-IDF vectorizer (not uploaded)
├── cleaned_data.csv # Cleaned sample data (optional)
├── .gitignore
└── README.md

```


---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/mental-health-chat-classifier.git
cd mental-health-chat-classifier
```


## 📊 Model Info
Vectorizer: TF-IDF with max_features=5000

Classifier: Logistic Regression (or SVM)

Data: Mental health-related chat messages (anonymized & preprocessed)

Note: .pkl files are excluded from this repo due to size. You can train your own or contact the maintainer.