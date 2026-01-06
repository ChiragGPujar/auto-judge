from feature_utils import text_features
import streamlit as st
import joblib
import pandas as pd


cls_model = joblib.load("difficulty_classifier.joblib")
reg_model = joblib.load("difficulty_regressor.joblib")

st.set_page_config(page_title="AutoJudge", layout="centered")
st.title("AutoJudge – Programming Problem Difficulty Predictor")

st.markdown(
    "Paste a programming problem description below to predict its **difficulty class** "
    "and **numerical difficulty score**."
)


desc = st.text_area("Problem Description")
inp = st.text_area("Input Description")
out = st.text_area("Output Description")


if st.button("Predict Difficulty"):
    if not desc.strip():
        st.warning("Please enter a problem description.")
    else:
        combined = desc + " " + inp + " " + out

        data = {
            "combined_text": [combined],
            "title": [""],
            "description": [desc],
            "input_description": [inp],
            "output_description": [out],
        }
        X_input = pd.DataFrame(data)

        pred_class = cls_model.predict(X_input)[0]
        pred_score = reg_model.predict(X_input)[0]

        st.success("Prediction Complete!")
        st.write("### Difficulty Class:", pred_class)
        st.write("### Difficulty Score:", round(float(pred_score), 2))
