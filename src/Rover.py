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
from Tkinter import *
from PIL import ImageTk
import math
import numpy as np

class Rover(object):

    def __init__(self, CanvasWindow, pos_x, pos_y, number):
        """ Initializes the Rover class.
        Parameters:
        ------------
            canvasWindow : CanvasWindow object
                CanvasWindow object in which the rover is.
            pos_x : int
                Initial x position.
            pos_y : int
                Initial y position.
            number : int
                The number tag of the rover.
        Attributes:
        ------------
            canvasWindow : CanvasWindow object
                CanvasWindow object in which the rover is.
            canvas : Canvas object
                The canvas of the rover.
            img : image object
                Formatted image object of the rover.
            imgPIL : PIL object
                PIL image object of the image of the rover.
            id : Canvas widget instance
                The id of the instance of the rover object.
            pos : list
                List with two elements, which represent the coordinates of the rover.
            width, height : int, int
                Width and height of the image of the rover.
            angle : int
                The rotated angle of the rover.
            velocity : int
                The velocity of the rover.
            canvas_width, canvas_height : int, int
                Width and height of the canvas.
        """
        # Rover variables
        self.canvasWindow = CanvasWindow
        self.canvas = CanvasWindow.canvas
        self.sizeRadius = 5
        self.id = CanvasWindow.canvas.create_oval(pos_x-self.sizeRadius, pos_y-self.sizeRadius, pos_x+self.sizeRadius, pos_y+self.sizeRadius, fill='red')
        self.number = number
        self.pos = self.canvas.coords(self.id)
        self.posCenter = self.getPositionCenter()
        self.width, self.height = self.sizeRadius*2, self.sizeRadius*2
        self.angle = 0  # degrees
        self.velocity = 1
        self.roverTarget = None  # Target object that robot is carrying
        self.targetCoords = []
        self.searchRadius = 21 # Needs to be odd
        self.targetsCaptured = 0  # Amount of targets the rover has captured

        # Rover State Variables
        self.isCarrying = False
        self.isTrace = True

        # Canvas variables
        self.canvas_height = CanvasWindow.height
        self.canvas_width = CanvasWindow.width

    # Setters
    def setPosition(self, x, y):
        """ Moves the rover to the (x,y) pixel coordinate.
        Parameters:
        ------------
            x : int
                Moves the rover to the x pixel in the horizontal direction.
            y : int
                Moves the rover to the y pixel in the vertical direction.

        :return: void
        """
        self.canvas.coords(self.id, (x-self.sizeRadius, y-self.sizeRadius, x+self.sizeRadius, y+self.sizeRadius))
        self.pos = self.canvas.coords(self.id)
        self.posCenter = self.getPositionCenter()


    def getPositionCenter(self):
        """ Gets the center position

        :return: Center
        """
        return np.array(self.pos)[:2] + [self.sizeRadius, self.sizeRadius]

    def move(self):
        """
        Moves the rover. If no delta values are used.
        The rover will move with its velocity in the angle direction.
        :return: void
        """

        if self.isTrace:
            self.canvas.create_polygon(*self.posCenter, outline="black")
        d_x = self.velocity * math.cos(math.radians(self.angle))
        d_y = -self.velocity * math.sin(math.radians(self.angle))
        self.canvas.move(self.id, d_x, d_y)

        self.pos = self.canvas.coords(self.id)
        self.posCenter = self.getPositionCenter()

    def rotate(self, angle):
        """
        Rotates the image of the rover by certain degrees.
        :param angle:(int) Number of degrees the image will be rotated counterclockwise.
        :return: none
        """
        self.angle = angle

    def isInsideArena(self, radius):
        """
        Verifies rover is inside the arena.
        :param radius: Extends the rovers size by such radius.
        :return: True if rover is inside the arena, else False
        """
        x, y = self.posCenter
        x, y = int(x), int(y)
        if x > radius and x < self.canvas_width - radius and y > radius and y < self.canvas_height - radius:
            return True

        return False


    def searchTarget(self):
        """
         Searches for a nearby target.
         Uses the robot as a convolving filter through the image.

         :return: True if found target, otherwise False
        """
        map = self.canvasWindow.map_array
        radius = self.searchRadius
        x, y = self.posCenter
        x, y = int(x), int(y)
        if self.isInsideArena(radius-1):
            roverKernel = map[x-radius:x+radius+1, y-radius:y+radius+1]
            centerIdx = np.array([(roverKernel.shape[0]-1)/2, (roverKernel.shape[1]-1)/2])
            for i in xrange(radius*2+1):
                for j in xrange(radius*2+1):
                    if roverKernel[i][j] == 1:
                        d_list = np.array([i, j]) - centerIdx
                        coords = np.array([x, y]) + d_list
                        print 'Found a Target!!!!!!'
                        return coords, True

        return None, False

    def pickTarget(self, target):
        """ Picks up a target the rover found.
        Parameter:
        ------------
            target : Target object
                The target instance the rover found while searching.

        :return: True, if picks target else False
        """
        if not self.isCarrying:
            self.roverTarget = target
            self.canvasWindow.canvas.itemconfig(self.id, fill='yellow')
            self.canvasWindow.canvas.itemconfig(target.id, state='hidden')
            self.canvasWindow.map_array[int(target.pos[0]), int(target.pos[1])] = 0  # Take the picked target out of the map array
            self.isCarrying = True
            return True

        return False

    def returnToNest(self):
        """
        Make the rover return to the nest.
        :return: void
        """
        center = np.array(self.canvasWindow.center)
        centerVect = center - np.array(self.posCenter, dtype=int)
        angle = math.degrees(math.atan2(centerVect[1], centerVect[0]))
        self.rotate(-angle)

    def isInNest(self):
        """ Check if rover is inside the nest.

        :return: True if inside the nest, else False
        """
        center = np.array(self.canvasWindow.center)
        radius = self.canvasWindow.radius - 10
        return np.linalg.norm(self.posCenter - center) <= radius

    def resetInNest(self):
        """ Resets the rover state variables.
        If the rover is carrying a target when the function is called
        it releases the target in the nest.
        Returns
        ---------
        Returns the target object the rover brought to the nest.
        If the rover is not carrying a target object returns -1.
        """
        if self.isCarrying:
            self.canvas.itemconfig(self.id, fill='red')
            self.isCarrying = False
            self.canvasWindow.canvas.delete(self.roverTarget.id)
            roverTarget = self.roverTarget
            self.roverTarget = None
            self.targetsCaptured += 1
            ######## For ToolBox Window ######
            idx = self.number
            self.canvasWindow.roverLabelList[idx].config(text="Rover "+str(idx)+": "+str(self.targetsCaptured))
            ##################################
            return roverTarget

        return None
