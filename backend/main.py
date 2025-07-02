from flask import Flask, request, jsonify, send_from_directory
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import os, io

app = Flask(__name__, static_folder='static', static_url_path='')

model = load_model("/app/backend/model.keras")
CLASS_NAMES = ["akiec", "bcc", "bkl", "df", "mel", "nv", "vasc"]

@app.route("/")
def index():
    return app.send_static_file("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if 'file' not in request.files:
        return jsonify({"error": "No image provided"}), 400

    file = request.files['file']
    image = Image.open(io.BytesIO(file.read())).convert("RGB")
    image = image.resize((128, 128))
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

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000)) 
    app.run(host='0.0.0.0', port=port)
