# 🏠 House Price Prediction – Machine Learning Project

## 📌 Project Overview
This project predicts house prices based on various property features using Machine Learning. It uses numerical and categorical data to estimate the price of a house.

## 🎯 Problem Statement
To develop a Machine Learning model that predicts house prices based on property characteristics such as area, bedrooms, bathrooms, floors, year built, location, condition, and garage availability.

## 📊 Dataset Description
- Total Records: 2,000
- Total Columns: 10
- Target Variable: `Price`

### Features
- Area
- Bedrooms
- Bathrooms
- Floors
- YearBuilt
- Location
- Condition
- Garage

## 🛠️ Technologies Used
- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- Joblib
- Streamlit

## ⚙️ Machine Learning Workflow
1. Data Collection
2. Data Cleaning and Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Selection
5. Train-Test Split
6. Numerical Feature Scaling
7. Categorical Feature Encoding
8. Random Forest Regression Model
9. Model Evaluation
10. Model Deployment using Streamlit

## 🤖 Machine Learning Model
**Algorithm:** Random Forest Regressor

A Scikit-learn Pipeline was created using:
- SimpleImputer
- StandardScaler
- OneHotEncoder
- ColumnTransformer
- RandomForestRegressor

The trained pipeline was saved using Joblib as `house_price_pipeline.pkl`.

## 🌐 Streamlit Application
The project includes a Streamlit web application where users can enter house details and receive a predicted house price.

## 🚀 How to Run the Project Locally

1. Clone the repository:

   ```bash
   git clone YOUR_GITHUB_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd House-Price-Prediction
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit application:

   ```bash
   streamlit run app.py
   ```

## 📁 Project Structure

```text
House-Price-Prediction/
│
├── app.py
├── house_price_pipeline.pkl
├── requirements.txt
└── README.md
```

## 👩‍💻 Project Outcome
Developed an end-to-end Machine Learning application that predicts house prices and makes the trained model accessible through a user-friendly Streamlit interface.
