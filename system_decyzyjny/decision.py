import numpy as np
import math

class ball:
    def __init__(self, position):
        self.position = position

class player:
    def __init__(self, number, angle, position):
        self.number = number
        self.angle = angle
        self.position = position

    def description(self):
        return f"player {self.number} has ({self.position.X},{self.position.Y}) position with {self.angle} angle"

    def action(self, number, positionBall):
        angle_difference = np.arctan2( positionBall.y - self.position.Y, positionBall.x - self.position.x)
        distance = np.linalg.norm(positionBall,self.position)

        if np.absolute(self.angle - angle_difference) <= 10/360*2*math.pi and distance >= 10:
            return f"GO"
        if np.absolute(self.angle - angle_difference) <= 10/360*2*math.pi and distance > 10:
            return f"KICK"
        if self.angle - angle_difference > 10 / 360*2*math.pi:
            return f"TURN_RIGHT"
        if self.angle - angle_difference < 10 / 360*2*math.pi:
            return f"TURN_LEFT"