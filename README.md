# 🏠 House Price Prediction – End-to-End Machine Learning Project

## 🌐 Live Demo

**Try the deployed application here:**

[🏠 House Price Prediction – Live App](https://ragapriya01--house-price-prediction-app-qutbji.streamlit.app/)

---

## 📌 Project Overview

This project is an end-to-end Machine Learning application that predicts house prices based on different property features.

It uses numerical and categorical data to estimate house prices through a trained Random Forest Regression model. The trained model is integrated into an interactive Streamlit web application, allowing users to enter property details and receive price predictions.

## 🎯 Problem Statement

To develop a Machine Learning model that predicts house prices based on property characteristics such as area, number of bedrooms, bathrooms, floors, year built, location, condition, and garage availability.

## 📊 Dataset Description

- **Total Records:** 2,000
- **Total Columns:** 10
- **Target Variable:** `Price`

### Features Used

| Feature | Description |
|---|---|
| Area | Size of the house |
| Bedrooms | Number of bedrooms |
| Bathrooms | Number of bathrooms |
| Floors | Number of floors |
| YearBuilt | Year the house was built |
| Location | Location of the property |
| Condition | Overall condition of the house |
| Garage | Garage availability |
| Price | Target variable to predict |

The `Id` column was excluded from model training.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit
- GitHub
- Streamlit Community Cloud

## ⚙️ Machine Learning Workflow

1. Dataset Collection
2. Data Understanding
3. Data Cleaning and Preprocessing
4. Exploratory Data Analysis (EDA)
5. Feature Selection
6. Train-Test Split
7. Numerical Feature Scaling
8. Categorical Feature Encoding
9. Random Forest Regression Model Training
10. Model Evaluation
11. Model Saving using Joblib
12. Web Application Development using Streamlit
13. Deployment using Streamlit Community Cloud

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Regressor

A Scikit-learn Pipeline was developed to combine preprocessing and model training.

### Pipeline Components

- **SimpleImputer:** Handles missing values.
- **StandardScaler:** Scales numerical features.
- **OneHotEncoder:** Converts categorical features into numerical format.
- **ColumnTransformer:** Applies different preprocessing techniques to numerical and categorical columns.
- **RandomForestRegressor:** Predicts house prices.

The complete trained pipeline was saved using Joblib as:

`house_price_pipeline.pkl`

## 🌐 Streamlit Web Application

An interactive web application was developed using Streamlit.

### Application Features

- User-friendly interface
- Input fields for house property details
- Numerical and categorical feature selection
- House price prediction
- Instant prediction results

Users can enter the property details and click the **Predict House Price** button to receive the estimated price.

## 🚀 How to Run the Project Locally

### 1. Clone the Repository

```bash
git clone https://github.com/Ragapriya01/-House-Price-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd -House-Price-Prediction
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit Application

```bash
streamlit run app.py
```

The application will open in your browser.

## 📁 Project Structure

```text
-House-Price-Prediction/
│
├── app.py
├── house_price_pipeline.pkl
├── House Price Prediction Dataset.csv
├── requirements.txt
└── README.md
```

## 📈 Project Outcome

Successfully developed and deployed an end-to-end Machine Learning application that predicts house prices using a Random Forest Regression model.

The project demonstrates practical implementation of data preprocessing, feature engineering, model training, pipeline creation, and web application deployment.

## 🔗 Project Links

- **GitHub Repository:** https://github.com/Ragapriya01/-House-Price-Prediction
- **Live Streamlit Application:** https://ragapriya01--house-price-prediction-app-qutbji.streamlit.app/

## 👩‍💻 Author

**Kalasikam Raga Priya**

Machine Learning | Data Science | Python | Data Analytics

---

⭐ If you find this project useful, feel free to explore the repository!
