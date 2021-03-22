# Import modules
import pygame
import math
import random

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# initialize pygame and global variables
pygame.init()
width = 400
height = 500
screen = pygame.display.set_mode((width, height))
done = False

# convert cartesian coordinates to pygame coordinates
def to_coord(coords):
  return (width / 2 + coords[0], height/2 - coords[1])

# draw function
def draw():
  pygame.draw.lines(screen, WHITE, True, [to_coord([0, -18]), to_coord([18, -24])])

# Events
while not done:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      done = True
  draw()
  pygame.display.flip()