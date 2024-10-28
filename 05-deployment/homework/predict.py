import pickle
from flask import Flask, request, jsonify

app = Flask(__name__)

def load_model():
    with open('model2.bin', 'rb') as f_in:
        model = pickle.load(f_in)
    with open('dv.bin', 'rb') as f_in:
        dv = pickle.load(f_in)
    return dv, model

dv, model = load_model()

@app.route('/predict', methods=['POST'])
def predict():
    client = request.get_json()

    dv_client = dv.transform(client)
    y_pred = model.predict_proba(dv_client)[0, 1]
    result = {
        'y_pred': (y_pred)
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=6969)