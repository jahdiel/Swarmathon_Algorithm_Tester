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

    def insideAngle(self):

        if self.angle >= 45 and self.angle <=135 or self.angle >= 225 and self.angle <= 315:
            return True

    def sidesDegrees(self):

        if self.angle < 45 and self.angle >= 0 or self.angle < 360 and self.angle > 315 or self.angle > 135 and self.angle < 225 or self.angle > 360:
            return True
