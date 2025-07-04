from flask import Flask, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

frontend_path = os.path.join(os.path.dirname(__file__), '../frontend/dist')

app = Flask(__name__, static_folder=frontend_path, static_url_path='')

model = load_model("/app/backend/model.keras")
CLASS_NAMES = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    image = image.resize((256, 256))
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    preds = model.predict(image)[0]
    pred_class = CLASS_NAMES[np.argmax(preds)]
    confidence = float(np.max(preds))
    predictions_by_class = {
        class_name: float(prob)
        for class_name, prob in zip(CLASS_NAMES, preds)
    }

    return jsonify({
        "prediction": pred_class,
        "confidence": confidence,
        "predictions_by_class": predictions_by_class
    })
