# Nursery Plant Quality Detection System 🌱

This project focuses on developing an **automated disease detection system for Nai-chili plants**
using **deep learning (YOLOv5)** and **computer vision techniques**. The system integrates an 
**automated conveyor belt with sensors** to enable real-time monitoring of nursery plants, aiming to 
reduce manual labor costs and improve accuracy in disease identification.

## 🚀 Project Overview
- **Objective**: Detect and classify plant diseases (healthy, yellow leaves, and curl leaves) in Nai-chili plants.
- **Technologies Used**: Python, YOLOv5, PyTorch, OpenCV, Roboflow, Raspberry Pi 4B, Arduino Mega 2560.
- **Automation**: Integrated with a conveyor belt system controlled by stepper motors and sensors for positioning plants.
- **Outcome**: Achieved reliable classification of diseases with real-time predictions on embedded hardware.

## 🛠 Features
- Automated **image acquisition** using webcam + conveyor system.
- **Deep learning-based detection** of plant leaf diseases using YOLOv5.
- **Real-time monitoring** and predictions displayed on a 7-inch screen via Raspberry Pi.
- Cloud-based model prediction using **Roboflow API** for optimized performance.
- Cost-effective solution for reducing manual inspection in agriculture.

## 📂 Project Structure
- `data/` → Collected dataset of healthy and diseased plant images (annotated using Roboflow).
- `training/` → YOLOv5 model training scripts and configurations.
- `automation/` → Arduino code for conveyor system and motor control.
- `prediction/` → Raspberry Pi Python scripts for real-time detection and display.

## 🔧 Hardware Components
- Raspberry Pi 4 Model B  
- Arduino Mega 2560 + CNC Shield V3  
- Stepper Motor (NEMA17) + DRV8825 Driver  
- Ultrasonic Sensors  
- Full HD Webcam  
- 7-Inch Waveshare Display  

## 📊 Results
- Successfully detected **3 plant conditions**: Healthy, Yellow Leaves, Curl Leaves.
- Integrated hardware + AI for **real-time disease classification**.  
- Demonstrated **scalable potential** for agricultural automation.  

## 🌍 Impact
This project provides a **cost-effective and sustainable solution** to reduce farmers' dependency on 
manual inspections. By leveraging AI and automation, it helps improve agricultural productivity 
and supports the adoption of smart farming practices.

## 📖 Future Work
- Expanding the dataset for higher accuracy across diverse environments.
- Implementing a more powerful edge device for faster predictions.
- Developing a user-friendly mobile app for remote monitoring.
- Scaling system for large-scale agricultural use.  

---
👨‍💻 **Author**: Vinujitha Pindenya  
📧 Email: thisen1vinujitha@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/vinujitha/)  
