"""
MIT License (MIT)

Copyright (c) FALL 2016, Jahdiel Alvarez

Author: Jahdiel Alvarez

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software,
and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED,
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


"""
import numpy as np
from Target import Target
from Tkinter import Label

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
        self.canvasWindow.tbwCaptured.config(text=self.size)

    def generateTargetCoordinates(self):
        """
        Generate a list of tuples with the coordinates of the targets
        :return:
        """
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
        """
        Removes specified target from the targets list.
        :param target: Target object
        :return: void
        """
        if target:
            self.targetsList.remove(target)
            self.size = len(self.targetsList)
            ######## For ToolBox Window ######
            self.canvasWindow.tbwCaptured.config(text=str(self.numOfTargets - self.size)+' of '+str(self.numOfTargets))
            ##################################
            print 'Target List Size:', self.size
