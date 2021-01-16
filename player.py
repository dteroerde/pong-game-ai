import pickle
import random

import pygame
from settings import START_POINT_PLAYER, PLAYER_HEIGHT, size, BLACK, GRAY, PLAYER_LENGTH, screen
from pandas import np

class Player:

    def __init__(self, posPlayer=START_POINT_PLAYER, weights=-1, bias=-1, start=True):
        self.movePlayer = 0
        self.posPlayer = posPlayer
        self.isAlive = True
        self.isWinner = False
        self.score = 0
        if start:
            self.weights = self.generateWeights()
        else:
            self.weights = self.mutate(weights, isWeight=True)
        if start:
            self.bias = self.generateBias()
        else:
            self.bias = self.mutate(bias, isWeight=False)

    def mutate(self, mat, isWeight):
        if isWeight:
            weights = np.copy(mat)
            for j in range(2):
                for k in range(3):
                    # Try different scales. However, try not to go below 1.0. The children seem to be too similar to their parents
                    weights[0][j][k] = np.random.normal(loc=mat[0][j][k], scale=1.2)
            return weights
        else:
            bias = np.copy(mat)
            for j in range(3):
                # Try different scales. However, try not to go below 1.0. The children seem to be too similar to their parents
                bias[0][j] = np.random.normal(loc=mat[0][j], scale=1.2)
            return bias

    def generateWeights(self):
        weights = []
        weights.append(np.random.rand(2, 3))
        return weights

    def generateBias(self):
        bias = []
        bias.append(np.random.rand(3))
        return bias

    def start(self):
        self.posPlayer = START_POINT_PLAYER
        self.lastPos = START_POINT_PLAYER
        self.movePlayer = 0
        self.isAlive = True
        self.score = 0

    def update(self):
        self.lastPos = self.posPlayer
        self.posPlayer += self.movePlayer
        if self.posPlayer < 0:
            self.posPlayer = 0
        elif self.posPlayer > size[0]:
            self.posPlayer = size[0]

        self.lastPos = self.posPlayer

    def drawPlayers(self):
        pygame.draw.rect(screen, BLACK, [self.posPlayer, size[1] - PLAYER_HEIGHT, PLAYER_LENGTH, PLAYER_HEIGHT], border_radius=5)
        pygame.draw.rect(screen, GRAY, [self.posPlayer + 2, size[1] - (PLAYER_HEIGHT - 2), PLAYER_LENGTH - 5, PLAYER_HEIGHT - 5], border_radius=5)
