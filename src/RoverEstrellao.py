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

    def insideAngle(self):
        """ These ranges of angles helps to control
            better the rover and maintain it inside the arena.

            Rover Angle(RA) ranges; 45 <= RA <= 135
            OR 225 <= RA <= 315

        :return: True if is inside one of the ranges, otherwise False.
        """
        if self.angle >= 45 and self.angle <=135 or self.angle >= 225 and self.angle <= 315:
            return True

    def sidesDegrees(self):
        """ These ranges of angles helps to control
            better the rover and maintain it inside the arena.

            Rover Angle(RA) ranges;
            0 <= RA < 45      OR
            135 < RA < 225    OR
            315 < RA < 360    OR
            RA > 360

        :returns: True if is inside one of the ranges, otherwise false.
        """

        if self.angle < 45 and self.angle >= 0 or self.angle < 360 and self.angle > 315 or self.angle > 135 and self.angle < 225 or self.angle > 360:
            return True
