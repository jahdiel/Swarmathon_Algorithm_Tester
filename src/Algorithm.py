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
class Algorithm:

    def __init__(self, CanvasWindow, RoverCluster, Targets, FrameRate):
        """ Initializes the Algorithm class.
        Parameters:
        ------------
            CanvasWindow : CanvasWindow object

            RoverCluster : RoverCluster object

            Targets : Target object

            FrameRate : int
                The framerate of the canvas.
                It is in frames per milliseconds.

        Attributes:
        ------------
            canvasWindow : CanvasWindow object

            roverCluster : RoverCluster object

            targets : Target object
        """

        self.canvasWindow = CanvasWindow
        self.roverCluster = RoverCluster
        self.targets = Targets
        self.framerate = FrameRate

    def mainAlgorithm(self):
        """
        Algorithm:
            Move
            Search
            If Target found -> Pick
            Return to nest
            When in Nest -> Reset Rover and Release the Target
        """

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

    def updateRovers(self):
        """ Updates the rovers.
        This is where the main algorithm should be implemented.
        """
        self.mainAlgorithm()

        self.canvasWindow.master.update_idletasks()
        self.canvasWindow.master.after(self.framerate, self.updateRovers)
