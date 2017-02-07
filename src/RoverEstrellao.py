from Rover import *

class RoverEstrellao(Rover):

    def __init__(self, CanvasWindow, pos_x, pos_y, number):
        super(RoverEstrellao, self).__init__(CanvasWindow, pos_x, pos_y, number)

        self.velocity = 10
