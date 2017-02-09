from Algorithm import *
import random

class Estrella(Algorithm):

    def __init__(self, CanvasWindow, RoverCluster, Targets, FrameRate):
        """
        Constructor for Estrella Algorithm
        :param CanvasWindow:
        :param RoverCluster:
        :param Targets:
        :param FrameRate:
        """
        super(Estrella, self).__init__(CanvasWindow, RoverCluster, Targets, FrameRate)

    def mainAlgorithm(self):
        """
        This method implement the main Estrella algorithm
        :return: void
        """

        for rover in self.roverCluster.roverList:
            rover.move()
            t_coords, found = rover.searchTarget()
            if found:
                target_found = self.targets.getTargetAtPos(t_coords)
                if rover.pickTarget(target_found):
                    rover.returnToNest()

            if not rover.isInsideArena(rover.searchRadius):
                rover.foundBorder = True
                rover.returnToNest()

            if rover.isInNest():
                if rover.foundBorder:
                    rover.foundBorder = False
                    #rover.rotate(random.randint(0, 360))
                    rover.rotate(rover.angle+190)
                    for i in xrange(10):
                        rover.move()
                else:
                    rover.rotate(rover.angle+180)

                target = rover.resetInNest()
                self.targets.removeTarget(target)
