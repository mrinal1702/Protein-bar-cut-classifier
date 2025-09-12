# app.py
import joblib
import pandas as pd
import streamlit as st
from sklearn.pipeline import Pipeline

st.set_page_config(page_title="Protein Bar Cutting Classifier", page_icon="💪", layout="centered")
st.title("💪 Protein Bar Cutting Classifier")
st.write("Enter nutrition **per 100g**. The model predicts whether it’s cutting-friendly.")

@st.cache_resource
def load_model() -> Pipeline:
    return joblib.load("cutting_classifier.joblib")

pipe = load_model()

def build_row(kcal, protein, sugar, fiber, satfat):
    if kcal <= 0:
        st.error("Energy (kcal) must be > 0")
        st.stop()
    protein_per_100kcal = protein / (kcal / 100.0)
    return pd.DataFrame([{
        "energy-kcal_value": float(kcal),
        "protein_per_100kcal": float(protein_per_100kcal),
        "sugars_value": float(sugar),
        "fiber_value": float(fiber),
        "saturated-fat_value": float(satfat),
    }])

col1, col2 = st.columns(2)
with col1:
    kcal   = st.number_input("Energy (kcal / 100g)",  min_value=1.0,  max_value=1200.0, value=320.0, step=1.0)
    sugar  = st.number_input("Sugar (g / 100g)",      min_value=0.0,  max_value=100.0, value=3.0,   step=0.1)
    satfat = st.number_input("Saturated fat (g / 100g)", min_value=0.0,max_value=60.0,  value=2.0,   step=0.1)
with col2:
    protein= st.number_input("Protein (g / 100g)",    min_value=0.0,  max_value=100.0, value=30.0,  step=0.1)
    fiber  = st.number_input("Fiber (g / 100g)",      min_value=0.0,  max_value=60.0,  value=10.0,  step=0.1)

if st.button("Predict"):
    row = build_row(kcal, protein, sugar, fiber, satfat)
    prob = float(pipe.predict_proba(row)[0, 1])
    label = "✅ Cutting-friendly" if prob >= 0.5 else "❌ Not cutting-friendly"
    st.markdown(f"### {label}")
    st.caption(f"Probability of cutting-friendly: **{prob:.3f}**")
    st.dataframe(row.rename(columns={
        "energy-kcal_value":"kcal/100g", "protein_per_100kcal":"protein/100kcal",
        "sugars_value":"sugar g/100g", "fiber_value":"fiber g/100g", "saturated-fat_value":"sat fat g/100g"
    }))
