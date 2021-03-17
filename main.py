# Import modules
import pygame
import math
import random

# initialize pygame and global variables
pygame.init()
width = 400;
height = 300;
screen = pygame.display.set_mode((width, height))
done = False
is_blue = True

# draw function
def draw():
  if is_blue: color = (0, 128, 255)
  else: color = (255, 100, 0)
  pygame.draw.rect(screen, color, pygame.Rect(30, 30, 60, 60))
  pygame.draw.circle(screen, (255, 255, 255), (width/2, height/2), 30)

# Events
while not done:
  for event in pygame.event.get():
    if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
      is_blue = not is_blue
    if event.type == pygame.QUIT:
      done = True
  draw()
  pygame.display.flip()