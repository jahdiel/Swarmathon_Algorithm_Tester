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
from Algorithm import *

class Cuadrito(Algorithm):

    def __init__(self, CanvasWindow, RoverCluster, Targets, FrameRate):
        Algorithm.__init__(self, CanvasWindow, RoverCluster, Targets, FrameRate)

        self.alpha = 20
        self.d_m = self.alpha
        self.epsilon = 0
        self.counter = 0
        self.is360 = 0
        self.start = True

    def mainAlgorithm(self):

        # TODO: Apply Cuadrito Algorithm
        for rover in self.roverCluster.roverList:
            rover.move()
            t_coords, found = rover.searchTarget()

            if rover.number == 0:
                self.squareMove(rover, 2)

        return

    def squareMove(self, rover, step):
        if rover.angle == 0:
            rover.move()
            self.counter += 1
            if self.counter == self.d_m and self.start:
                rover.rotate(rover.angle + 90)
                self.start = False
                self.d_m = self.d_m + self.epsilon
                self.counter = 0
            elif self.counter == self.epsilon and not self.start:
                rover.rotate(rover.angle+90)
                self.d_m = self.d_m + self.epsilon
                self.counter = 0
        elif rover.angle == 90 and not self.is360:
            print self.counter
            rover.move()
            self.counter += 1
            if self.counter == self.d_m:
                rover.rotate(rover.angle+90)
                self.counter = 0
        elif rover.angle == 180.0 or rover.angle == 270.0:
            rover.move()
            self.counter += 1
            if self.counter == 2*self.d_m:
                rover.rotate(rover.angle+90)
                self.counter = 0
        else:
            if not self.is360:
                rover.move()
                self.counter += 1
                if self.counter == 2 * self.d_m:
                    rover.rotate(90)
                    self.counter = 0
                    self.is360 = True
            else:
                rover.move()
                self.counter += 1
                if self.counter == self.d_m:
                    rover.rotate(0)
                    self.epsilon += step
                    self.is360 = False
                    self.counter = 0



