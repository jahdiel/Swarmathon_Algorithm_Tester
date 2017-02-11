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
import math

class RoverCluster:

    def __init__(self, canvasWindows):
        """ Initializes the RoverCluster class.
        Parameters:
        ------------
            roverList : list
                A rover list which has Rover objects as elements.
            canvasWindow : CanvasWindow object
                CanvasWindow object in which the rovers inside roverList are in.

        :return: None
        """
        self.roverList = []
        self.canvasWindow = canvasWindows


    def setRoversInNest(self):
        """ Sets the rovers inside the rover list in to their respective positions
        at the boundary of the nest.
        Parameters:
        ------------
            angleStepSize : int
                The amount of degrees the next rover will be placed to the right of the previous one.
            angle : int
                The current angle in which the rover will be placed.

        Note: The algorithm places the first rover in the initial position. Then places the next plus 180 degrees,
        of the first one and the next after that minus 180 - angleStepSize degrees.

        :return: None
        """
        angleStepSize = 60  # in degrees
        angle = 0
        for idx, rover in enumerate(self.roverList):
            rover.rotate(angle)

            # Parametric Equation of a Circle
            x = self.canvasWindow.center[0] + self.canvasWindow.radius * math.cos(math.radians(angle))
            y = self.canvasWindow.center[1] - self.canvasWindow.radius * math.sin(math.radians(angle))
            rover.setPosition(int(x), int(y))
            if idx % 2 == 0:
                angle += 180
            else:
                angle = 180 - angle + angleStepSize


    def addRover(self, rover):
        """ Adds rover object to the rover list.
        The list represents the cluster of rovers.
        Parameters:
        ------------
            rover : Rover object
                A rover object to be added to the cluster of rovers.

        :return: None
        """
        self.roverList.append(rover)

