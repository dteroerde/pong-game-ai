from random import randrange
import pygame
import numpy as np

from FeedForwardNetwork import feedForwardNetwork
from player import Player
from ball import Ball

from settings import NUMBER_PLAYERS, WHITE, FONT_SIZE, START_POINT_DESC, BLACK, screen, clock, size

GAME_AHEAD = False
score = 0
generation = 1
highestScoreAllTime = 0
generationFromHighestScore = 1


def howToMove(i):
    switcher = {
        0: -5,
        1: 5,
        2: 0
    }
    return switcher.get(i)


players = []
balls = []
for i in range(NUMBER_PLAYERS):
    players.append(Player())
    balls.append(Ball())

isWinner = players[-1]
players[-1].isWinner = True

while not GAME_AHEAD:
    screen.fill(WHITE)

    isAlive = 0
    bestScore = -9e99
    bestScoreIndex = -1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GAME_AHEAD = True

    for i, player in enumerate(players):

        input = np.array([[balls[i].currentXPos, player.posPlayer]])
        player.howToMove = feedForwardNetwork(input, player.weights, player.bias)
        player.movePlayer = howToMove(player.howToMove)

        if player.isAlive:
            player.update()
            balls[i].update(player)
            isAlive += 1
            if player != isWinner:
                player.drawPlayers()
                balls[i].drawBall()
                player.isWinner = False

        if player.score > bestScore:
            bestScore = player.score
            isWinner = players[i]
            if bestScore > highestScoreAllTime:
                highestScoreAllTime = bestScore
                generationFromHighestScore = generation

    if isAlive == 0:
        generation += 1
        isWinner.start()
        players.clear()
        balls.clear()
        random_start = currentXPos = randrange(0, size[0])
        for i in range(NUMBER_PLAYERS - 1):
            players.append(Player(weights=isWinner.weights, bias=isWinner.bias, start=False))
            balls.append(Ball(currentXPos=random_start))

        players.append(isWinner)
        balls.append(Ball(currentXPos=random_start))

    font = pygame.font.SysFont('ComicSans', FONT_SIZE, False, False)
    screen.blit(font.render("Score: " + str(bestScore), True, BLACK), START_POINT_DESC)
    screen.blit(font.render("Alive: " + str(isAlive), True, BLACK), [START_POINT_DESC[0], START_POINT_DESC[1] + 20])
    screen.blit(font.render("Generation: " + str(generation), True, BLACK),
                [START_POINT_DESC[0], START_POINT_DESC[1] + 2 * 20])
    screen.blit(font.render(
        "Best score in game: " + str(highestScoreAllTime) + " in Generation: " + str(generationFromHighestScore), True,
        BLACK), [START_POINT_DESC[0], START_POINT_DESC[1] + 3 * 20])
    pygame.display.flip()
    clock.tick(200)

pygame.quit()
