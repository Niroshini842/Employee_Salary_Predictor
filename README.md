# Employee_Salary_Predictor
# 💼 Employee Salary Classification using Machine Learning

An end-to-end machine learning project that classifies whether an employee earns **>50K or <=50K** annually based on various demographic and job-related features. The model is deployed using **Flask** with a stylish, responsive web UI built using **Tailwind CSS**.

---

## 📌 Table of Contents

- [Problem Statement](#-problem-statement)
- [Tech Stack](#-tech-stack)
- [Features](#-features)
- [Model](#-model)
- [Demo](#-demo)
- [How to Run](#-how-to-run)
- [Future Scope](#-future-scope)
- [License](#-license)

---

## ❓ Problem Statement

Organizations often need to analyze employee income distribution for planning, recruitment, and policy decisions. Manual prediction is error-prone and biased.

This project aims to:
- Predict if an employee earns >50K or ≤50K
- Use demographic and employment features for classification
- Provide an interactive, user-friendly interface for HR and analysts

---

## 🛠 Tech Stack

- **Languages**: Python, HTML, CSS, JavaScript
- **Libraries**: 
  - pandas, numpy
  - scikit-learn
  - XGBoost
  - joblib
- **Framework**: Flask (for backend and deployment)
- **Styling**: Tailwind CSS
- **UI Tools**: Jinja2 templates

---

## ✨ Features

- Predict employee salary range based on input form
- Dark/Light mode toggle 🌙☀️
- Tooltips and animated form entry
- Responsive UI (mobile and desktop)
- Input validation and form reset functionality
- Salary result shown with styling and indicators
- Clean backend with error handling

---

## ⚙️ Model

- Dataset: [UCI Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- Preprocessing:
  - Label encoding for education
  - One-hot encoding for categorical variables
  - Capital gain/loss and work hours considered
- Algorithms Tried: Logistic Regression, Random Forest, XGBoost
- Final Model: **XGBoost** (Accuracy ~87%)

---

## 🎥 Demo

You can try the live version here (if hosted):  
🔗 `https://your-render-url.com`


---

## ▶️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/employee-salary-classification.git
cd employee-salary-classification
