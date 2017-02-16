from Algorithm import *

class Cuadrito2(Algorithm):

    def __init__(self, CanvasWindow, RoverCluster, Targets, FrameRate):
        """ Initializes the Cuadrito2 (Algorithm) class.

        :param CanvasWindow: CanvasWindow object
        :param RoverCluster: RoverCluster object
        :param Targets: Target object
        :param FrameRate: Int
                    The framerate of the canvas.
                    It is in frames per milliseconds.

        :return: None
        """
        Algorithm.__init__(self, CanvasWindow, RoverCluster, Targets, FrameRate)


        self.alpha = 20
        self.d_m = self.alpha
        self.epsilon = 0
        self.counter = 0
        self.is360 = 0
        self.start = True

    def mainAlgorithm(self):

        for rover in self.roverCluster.roverList:

            t_coords, found = rover.moveAndSearch()

            if rover.number == 0:
                self.squareMove(rover)

        return

    def squareMove(self, rover):
        """ Makes square pattern on one rover.
        :param rover: Rover object

        :return: None
        """
        if rover.angle == 0:
            self.counter += 1
            if self.counter == self.d_m - 10 and self.start:
                rover.rotate(90)
                self.start = False
                self.d_m = self.d_m + self.epsilon
                self.counter = 0
            elif self.counter == self.epsilon and not self.start:
                rover.rotate(rover.angle+90)
                self.d_m = self.d_m + self.epsilon - 5
                self.counter = 0
        elif rover.angle == 90 and not self.is360:
            print self.counter
            rover.move()
            self.counter += 1
            if self.counter == self.d_m:
                rover.rotate(180)
                self.counter = 0
        elif rover.angle == 180.0:
            rover.move()
            self.counter += 1
            if self.counter == 2*self.d_m + 5:
                rover.rotate(270)
                self.counter = 0
        elif rover.angle == 270:
            rover.move()
            self.counter += 1
            if self.counter == 2*self.d_m:
                rover.rotate(360)
                self.counter = 0
        else:
            if not self.is360:
                rover.move()
                self.counter += 1
                if self.counter == 2 * self.d_m + 5:
                    rover.rotate(90)
                    self.counter = 0
                    self.is360 = True
            else:
                rover.move()
                self.counter += 1
                if self.counter == self.d_m:
                    rover.rotate(0)
                    self.epsilon = 10
                    self.is360 = False
                    self.counter = 0
