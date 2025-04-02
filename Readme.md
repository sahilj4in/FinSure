# LoanEase - Loan Approval Prediction

## 🚀 Project Overview
LoanEase is a **machine learning-based loan approval prediction system** that helps assess whether a loan applicant is likely to be approved or rejected. Using a trained **Random Forest model**, the system predicts loan eligibility based on key financial and demographic factors such as income, credit history, and employment status.

## 🛠️ Technologies Used
- **Python (Flask)** - Backend web framework
- **Scikit-Learn** - Machine learning model training
- **Pandas & NumPy** - Data preprocessing
- **Joblib** - Model serialization
- **Bootstrap (HTML/CSS)** - Frontend for user-friendly form

## 🔍 How It Works
1. The user fills out a **loan application form** on the website.
2. The system processes the input data and applies **data preprocessing** (handling missing values, encoding categorical variables, etc.).
3. A **pre-trained Random Forest model** predicts the loan approval outcome.
4. The result is displayed as either **Approved ✅** or **Not Approved ❌** along with a confidence score.

## 📂 Project Structure
```
LoanEase/
│── static/              # CSS, JS, Images
│── templates/           # HTML templates
│   ├── index.html       # User input form
│── model/               # Trained ML model
│   ├── loan_model.pkl   # Serialized Random Forest model
│   ├── label_encoder.pkl
│   ├── imputer.pkl
│── app.py               # Flask application
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## 📌 Installation & Setup
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/LoanEase.git
cd LoanEase
```

### 2️⃣ Create a Virtual Environment (Optional but Recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Run the Flask Application
```sh
python app.py
```
Access the web app at **http://127.0.0.1:5000/**.

## 📊 Model Training (Optional)
If you want to retrain the model:
1. Load the dataset (`loan.csv`).
2. Preprocess data (handle missing values, encode categorical features).
3. Train a **Random Forest Classifier**.
4. Save the model using `joblib.dump()`.

## 🎯 Use Cases
- **Banks & Financial Institutions**: Automated loan eligibility screening.
- **Individuals**: Check loan approval chances before applying.
- **Educational Purposes**: Understanding ML model deployment with Flask.

## 👨‍💻 Contributors
- [Sahil Jain](https://github.com/sahilj4in)

---
Let me know if you need any modifications! 🚀

