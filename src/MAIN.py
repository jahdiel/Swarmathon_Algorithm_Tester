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
from CanvasWindow import CanvasWindow
from Rover import Rover
from RoverCluster import RoverCluster
from Targets import Targets
from Algorithm import Algorithm
from Tkinter import *
from Estrella import Estrella
from RoverEstrellao import RoverEstrellao
from Cuadrito2 import Cuadrito2
from EstrellaBorderMove import EstrellaBorderMove

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
AlgoObj = EstrellaBorderMove

######## PARAMETERS TO ADJUST #########

NUM_OF_TARGETS = 200  # Set the number of targets
NUM_OF_ROVERS = 1    # Set the number of rovers

#######################################

# Tkinter Master Object
master = Tk()

# Canvas Object
canvasWindow = CanvasWindow(700, 700, NUM_OF_ROVERS, master)

# Image Files
targetImg = "C:\Users\jahdiel.alvarez\Documents\GitHub\Swarmathon_Algorithm_Tester\Media\Rock.png"
roverImg = "C:\Users\jahdiel.alvarez\Documents\GitHub\Swarmathon_Algorithm_Tester\Media\Rover1_PNG.png"

# Targets Object
targets = Targets(canvasWindow, NUM_OF_TARGETS, image=targetImg)

# Rover Cluster
roverCluster = RoverCluster(canvasWindow)

# Set Rovers
for i in xrange(NUM_OF_ROVERS):
    rover = RoverObj(canvasWindow, 0, 0, number=i)  # Initialize rover
    roverCluster.addRover(rover) # Add rover to rover cluster

# Set the rovers in nest position
roverCluster.setRoversInNest()

# Algorithm Object inherited from Algorithm Class
FRAMERATE = 1
algorithm = AlgoObj(canvasWindow, roverCluster, targets, FRAMERATE)

# Update Canvas
canvasWindow.showUpdate(algorithm.updateRovers)

