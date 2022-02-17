import cv2
import time
import csv
import math
import numpy as np

from controller import Robot, Camera, Accelerometer
from ImageProcessing import Vision
from Moves import Move
from camera import Camera
from Actions import Action


#inicjaliacja do webotsow
robot = Robot()  # tworzenie klasy Robot
timestep = int(robot.getBasicTimeStep())
Camera_Observation = Vision(robot.getDevice("camera"), timestep)  # dodanie kamery
move = Move(robot) #dodanie klasy Move
action = Action(robot,move) #dodanie klasy Action


number_of_steps = 5



print("START")

lines = Camera_Observation.GetLines()
Camera_img = Shape_Real(lines)


        #Jesli chcesz zobaczyc jak wykrywa linie odkomentuj
img = Camera_Observation.CleanImg()
s = Camera_Observation.MaskedLines()
        
for line in lines:
    line=line[0]
    cv2.line(img, (line[0], line[1]), (line[2], line[3]), (0, 0, 255), 3)
cv2.imshow("test",s)
cv2.imshow("narysowane",img)
cv2.waitKey()

        # obraz z symulacji i pogrubienie go
Lines_from_camera = np.zeros((400, 400, 3), dtype=np.uint8)
Camera_img.draw(Lines_from_camera, dir2color=True)

action.move_forward(robot, number_of_steps)
action.turn_right(robot, 2)
action.turn_left(robot, 1)
action.single_step(robot)
action.crouch(robot)
action.single_step(robot)


print("FINISH")

