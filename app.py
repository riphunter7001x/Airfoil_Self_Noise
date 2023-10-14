# importing libary
import pickle
import flask
import pandas as pd 
import numpy as np
from flask import Flask, request, jsonify, render_template
from flask import Response
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Enable CORS for your API
model = pickle.load(open("/app/model.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict_api",methods = ["POST"])
def predict_api():
    try:
        data = request.json["data"]

        # Create a DataFrame from the input data
        input_df = pd.DataFrame(data, index=[0])

        # Make predictions using the model
        predictions = model.predict(input_df)

        # Assuming model returns a single prediction, you can return it like this:
        output = predictions[0]

        # If  model returns multiple predictions, you can convert it to a list:
        # output = predictions.tolist()

        return jsonify(output)
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__=="__main__":
    app.run(debug=True)