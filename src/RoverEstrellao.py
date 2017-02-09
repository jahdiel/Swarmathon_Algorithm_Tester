from Rover import *

class RoverEstrellao(Rover):

    def __init__(self, CanvasWindow, pos_x, pos_y, number):
        """

        :param CanvasWindow:
        :param pos_x:
        :param pos_y:
        :param number:
        """
        super(RoverEstrellao, self).__init__(CanvasWindow, pos_x, pos_y, number)
        self.velocity = 5
        self.foundBorder = False

    def isInNest(self):
        """ Returns true if rover is inside the nest,
                otherwise returns false.
                """
        center = np.array(self.canvasWindow.center)
        radius = self.canvasWindow.radius - 30
        return np.linalg.norm(self.posCenter - center) <= radius