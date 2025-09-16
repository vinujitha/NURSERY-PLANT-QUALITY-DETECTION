import RPi.GPIO as GPIO 
import time 
import cv2 
import threading 
import tkinter as tk 
from PIL import Image, ImageTk 
from roboflow import Roboflow 
import matplotlib.pyplot as plt 
 
# Initialize the Roboflow model 
api_key = "owo2nOPFFuy3OhMprQOl" 
workspace = "plantleaves" 
project_name = "plant-leaves-3m8t6" 
version_number = "1" 
rf = Roboflow(api_key=api_key) 
project = rf.workspace(workspace).project(project_name) 
model = project.version(version_number, local="http://localhost:9001/").model 
 
# Initialize GPIO 
GPIO.setmode(GPIO.BCM) 
TRIG = 23 
ECHO = 24 
GPIO.setup(TRIG, GPIO.OUT) 
GPIO.setup(ECHO, GPIO.IN) 
print("Distance Measurement in Progress") 
 
# Function to run in the thread 
def capture_and_predict(): 
    while True: 
        # Trigger the ultrasonic burst 
        GPIO.output(TRIG, True) 
        time.sleep(0.00001) 
        GPIO.output(TRIG, False) 
         
        # Measure the return pulse 
        while GPIO.input(ECHO) == 0: 
            pulse_start = time.time() 
         
        while GPIO.input(ECHO) == 1: 
            pulse_end = time.time() 
         
 
        pulse_duration = pulse_end - pulse_start 
        distance = pulse_duration * 17150 
        distance = round(distance, 2) 
        print("Distance:", distance, "cm") 
        # Check if an object is detected within 15cm 
        if distance < 25: 
            # Capture an image 
            time.sleep(3) 
            cap = cv2.VideoCapture(0)  # Use the correct camera index 
            ret, frame = cap.read() 
            image_path = '/home/pi/Documents/projects/image_cap.jpg' 
            if ret: 
                # Save the image 
                cv2.imwrite(image_path, frame) 
                print("Image captured successfully") 
                 
                # Make a prediction 
                prediction = model.predict(image_path, confidence=40, overlap=30) 
                print(prediction.json()) 
                 
                # Save the prediction result image 
                prediction.save('/home/pi/Documents/projects/result.png') 
                 
                # Update the GUI with the prediction plot 
                root.after(0, update_gui_with_plot, '/home/pi/Documents/projects/result.png') 
                 
                # Delay before capturing the next image 
                time.sleep(10) 
                 
        time.sleep(2)  # Delay before the next check 
def update_gui_with_plot(plot_path): 
    # Load and display the plot image 
 
    plot_img = Image.open(plot_path) 
    plot_img = plot_img.resize((500, 300), Image.LANCZOS)  # Resize to fit the GUI 
    plot_img = ImageTk.PhotoImage(plot_img) 
    plot_label.configure(image=plot_img) 
    plot_label.image = plot_img  # Keep a reference! 
# Setup Tkinter window 
root = tk.Tk() 
root.geometry("1024x600")  # Set the window to full resolution 
root.title("Prediction Results") 
# Plot display 
plot_label = tk.Label(root) 
plot_label.pack(side="top", fill="both", expand="yes") 
# Start the capture and predict thread 
thread = threading.Thread(target=capture_and_predict) 
thread.daemon = True 
thread.start() 
root.mainloop() 
# Cleanup GPIO resources 
GPIO.cleanup()