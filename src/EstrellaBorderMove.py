from Algorithm import *

class EstrellaBorderMove(Algorithm):

    def __init__(self, CanvasWindow, RoverCluster, Targets, FrameRate):
        """ Initializes the Estrella (Algorithm) class.
            Constructor for Estrella Algorithm

        :param CanvasWindow: CanvasWindow object
        :param RoverCluster: RoverCluster object
        :param Targets: Target object
        :param FrameRate: int
                The framerate of the canvas.
                It is in frames per milliseconds.

        :return: None
        """
        super(EstrellaBorderMove, self).__init__(CanvasWindow, RoverCluster, Targets, FrameRate)

    def mainAlgorithm(self):
        """ This method implement the main Estrella algorithm.

        -Search
        -Move
        -Return to Nest
        -If rover is Inside Arena --> Reach the border?
        -If rover is Inside Angle --> Turns x angle
        -If rover is on sides Degrees --> Turns x angle
        -If rover is In Nest --> Rotate rover fixed angle if found border(FB)
         and turn FB = False... Otherwise rotate 180

         :return: None
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

                if rover.angle >= 45 and rover.angle < 135:
                    rover.rotate(180)
                elif rover.angle >= 135 and rover.angle < 225:
                    rover.rotate(270)
                elif rover.angle >= 225 and rover.angle < 315:
                    rover.rotate(0)
                else:
                    rover.rotate(90)

                for i in xrange(4):
                    rover.move()
                rover.returnToNest()

            if rover.isInNest():
                if rover.foundBorder:
                    rover.foundBorder = False
                    rover.rotate(rover.angle+190)
                    for i in xrange(10):
                        rover.move()
                else:
                    rover.rotate(rover.angle+180)

                target = rover.resetInNest()
                self.targets.removeTarget(target)
