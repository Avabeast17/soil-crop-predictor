import streamlit as st
import pickle

st.title("🌾 Soil-Based Crop Recommender")

n = st.number_input("Nitrogen", min_value=0)
p = st.number_input("Phosphorus", min_value=0)
k = st.number_input("Potassium", min_value=0)
ph = st.number_input("pH", min_value=0.0, format="%.2f")

if st.button("Predict Crop"):
    # Replace with your actual trained model path
    model = pickle.load(open("crop_model.pkl", "rb"))
    prediction = model.predict([[n, p, k, ph]])
    st.success(f"Recommended Crop: {prediction[0]}")
