from flask import Flask, request, jsonify
import base64
import io
from PIL import Image
import numpy as np
import torch
from transformers import AutoModel, AutoConfig
from model import DigitClassifierModel

app = Flask(__name__)
digit_model = DigitClassifierModel.from_pretrained("./model")


@app.route("/digit", methods=["POST"])
def receive_image():
    data = request.json

    if "image" not in data:
        return jsonify({"error": "No image data found"}), 400
    image_data = data["image"]

    image_bytes = base64.b64decode(image_data.split(",")[1])
    image = Image.open(io.BytesIO(image_bytes))
    image.save("./cache/received_image.png")

    processed_image = preprocess_image(image)
    processed_image = torch.Tensor([processed_image])
    result = digit_model(processed_image)
    result = torch.argmax(result)

    # Perform further processing with the image data
    return jsonify({"message": "Image received successfully", "result": result.item()})


def preprocess_image(image):
    image = image.resize((28, 28)).convert("L")
    image_array = np.array(image)
    image_array = image_array.astype("uint8")
    image_array = np.expand_dims(image_array, axis=0)
    return image_array
