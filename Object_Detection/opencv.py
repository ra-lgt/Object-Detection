from cv2 import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np
import pyttsx3  as py
import time


weight="ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
config="frozen_inference_graph.pb"
start=py.init()


files=open("coco.names.txt","r")
coco=[]
coco_2=[]
for names in files:
    coco.append(names)
for line in coco:
    coco_2+=line.split(",")

net=cv.dnn_DetectionModel(weight,config)
net.setInputSize(320,320)
net.setInputScale(1.0/127.5)
net.setInputMean((127.5,127.5,127.5))
net.setInputSwapRB(True)

vid=cv.VideoCapture("demo1.mp4")
vid.set(3,648)
vid.set(4,480)

while True:
    video,image=vid.read()

    ids,confidence,bbox=net.detect(image,confThreshold=0.6)
    if(len(ids)!=0):
        try:
            for id,conf,box in zip(ids.flatten(),confidence.flatten(),bbox):
                cv.rectangle(image,box,color=(0,255,0),thickness=1)
                cv.putText(image,coco_2[id-1],(box[0]+1,box[1]+1),cv.FONT_HERSHEY_DUPLEX,1,(0,225,0),2)
                cv.imshow("output",image)
                #if ids==1:
                    #start.say("person")
                    #start.runAndWait()
                #elif ids==3:
                    #start.say("car")
                    #start.runAndWait()
                #else:
                    #pass
        except:
            pass
        if cv.waitKey(1) & 0XFF==ord('q'):
            break
cv.release()
cv.destroyAllWindows()        