from operator import truediv
from pyexpat import model
from tkinter import Button
import cv2
import numpy as np
from gui_buttons import Buttons

# intialise buttons 
button = Buttons()
button.add_button("cell phone",20,100)
button.add_button("person",20,180)
button.add_button("remote",20,260)
button.add_button("scissors",20,340)

colors = button.colors

# OpenCv DNN

net = cv2.dnn.readNet("J:\Python large projects\object detection software\dnn_model\yolov4-tiny.cfg","J:\Python large projects\object detection software\dnn_model\yolov4-tiny.weights")
model = cv2.dnn_DetectionModel(net)
model.setInputParams(size=(416,416), scale=1/255)


# Load classes lists
classes = []
with open("J:\Python large projects\object detection software\dnn_model\classes.txt", "r") as file_object:
    for class_name in file_object.readlines():
        class_name = class_name.strip()
        classes.append(class_name)

print("object list")
print(classes)



#intialise camera
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,600)
#Full HD 1920*1080

def click_button(event,x,y,flags,params):
    global button_person
    if event == cv2.EVENT_LBUTTONUP:
        button.button_click(x,y)
        print(x,y)
       

#create window
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",click_button)
while True:
    # Get frames
    ret,frame = cap.read()
    
    #get active button list
    active_buttons = button.active_buttons_list()
    print("active buttons", active_buttons)
    
    
    # object detection
    (class_ids , score ,bboxes) = model.detect(frame)
    for class_id, score,bbox, in zip(class_ids,score,bboxes):
        (x,y,w,h) = bbox
        print(x,y,w,h)
        class_name = classes[class_id]

        if class_name in active_buttons:
             cv2.putText(frame, class_name , (x,y-5,),cv2.FONT_HERSHEY_SIMPLEX,1,(200,0,50),2)
             cv2.rectangle(frame, (x,y), (x+w,y+h), (200,0,50), 3)
        
         
    
    # display buttons
    button.display_buttons(frame)

    cv2.imshow("Frame",frame)
    key =  cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows

 
    







