import os
import json
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np
import tensorflow as tf
from flask_cors import CORS

TF_ENABLE_ONEDNN_OPTS = 0

app = Flask(__name__)
CORS(app)

# Load the pre-trained CNN model
working_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(working_dir, 'detection_model.h5')
cnn_model = tf.keras.models.load_model(model_path)

# Load class indices and disease information from JSON files
class_indices = json.load(open(os.path.join(working_dir, 'class_indices.json')))
disease_info_path = os.path.join(working_dir, 'doc.json')

# Load the disease descriptions into a dictionary
with open(disease_info_path, 'r', encoding='utf-8') as file:
    disease_descriptions = json.load(file)

# Load and preprocess the image
def load_and_preprocess_image(image):
    target_size = (224, 224)
    img = Image.open(image)
    img = img.resize(target_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array.astype('float32') / 255.
    return img_array

# Fetch disease information from the local JSON file
def get_disease_info(disease_name):
    return disease_descriptions.get(disease_name, "No description available for this disease.")

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400

    image = request.files['image']
    preprocessed_img = load_and_preprocess_image(image)
    predictions = cnn_model.predict(preprocessed_img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    predicted_class_name = class_indices.get(str(predicted_class_index), "Unknown")

    return jsonify({
        'prediction': predicted_class_name
    })

@app.route('/description', methods=['POST'])
def description():
    data = request.get_json()
    disease_name = data.get('prediction')
    if disease_name:
        disease_info = get_disease_info(disease_name)
        return jsonify({'description': disease_info})
    else:
        return jsonify({'error': 'Prediction not provided'}), 400

if __name__ == '__main__':
    app.run(debug=True)
