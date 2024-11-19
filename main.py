
from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from ultralytics import YOLO
from PIL import Image
import json
import io

# Initialize YOLOv8 model
model_path = '/content/drive/MyDrive/best.pt'
model = YOLO(model_path)

# FastAPI app setup
app = FastAPI()

class PredictionResponse(BaseModel):
    predictions: list

@app.post("/predict", response_model=PredictionResponse)
async def predict(file: UploadFile = File(...)):
    # Load image from incoming file
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    # Perform inference
    results = model(img)

    # Process results
    predictions = []
    for box in results[0].boxes:
        predictions.append({
            "class": int(box.cls),  # Class ID
            "label": model.names[int(box.cls)],  # Class label
            "confidence": float(box.conf),  # Confidence score
            "bbox": [float(coord) for coord in box.xyxy[0]]  # Convert tensor to list of floats
        })

    # Return predictions
    return PredictionResponse(predictions=predictions)

    
