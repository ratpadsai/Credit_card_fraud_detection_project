import streamlit as st
import numpy as np
import pickle
loaded_model = pickle.load(open('trained_model.sav','rb'))
st.title("💳 Credit Card Fraud Detection App")

st.write("Enter transaction details below:")

# Example: Assuming 30 features like in the Kaggle dataset
features = []
for i in range(30):  # Replace 30 with actual number of features your model expects
    val = st.number_input(f"Feature {i+1}", min_value=0.0, step=0.1)
    features.append(val)

if st.button("Detect Fraud"):
    input_data = np.array([features])
    prediction = loaded_model.predict(input_data)
    result = "🚨 Fraudulent" if prediction[0] == 1 else "✅ Legitimate"
    st.success(f"Prediction: {result}")