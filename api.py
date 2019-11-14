# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 08:34:06 2019

@author: Julie.Vranken
"""

from flask import Flask, request, jsonify
from pandas.io.json import json_normalize
import pickle
 
# Create an instance of the Flask class.
app = Flask(__name__)
 
# Define which URL should trigger the predict function.
@app.route('/api/predictions', methods=['POST'])
 
# Define the predict function.
def predict():
    # DATA
    # Get the data from the POST request.
    data = request.get_json()
 
    # PREDICTION
    # Make a prediction.
    prediction = model.predict(json_normalize(data)[['Experience', 'Education']])
 
    # OUTPUT
    # Create the prediction output.
    output = {'prediction': prediction[0]}
 
    # RETURN
    # Return a json file containing the prediction output.
    return jsonify(output)
 
if __name__ == '__main__':
    # The model is loaded when the API is launched.
    model = pickle.load(open('model', 'rb'))
    app.run(host='0.0.0.0', port=2019, debug=False)