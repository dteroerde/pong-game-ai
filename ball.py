from random import random

import pygame
from settings import size, BALL_SIZE, PLAYER_LENGTH, PLAYER_HEIGHT, screen, BLACK
from random import randrange


class Ball:

    def __init__(self, currentXPos=randrange(0, size[0]), currentYPos=0, moveXPos=5, moveYPos=5):
        self.currentXPos = currentXPos
        self.currentYPos = currentYPos
        self.xPos = currentXPos - moveXPos
        self.yPos = currentYPos - moveYPos
        self.moveXPos = moveXPos
        self.moveYPos = moveYPos
        self.isAlive = True

    def update(self, player):
        self.xPos = self.currentXPos
        self.yPos = self.currentYPos

        self.currentXPos += self.moveXPos
        self.currentYPos += self.moveYPos

        if self.currentXPos < 0:
            self.currentXPos = 0
            self.moveXPos = - self.moveXPos
        elif self.currentXPos > size[0]:
            self.currentXPos = size[0]
            self.moveXPos = - self.moveXPos
        elif self.currentYPos < 0:
            self.currentYPos = 0
            self.moveYPos = - self.moveYPos
        elif self.currentXPos > player.posPlayer and self.currentXPos < player.posPlayer + PLAYER_LENGTH\
                and self.yPos < size[1] - PLAYER_HEIGHT-BALL_SIZE and self.currentYPos >= size[1] - PLAYER_HEIGHT-BALL_SIZE:
            self.moveYPos = - self.moveYPos
            player.score += 1
        elif self.currentYPos > size[1]:
            self.moveYPos = - self.moveYPos
            player.score -= 1
            player.isAlive = False

    def drawBall(self, rounded=10):
        pygame.draw.rect(screen, BLACK, [self.currentXPos, self.currentYPos, BALL_SIZE, BALL_SIZE], border_radius=rounded)
