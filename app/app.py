import streamlit as st
from predict import predict_risk

st.title("Liver Cirrhosis Predictor")

inputs = {
    "Age": st.slider("Age", 10, 90, 45),
    "Gender": st.selectbox("Gender", ["Male", "Female"]),
    "Total_Bilirubin": st.number_input("Total Bilirubin", 0.1, 30.0),
    "Direct_Bilirubin": st.number_input("Direct Bilirubin", 0.1, 10.0),
    "Alkaline_Phosphotase": st.number_input("Alkaline Phosphotase", 50, 2000),
    "SGPT": st.number_input("SGPT", 0, 2000),
    "SGOT": st.number_input("SGOT", 0, 2000),
    "Total_Proteins": st.number_input("Total Proteins", 1.0, 10.0),
    "Albumin": st.number_input("Albumin", 1.0, 6.0),
    "A/G_Ratio": st.number_input("A/G Ratio", 0.1, 3.0)
}

if st.button("Predict"):
    input_data = list(inputs.values())
    input_data[1] = 1 if inputs["Gender"] == "Male" else 0  # Gender encoding
    result = predict_risk(input_data)
    if result == 1:
        st.error("⚠️ High risk of Liver Cirrhosis")
    else:
        st.success("✅ Low risk of Liver Cirrhosis")
