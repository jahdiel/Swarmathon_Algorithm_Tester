
class Target:

    def __init__(self, CanvasWindow, numberIndex, image, posTup):
        """
        Initializes the Target class

        Parameters:
        ------------
            CanvasWindow: CanvasWindow object
            CanvasWindow object where the target is in

            numberIndex: int
            Index of the targer

            image: Image file
            Image of the target

            posTup: tuple
            Position of the target
        Attributes:
        ------------
            canvasWindow: CanvasWindow object
            canvas:
            img:
            imgPIL:
            width:
            height:
            index:
            id:
            pos:

        """


        self.canvasWindow = CanvasWindow
        self.canvas = CanvasWindow.canvas

        self.img, self.imgPIL = CanvasWindow.imageFormatting(image, (8, 8))
        self.width, self.height = self.imgPIL.size

        self.index = numberIndex
        self.id = CanvasWindow.canvas.create_image(posTup, image=self.img)
        self.pos = self.canvas.coords(self.id)
