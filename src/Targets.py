import numpy as np
from Target import Target

class Targets:

    def __init__(self, CanvasWindow, numOfTargets, image):
        """ Initializes the Rover class.
               Parameters:
               ------------
                   CanvasWindow : CanvasWindow object
                       CanvasWindow object for the targets.
                   numOfTargets : int
                       The total number of targets.
                   image : Image file
                       The image file for the targets
               Attributes:
               ------------
                   canvasWindow:
                   numOfTargets:
                   targetList:
                   canvas_height:
                   canvas_width:
               """


        self.canvasWindow = CanvasWindow
        self.numOfTargets = numOfTargets
        self.targetCoords = self.generateTargetCoordinates()
        self.size = numOfTargets
        self.targetsList = []
        for i in xrange(numOfTargets):
            self.targetsList.append(Target(self.canvasWindow, i, image, self.targetCoords[i]))
            self.canvasWindow.map_array[self.targetCoords[i][0]][self.targetCoords[i][1]] = 1

        # Canvas variables
        self.canvas_height = self.canvasWindow.canvas.winfo_height()
        self.canvas_width = self.canvasWindow.canvas.winfo_width()

    def generateTargetCoordinates(self):
        """ Generate a list of tuples with the coordinates of the targets"""
        rand_x = np.random.randint(20, self.canvasWindow.width,size=self.numOfTargets)
        rand_y = np.random.randint(20, self.canvasWindow.height, size=self.numOfTargets)

        return zip(rand_x, rand_y)

    def getTargetAtPos(self, posTup):
        """ Gets target at the specified position
                Parameters:
                ------------
                posTup : array
                An array to be searched
          """
        for target in self.targetsList:
            if np.array_equal(posTup, np.array(target.pos)):
                return target

    def removeTarget(self, target):

        self.targetsList.remove(target)
        self.size = len(self.targetsList)
