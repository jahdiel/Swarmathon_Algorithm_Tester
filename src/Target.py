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

        :return: None
        """

        self.canvasWindow = CanvasWindow
        self.canvas = CanvasWindow.canvas

        self.img, self.imgPIL = CanvasWindow.imageFormatting(image, (3, 3))
        self.width, self.height = self.imgPIL.size

        self.index = numberIndex
        self.id = CanvasWindow.canvas.create_image(posTup, image=self.img)
        self.pos = self.canvas.coords(self.id)
