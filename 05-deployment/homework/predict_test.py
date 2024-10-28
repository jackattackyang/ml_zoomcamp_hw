import pickle

with open('model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)
with open('dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)

client = {"job": "management", "duration": 400, "poutcome": "success"}
dv_client = dv.transform(client)
y_pred = model.predict_proba(dv_client)[0, 1]

print(y_pred)