# coding: utf-8

import pandas as pd
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load dataset (used for dummy alignment)
df_1 = pd.read_csv("first_telc.csv")

# Clean TotalCharges if needed
df_1["TotalCharges"] = pd.to_numeric(df_1["TotalCharges"], errors="coerce")
df_1["TotalCharges"].fillna(0, inplace=True)

# Load model ONCE (better practice)
model = pickle.load(open("model.sav", "rb"))


@app.route("/")
def loadPage():
    return render_template("home.html", query="")


@app.route("/", methods=["POST"])
def predict():

    # Convert numeric inputs properly
    inputQuery1 = int(request.form["query1"])     # SeniorCitizen
    inputQuery2 = float(request.form["query2"])   # MonthlyCharges
    inputQuery3 = float(request.form["query3"])   # TotalCharges
    inputQuery4 = request.form["query4"]
    inputQuery5 = request.form["query5"]
    inputQuery6 = request.form["query6"]
    inputQuery7 = request.form["query7"]
    inputQuery8 = request.form["query8"]
    inputQuery9 = request.form["query9"]
    inputQuery10 = request.form["query10"]
    inputQuery11 = request.form["query11"]
    inputQuery12 = request.form["query12"]
    inputQuery13 = request.form["query13"]
    inputQuery14 = request.form["query14"]
    inputQuery15 = request.form["query15"]
    inputQuery16 = request.form["query16"]
    inputQuery17 = request.form["query17"]
    inputQuery18 = request.form["query18"]
    inputQuery19 = int(request.form["query19"])   # tenure

    # Create DataFrame for new user
    data = [[
        inputQuery1, inputQuery2, inputQuery3, inputQuery4,
        inputQuery5, inputQuery6, inputQuery7, inputQuery8,
        inputQuery9, inputQuery10, inputQuery11, inputQuery12,
        inputQuery13, inputQuery14, inputQuery15, inputQuery16,
        inputQuery17, inputQuery18, inputQuery19
    ]]

    new_df = pd.DataFrame(data, columns=[
        "SeniorCitizen", "MonthlyCharges", "TotalCharges", "gender",
        "Partner", "Dependents", "PhoneService", "MultipleLines",
        "InternetService", "OnlineSecurity", "OnlineBackup",
        "DeviceProtection", "TechSupport", "StreamingTV",
        "StreamingMovies", "Contract", "PaperlessBilling",
        "PaymentMethod", "tenure"
    ])

    # Combine with reference dataset
    df_2 = pd.concat([df_1, new_df], ignore_index=True)

    # Create tenure groups
    labels = ["{0} - {1}".format(i, i + 11) for i in range(1, 72, 12)]

    df_2["tenure_group"] = pd.cut(
        df_2["tenure"].astype(int),
        range(1, 80, 12),
        right=False,
        labels=labels
    )

    df_2.drop(columns=["tenure"], inplace=True)

    # One-hot encoding
    dummies = pd.get_dummies(df_2[[
        "gender", "SeniorCitizen", "Partner", "Dependents",
        "PhoneService", "MultipleLines", "InternetService",
        "OnlineSecurity", "OnlineBackup", "DeviceProtection",
        "TechSupport", "StreamingTV", "StreamingMovies",
        "Contract", "PaperlessBilling", "PaymentMethod",
        "tenure_group"
    ]])

    # Combine numeric + dummy columns
    final_df = pd.concat([
        df_2[["MonthlyCharges", "TotalCharges"]],
        dummies
    ], axis=1)

    # Align with model training columns
    final_df = final_df.reindex(columns=model.feature_names_in_, fill_value=0)

    user_row = final_df.tail(1)

    # Prediction
    prediction = model.predict(user_row)[0]
    probabilities = model.predict_proba(user_row)[0]

    # Correct confidence logic
    if prediction == 1:
        o1 = "⚠ This customer is likely to churn!"
        o2 = "Confidence: {:.2f}%".format(probabilities[1] * 100)
    else:
        o1 = "✅ This customer is likely to continue!"
        o2 = "Confidence: {:.2f}%".format(probabilities[0] * 100)

    return render_template(
        "home.html",
        output1=o1,
        output2=o2,
        query1=request.form["query1"],
        query2=request.form["query2"],
        query3=request.form["query3"],
        query4=request.form["query4"],
        query5=request.form["query5"],
        query6=request.form["query6"],
        query7=request.form["query7"],
        query8=request.form["query8"],
        query9=request.form["query9"],
        query10=request.form["query10"],
        query11=request.form["query11"],
        query12=request.form["query12"],
        query13=request.form["query13"],
        query14=request.form["query14"],
        query15=request.form["query15"],
        query16=request.form["query16"],
        query17=request.form["query17"],
        query18=request.form["query18"],
        query19=request.form["query19"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

