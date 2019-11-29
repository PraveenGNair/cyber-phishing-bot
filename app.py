# Purpose - Receive the call for testing a page from the Chrome extension and return the result (SAFE/PHISHING)
# for display. This file calls all the different components of the project (The ML model, features_extraction) and
# consolidates the result.

import joblib
import features_extraction
import sys
import numpy as np
from flask import Flask, request, abort, jsonify, Response
import settings
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
import io
import os

from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME

app = Flask(__name__)
# Load config settings
app.config.from_object('app.settings')

def get_prediction_from_url(test_url,html):
    features_test = features_extraction.main(test_url,html)
    # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    features_test = np.array(features_test).reshape((1, -1))
    path = os.path.abspath('classifier/random_forest.pkl')
    clf = joblib.load(path)

    pred = clf.predict(features_test)
    return int(pred[0])

@app.route('/predictPhish', methods=['POST'])
def predict():
    request_json=request.form.to_dict()
    url = request_json.get('url')
    html = request_json.get('html')

    prediction = get_prediction_from_url(url,html)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if prediction == 1:
        # print "The website is safe to browse"
        return("SAFE")
    elif prediction == -1:
        # print "The website has phishing features. DO NOT VISIT!"
        return ("PHISHING")
        # print 'Error -', features_test


if __name__ == '__main__':
    application = DispatcherMiddleware(app, {
        app.config['APPLICATION_ROOT']: app,
    })
    run_simple('0.0.0.0', 8080, application, use_reloader=False)
