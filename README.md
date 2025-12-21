

# Fire Weather Index (FWI) Prediction AI

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-black?style=for-the-badge&logo=flask&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

> **A production-ready Machine Learning application for real-time forest fire risk assessment.**

This system leverages Ridge Regression and a standardized data pipeline to predict the **Fire Weather Index (FWI)** with high precision. Designed with a modular architecture, it serves predictions via a RESTful Flask interface, wrapped in a modern, responsive UI.

---

## ⚡ Key Features

* **Precision Modeling:** Trained on the **Algerian Forest Fires dataset** with optimized feature selection and hyperparameter tuning.
* **Enterprise UI/UX:** A clean, "Glassmorphism" design system ensuring readability and responsiveness across devices.
* **Robust Pipeline:** Automated `sklearn` pipeline handling scaling (`StandardScaler`) and inference in a single serialized object.
* **Production Ready:** Lightweight, container-friendly structure suitable for deployment on AWS Elastic Beanstalk, Render, or Azure App Service.

## 🛠️ Technical Architecture

| Component | Technology |
| :--- | :--- |
| **Core Logic** | Python 3.9+, NumPy, Pandas |
| **Machine Learning** | Scikit-Learn (Ridge Regression, LassoCV) |
| **Serialization** | Joblib (Optimized for NumPy arrays) |
| **Web Framework** | Flask (Jinja2 Templating) |
| **Frontend** | HTML5, CSS3, Flexbox/Grid System |

## 🚀 Quick Start Guide

### Prerequisites
* Python 3.8 or higher
* Git

### 1. Installation

```bash
# Clone the repository
git clone [https://github.com/YOUR_USERNAME/fwi-prediction-app.git](https://github.com/YOUR_USERNAME/fwi-prediction-app.git)

# Navigate to project directory
cd fwi-prediction-app

# Create virtual environment
python -m venv venv

# Activate environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

```

### 2. Running the Application

```bash
python application.py

```

*The server will initialize at `http://127.0.0.1:8000*`

## 🧪 Testing the Model

Use the web interface to test different environmental scenarios:

| Scenario | Temperature | Humidity | Rain | Prediction (FWI) | Status |
| --- | --- | --- | --- | --- | --- |
| **Safe Day** | 22°C | 85% | 2.5mm | **~0.3** | ✅ Low Risk |
| **Danger Day** | 35°C | 30% | 0.0mm | **~18.6** | ⚠️ High Danger |

## 📂 Repository Structure

```text
├── application.py       # Application entry point & route logic
├── requirements.txt     # Dependency definition
├── models/
│   └── model.pkl        # Serialized Model Pipeline
├── templates/
│   ├── index.html       # Landing/Welcome page
│   └── home.html        # Main prediction interface
├── data_set/
│   └── forest_fire.csv  # Training dataset source
└── README.md            # Documentation

```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/NewFeature`).
3. Commit your changes (`git commit -m 'Add NewFeature'`).
4. Push to the branch (`git push origin feature/NewFeature`).
5. Open a **Pull Request**.


*Developed by [Mihir Maru]*


