class DrawingFreeHand:
    def __init__(self,sam):
        self.sam = sam
    def moveForward(self):
        self.sam.forward(10)

    def moveBackward(self):
        self.sam.backward(10)

    def clockwise(self):
        self.sam.setheading(self.sam.heading() - 10)

    def anticlockwise(self):
        self.sam.setheading(self.sam.heading() + 10)

    def clear(self):
        self.sam.clear()
        self.sam.up()
        self.sam.home()
        self.sam.down()