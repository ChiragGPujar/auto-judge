# AutoJudge: Predicting Programming Problem Difficulty 

📌 Project Overview

AutoJudge is a machine learning–based system that automatically predicts the difficulty level of programming problems using only their textual descriptions. The system performs two tasks:

  1) Classification: Predicts the difficulty class
              
              → Easy / Medium / Hard

  2) Regression: Predicts a numerical difficulty score

The prediction is based solely on problem text (description, input, output), without using user submissions or platform statistics. A Streamlit web interface is provided for real-time inference on new problem statements.

⚙️ Installation & Setup

  1) Clone the Repository
     ``` bash
     git clone<repository-url>
     cd AutoJudge
  2) Install Dependencies
     ```python
     pip install pandas numpy scikit-learn joblib streamlit

Running the Project
Step 1 : Train the models (acm_classifier.ipynb)

This Step:

  1) Loads dataset
  2) Trains classification & regression models
  3) Evaluates performance
  4) Saves trained models

Step 2 : Launch Web Application

This web app loads the saved models and performs inference only

  ```bash
  streamlit run app.py
  ```

Web Interface Usage

  1) Paste:
     a) Problem Description
     b) Input Description
     c) Output Description

  2) Click Predict Difficulty
  3) View:
     a) Predicted Difficulty Class
     b) Predicted Difficulty Score

⚠️ Note:
The numerical difficulty score corresponds to the scale present in the training dataset and does not represent platform-specific ratings such as Codeforces scores.
