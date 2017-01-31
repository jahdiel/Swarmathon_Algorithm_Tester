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
        """
        self.roverList.append(rover)

