from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained pipeline model
try:
    model = joblib.load("model1.pkl")
except Exception as e:
    model = None
    print(f"Model loading error: {e}")

# Education to numeric mapping 
education_mapping = {
    "Bachelors": 13,
    "Masters": 14,
    "HS-grad": 9,
    "Some-college": 10,
    "Doctorate": 16,
    "Assoc-acdm": 12,
    "Assoc-voc": 11,
    "Prof-school": 15
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if not model:
        return render_template("predict.html", prediction_text="Model not loaded. Please check your model file.")

    try:
        # Fetch form values
        age = int(request.form.get("age", 0))
        gender = request.form.get("gender", "Male")
        education_str = request.form.get("education", "HS-grad")
        workclass = request.form.get("workclass", "Private")
        hours = int(request.form.get("hours", 40))
        occupation = request.form.get("occupation", "Prof-specialty")
        marital = request.form.get("marital", "Never-married")
        country = request.form.get("country", "United-States")
        relationship = request.form.get("relationship", "Not-in-family")
        race = request.form.get("race", "White")
        gain = int(request.form.get("gain", 0))
        loss = int(request.form.get("loss", 0))

        education_num = education_mapping.get(education_str, 0)

        # Create DataFrame
        input_df = pd.DataFrame([{
            "age": age,
            "workclass": workclass,
            "native-country": country,
            "hours-per-week": hours,
            "capital-gain": gain,
            "capital-loss": loss,
            "gender": gender,
            "education-num": education_num,
            "occupation": occupation,
            "marital-status": marital,
            "relationship": relationship,
            "race": race,
            "fnlwgt": 100000,  # Default value
            "educational-num": education_num,
        }
    ]
)

        # Predict
        prediction = model.predict(input_df)[0]
        result = ">50K" if prediction == 1 else "<=50K"

        return render_template("predict.html", prediction_text=f"Predicted Income: {result}")

    except Exception as e:
        return render_template("predict.html", prediction_text=f"Prediction Error: {str(e)}")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)

