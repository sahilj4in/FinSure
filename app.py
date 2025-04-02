from flask import Flask, render_template, request
import pandas as pd
import joblib
import json

app = Flask(__name__)

# Load trained model & preprocessors
rf_model = joblib.load("loan_model.pkl")
imputer = joblib.load("imputer.pkl")

# Load label encodings
with open("label_mappings.json", "r") as f:
    label_mappings = json.load(f)

# Define feature columns
categorical_cols = ["Gender", "Married", "Dependents", "Education", 
                    "Self_Employed", "Property_Area"]
numerical_cols = ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", 
                  "Loan_Amount_Term", "Credit_History"]

# Prediction function
def predict_loan_approval(new_data):
    new_data = pd.DataFrame([new_data])

    # Encode categorical features
    for col in categorical_cols:
        if col in new_data.columns:
            new_data[col] = new_data[col].fillna("Unknown")
            new_data[col] = new_data[col].map(lambda x: label_mappings[col].get(x, -1))  # Default -1 for unseen labels
    
    # Process numerical features
    new_data[numerical_cols] = imputer.transform(new_data[numerical_cols])
    
    # Make prediction
    prediction = rf_model.predict(new_data)
    
    return "Approved ✅" if prediction[0] == 1 else "Not Approved ❌"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = request.form.to_dict()

        # Convert numerical values
        for key in ["ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", "Credit_History"]:
            data[key] = float(data[key]) if data[key] else 0

        result = predict_loan_approval(data)
        return render_template("index.html", prediction=result)  # Show result in the page

    return render_template("index.html", prediction=None)

if __name__ == "__main__":
    app.run(debug=True)
