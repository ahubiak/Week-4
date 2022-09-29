import numpy as np
from flask import Flask, request,render_template
import pickle

import os 

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)
    output = 'unavailable'
    if prediction == 0:
        output = 'healthy'
    elif prediction == 1:
        output = 'sick'

    return render_template('index.html', prediction_text='Illness status is {}'.format(output))

# if __name__ == "__main__":
#     app.run(debug=True)


port = int(os.environ.get("PORT", 5000))
if __name__ == "__main__":
        app.run(host='0.0.0.0', port=port, debug=True)
