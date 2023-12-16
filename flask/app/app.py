from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model

app = Flask(__name__)
model_path = 'model/trained_model.keras'
model = load_model(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        sequence = request.form['sequence']

        # Perform one-hot encoding and sequence reshaping
        reshaped_sequence = preprocess_sequence(sequence)

        # Predict using the model directly
        prediction = model.predict(reshaped_sequence)
        # Customize the output message based on the predicted probability
        if prediction >= 0.5:
            result_message = "Prediction: Enhancer Region (probability: {:.2%})".format(prediction[0, 0])
        else:
            result_message = "Prediction: Non-Enhancer Region (probability: {:.2%})".format(1 - prediction[0, 0])

        return render_template('index.html', prediction=prediction[0][0], prediction_message=result_message)

def preprocess_sequence(sequence):
    # Assuming sequence is the variable representing your input DNA sequence as a string
    # Convert the string to a list of characters
    sequence_list = list(sequence)

    # Function for one-hot encoding DNA sequences
    def one_hot_encoding(base):
        mapping = {'A': [1, 0, 0, 0], 'G': [0, 1, 0, 0], 'C': [0, 0, 1, 0], 'T': [0, 0, 0, 1]}
        return np.array(mapping[base])

    # Apply one-hot encoding to each character in the sequence
    reshaped_sequence = np.array([one_hot_encoding(base) for base in sequence_list])

    # Pad the sequence to have a length of 5500
    desired_length = 1375
    if len(reshaped_sequence) < desired_length:
        padding_size = desired_length - len(reshaped_sequence)
        padding = np.zeros((padding_size, 4))  # Assuming 4 is the number of features for each base
        reshaped_sequence = np.concatenate([reshaped_sequence, padding], axis=0)

    # Reshape the sequence to have a shape of (1, 5500)
    reshaped_sequence = reshaped_sequence.reshape(1, -1)

    return reshaped_sequence

if __name__ == '__main__':
    app.run(debug=True)
