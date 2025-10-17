import json
import os
import torch
from torchvision.models.detection import fasterrcnn_resnet50_fpn_v2, FasterRCNN_ResNet50_FPN_V2_Weights
import requests
from flask import Flask, request, jsonify
from PIL import Image
from prometheus_flask_exporter import PrometheusMetrics
from prometheus_client import Counter

app = Flask(__name__, static_url_path="")
metrics = PrometheusMetrics(app)

print("started server")
weights = FasterRCNN_ResNet50_FPN_V2_Weights.DEFAULT
model = fasterrcnn_resnet50_fpn_v2(weights=weights, box_score_thresh=0.9)
model.eval()
preprocess = weights.transforms()

print("Loaded model")

@app.route("/predict", methods=['POST'])
@metrics.counter("app_http_inference_count", "number of http requests")
def predict():
    data = request.get_json(force=True)
    img = Image.open(requests.get(data["url"], stream=True).raw)
    batch = [preprocess(img)]
    prediction = model(batch)[0]
    labels = [weights.meta["categories"][i] for i in prediction["labels"]]

    return jsonify({
        "objects": labels
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
