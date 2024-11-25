# Self-Driving Car System
This project uses YOLOv8 for object detection to build a self-driving car system. 
It achieves box(precision)82% in identifying objects on the road, such as vehicles, persons ,bikes and traffic signs.
## Features
- Object detection with YOLOv8 Large model.
- API for deploying the model in real-world scenarios.
## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/self_driving_car.git
   ```
2. Navigate to the project directory:
   ```bash
   cd self_driving_car
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   ## Dataset
The dataset consists of annotated images for training the YOLOv8 model. It includes categories such as vehicles, pedestrians,bikes and traffic signs.

[dataset link](https://app.roboflow.com/raneem-hussien-fkq0x/od-for-autonomous-vehicles/browse?queryText=&pageSize=50&startingIndex=0&browseQuery=true)

## Model Performance
- **box precision:** .828
- **Recall:** .788
- **mAP50:** .871
- **mAP50-95:** .625

  ## Contact
Created by [Mona Rashad](https://github.com/mona164) 

