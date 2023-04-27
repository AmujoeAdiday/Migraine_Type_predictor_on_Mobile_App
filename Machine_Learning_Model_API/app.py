from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('extratree.pkl', 'rb'))

cors = CORS(app, resources={r"*": {"origins": "*"}})

@app.route('/', methods=['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'GET':
        return jsonify({'error':'method not allowed'}), 403

    elif request.method == "POST":
        data = request.get_json()
        input_values = [data['input_1'], data['input_2'], data['input_3'], data['input_4'], data['input_5'],
                    data['input_6'], data['input_7'], data['input_8'], data['input_9'], data['input_10'],
                    data['input_11'], data['input_12'], data['input_13'], data['input_14'], data['input_15'],
                    data['input_16'], data['input_17'], data['input_18']]



        input_array = np.array(input_values).reshape(1, -1)
        prediction = model.predict(input_array)[0]

    else:
        return jsonify({'error': 'invalid method'})

    return jsonify({'prediction': prediction})


if __name__ == '__main__':
    app.run()
