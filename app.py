
# Import libraries
import streamlit as st
import pandas as pd
import joblib

# Page configuration (must come first)
st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Load trained ML pipeline
model = joblib.load('house_price_pipeline.pkl')

# Application title
st.title("🏠 House Price Prediction")
st.write("Enter the house details below to predict its price.")

st.divider()

# Input fields
area = st.number_input(
    "Area (sq. ft.)",
    min_value=501,
    max_value=4999,
    value=2000
)

bedrooms = st.selectbox("Bedrooms", [1, 2, 3, 4, 5])
bathrooms = st.selectbox("Bathrooms", [1, 2, 3, 4])
floors = st.selectbox("Floors", [1, 2, 3])

year_built = st.number_input(
    "Year Built",
    min_value=1900,
    max_value=2026,
    value=2000
)

location = st.selectbox(
    "Location",
    ["Downtown", "Suburb", "Urban", "Rural"]
)

condition = st.selectbox(
    "Condition",
    ["Poor", "Fair", "Good", "Excellent"]
)

garage = st.selectbox("Garage", ["Yes", "No"])

# Prediction button
if st.button("Predict House Price"):

    input_data = pd.DataFrame({
        'Area': [area],
        'Bedrooms': [bedrooms],
        'Bathrooms': [bathrooms],
        'Floors': [floors],
        'YearBuilt': [year_built],
        'Location': [location],
        'Condition': [condition],
        'Garage': [garage]
    })

    prediction = model.predict(input_data)

    st.success(
        f"Predicted House Price: {prediction[0]:,.2f}"
    )
