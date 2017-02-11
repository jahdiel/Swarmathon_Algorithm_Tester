from Rover import *

class RoverEstrellao(Rover):

    def __init__(self, CanvasWindow, pos_x, pos_y, number):
        """ Initializes the RoverEstrellao class
            Variables of Rover used on Estrella

        :param CanvasWindow: CanvasWindow object
        :param pos_x: Int
                    Initial x position
        :param pos_y: Int
                    Initial y position
        :param number: Int
                    Number tag of the rover

        :return: Void
        """
        super(RoverEstrellao, self).__init__(CanvasWindow, pos_x, pos_y, number)
        self.velocity = 5
        self.foundBorder = False

    def isInNest(self):
        """ Check if rover is inside the nest.

        :return: True if is inside else False
        """
        center = np.array(self.canvasWindow.center)
        radius = self.canvasWindow.radius - 30
        return np.linalg.norm(self.posCenter - center) <= radius


