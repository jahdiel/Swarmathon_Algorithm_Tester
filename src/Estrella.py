from Algorithm import *

class Estrella(Algorithm):

    def __init__(self, CanvasWindow, RoverCluster, Targets, FrameRate):
        super(Estrella, self).__init__(CanvasWindow, RoverCluster, Targets, FrameRate)

    def mainAlgorithm(self):

         for rover in self.roverCluster.roverList:
             rover.move()
             t_coords, found = rover.searchTarget()
             if found:
                 target_found = self.targets.getTargetAtPos(t_coords)
                 if rover.pickTarget(target_found):
                      rover.returnToNest()

             if rover.isInNest():
                 target = rover.resetInNest()
                 if target is not None:
                     self.targets.removeTarget(target)
                     print 'Target List Size:', self.targets.size





