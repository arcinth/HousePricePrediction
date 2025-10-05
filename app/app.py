import streamlit as st
import joblib
import numpy as np
import cloudpickle
import os


model_path = os.path.join(os.path.dirname(__file__), "../models/HPmodel.pkl")

# Verify file exists
if not os.path.exists(model_path):
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Load the model
with open(model_path, "rb") as f:
    model = cloudpickle.load(f)

print("Model loaded successfully!")


st.set_page_config(page_title="🏠 House Price Prediction", page_icon="💰", layout="centered")

st.markdown("<h1 style='text-align: center; color: #2E86C1;'>🏡 House Price Prediction (India)</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict your house price instantly using AI — simple, fast, and accurate!</p>", unsafe_allow_html=True)
st.divider()

st.markdown("### 📋 Enter House Details")

col1, col2 = st.columns(2)

with col1:
    bedrooms = st.number_input("🛏️ Number of Bedrooms", min_value=0, value=3, step=1)
    bathrooms = st.number_input("🛁 Number of Bathrooms", min_value=0, value=2, step=1)
    livingarea = st.number_input("🏡 Living Area (sq ft)", min_value=200, value=1200, step=100)

with col2:
    condition = st.slider("💎 Condition (1 = Poor, 5 = Excellent)", 1, 5, 3)
    grade = st.slider("🏗️ Grade of the House (1 = Low, 13 = Excellent)", 1, 13, 7)

st.divider()

if st.button("🔍 Predict Price", use_container_width=True):
    x = np.array([[bedrooms, bathrooms, livingarea, condition, grade]])
    prediction = model.predict(x)
    predicted_value = float(prediction[0])
    st.success(f"### 💰 Estimated House Price: ₹ {predicted_value:,.2f}")
    
else:
    st.info("👆 Fill in the details above and click **Predict Price** to get your estimated house value.")

st.divider()
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ using Streamlit & Machine Learning<br>Credits: <b>Arcinth Siva</b></p>",
    unsafe_allow_html=True
)
