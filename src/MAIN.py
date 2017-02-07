"""
Swarm Algorithm Tester:

Software to test algorithms for the NASA Swarmathon Competition

Universidad de Puerto Rico, Mayaguez
January 2017

"""

from CanvasWindow import CanvasWindow
from Rover import Rover
from RoverCluster import RoverCluster
from Targets import Targets
from Algorithm import Algorithm
from Tkinter import *
from Estrella import Estrella
from RoverEstrellao import RoverEstrellao

# Algorithms
from El_Cuadrito import Cuadrito

# Things To DO:
#-------------------
# TODO: Separate Window
# TODO: Don't place targets inside the nest
# TODO: Create the distributions of the targets
#-------------------


# Algorithm Object References
# ----------------------------
# Set the Rover Class(inherited classes) you are using int RoverObj
# Set the Algorithm Class(inherited classes) you are using int AlgoObj
RoverObj = RoverEstrellao
AlgoObj = Estrella
FRAMERATE = 50

# Tkinter Master Object
master = Tk()

# Canvas Object
canvasWindow = CanvasWindow(1000, 700, master)

# Image Files
targetImg = "C:\Users\Brian\Documents\GitHub\Swarmathon_Algorithm_Tester\Media\Rock.png"
roverImg = "C:\Users\Brian\Documents\GitHub\Swarmathon_Algorithm_Tester\Media\Rover1_PNG.png"

# Targets Object
NUM_OF_TARGETS = 50
targets = Targets(canvasWindow, NUM_OF_TARGETS, image=targetImg)

# Rover Cluster
roverCluster = RoverCluster(canvasWindow)
NUM_OF_ROVERS = 4

# Set Rovers
for i in xrange(NUM_OF_ROVERS):
    rover = RoverObj(canvasWindow, 0, 0, number=i)  # Initialize rover
    roverCluster.addRover(rover) # Add rover to rover cluster

# Set the rovers in nest position
roverCluster.setRoversInNest()

# Algorithm Object inherited from Algorithm Class
algorithm = AlgoObj(canvasWindow, roverCluster, targets, FRAMERATE)

# Update Canvas
canvasWindow.showUpdate(algorithm.updateRovers)
