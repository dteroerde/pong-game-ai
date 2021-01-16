import pygame

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
FONT_SIZE = 20

# Display
size = (800, 600)

# Global Constants
START_POINT_PLAYER = size[0] / 2
START_POINT_DESC = (20, 20)
BALL_SIZE = 15
PLAYER_LENGTH = 100
PLAYER_HEIGHT = 20
NUMBER_PLAYERS = 100

pygame.init()
pygame.display.set_caption("Evolutionary AI")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()