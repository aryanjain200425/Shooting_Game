class Enemy:


    def __init__(self, x, y, angle, image):
        self.xCoor = x
        self.yCoor = y
        self.angle = angle
        self.image = image

    def changeX(self, x):
        self.xCoor = self.xCoor + x

    def changeY(self, y):
        self.yCoor = self.yCoor + y

    def setAngle(self, angle):
        self.angle = angle

    def setX(self, x):
        self.xCoor = x

    def setY(self, y):
        self.yCoor = y
