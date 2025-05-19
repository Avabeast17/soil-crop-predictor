#  Soil-Based Crop Recommender (ML + Streamlit)

##  Project Overview
This machine learning project helps farmers decide which crop to plant based on basic soil features like Nitrogen, Phosphorus, Potassium, and pH using a simple logistic regression model and a Streamlit web app.

##  Dataset
- `soil_measures.csv`: contains soil feature data and the optimal crop type.

##  Features
- Trains a model using logistic regression
- Identifies the best single soil feature for prediction
- Saves model as `crop_model.pkl`
- Interactive app to enter soil metrics and get a crop recommendation

##  Run the App
```bash
streamlit run app.py
