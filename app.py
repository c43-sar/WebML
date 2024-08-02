from flask import Flask, redirect, url_for, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
loaded_model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def index():
    return render_template("index.html")

def WeightPredictor(height):
    result = loaded_model.predict([[height]])
    return "Predicted Weight is " + str(result[0][0]) + "kg"

# Uncomment Lines To use HTML 

# def WeightPredictor_value(height):
#     result = loaded_model.predict([[height]])
#     return str(result[0][0])

@app.route("/results", methods=["POST"])
def output():
    if request.method == "POST":
        h = int(request.form['h'])
        # return render_template("result.html", height=h, weight=WeightPredictor_value(h))
        return WeightPredictor(h) # COMMENT THIS IF THE ABOVE LINE IS NOT COMMENTED

if __name__ == "__main__":
    app.run()