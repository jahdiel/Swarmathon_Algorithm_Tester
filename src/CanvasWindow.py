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
from PIL import Image, ImageTk
import numpy as np

class CanvasWindow:

    def __init__(self, width, height, master=None):
        """ Initializes the Rover class.
            Attributes:
            ------------
                master : Tkinter object
                    Tkinter object which holds the canvas.
                canvas : Canvas object
                    The canvas of the rover.
                width, height : int, int
                    Width and height of the canvas.
                center : tuple
                    Coordinates of the center of the canvas and of the nest.
                radius : float
                    The radius of the nest
                nest : Canvas oval object
                    Oval object that represents the nest.
                map_array : array
                    An array filles with zeroes
            """
        if master is not None:
            self.master = master
        else:
            self.master = Tk()
        self.canvas = Canvas(self.master, width=width, height=height)
        self.width = width
        self.height = height
        self.map_array = np.zeros((width, height))

        # Nest Variables
        self.center = (self.width / 2, self.height / 2)
        self.radius = max(self.width, self.height) * 0.05
        self.nest = self.createNest()


    def createNest(self):
        """ Creates the Nest in the middle of the canvas."""
        radius = self.radius
        return self.canvas.create_rectangle(self.center[0]-radius, self.center[1]-radius, self.center[0]+radius, self.center[1]+radius, fill='green')

    @staticmethod
    def imageFormatting(image, resizeTup):
        """ Formats the image of the rover in order for it to work with Tkinter's Canvas class.
        The image is stored inside a PIL object.
        Parameters:
        ------------
            image : string
                File path to the image to be used for the rover.
        """
        img = Image.open(image).rotate(-90)
        img = img.resize(resizeTup, Image.ANTIALIAS)  # Resize the image to desired size

        return ImageTk.PhotoImage(img), img


    def showUpdate(self, updateRoverFunct=None):
        """ Shows the initialized and updated canvas
        Parameters:
        -------------
            updateRoverFunct : function
                Function which will update the rovers movement
        """
        self.canvas.pack()
        if updateRoverFunct is not None:
            self.master.after(10, updateRoverFunct)
        self.master.mainloop()
