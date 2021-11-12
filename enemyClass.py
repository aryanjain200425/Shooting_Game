import pygame
class Enemy:


    def __init__(self, x, y, img=pygame.image.load('ghost.png')):
        self.x = x
        self.y = y
        self.img = img

    def getLoc(self):
        return self.x, self.y

    def getImg(self):
        return self.img

    def setLoc(self, x, y):
        self.x = x
        self.y = y

