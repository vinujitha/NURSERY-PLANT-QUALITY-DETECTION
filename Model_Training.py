# Install the roboflow package to manage datasets 
!pip install roboflow 
 
# Import the necessary class from the roboflow package 
from roboflow import Roboflow 
# Initialize Roboflow with your API key 
rf = Roboflow(api_key="owo2nOPFFuy3OhMprQOl") 
# Access the specific workspace and project containing your dataset 
project = rf.workspace("plantleaves").project("plant-leaves-3m8t6") 
 
# Get the specific version of the dataset 
version = project.version(1) 
# Download the dataset for YOLOv5 
dataset = version.download("yolov5") 
# Clone the YOLOv5 repository from GitHub 
!git clone https://github.com/ultralytics/yolov5 
# Change the current working directory to the yolov5 directory 
%cd yolov5 
 
# Install the required dependencies for YOLOv5 
!pip install -qr requirements.txt 
# Edit the model parameters and train 
!python train.py --img-size 416 --batch-size 16 --epochs 100 --data '/content/plant-leaves
1/data.yaml' --cfg models/yolov5s.yaml --weights 'yolov5s.pt' 