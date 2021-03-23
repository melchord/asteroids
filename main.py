# Import modules
import pygame
import math
import random

# initialize pygame
pygame.init()

# colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#constants
width = 1000
height = 800
screen = pygame.display.set_mode((width, height))
starting_state = "Menu";

# convert cartesian coordinates to pygame coordinates
def to_coord(coords):
  return (width / 2 + coords[0], height/2 - coords[1])

def to_x(coord_x):
  return width/2 + coord_x

def to_y(coord_y):
  return height/2 - coord_y

# Draw text on the screen
def draw_text(text, color, x ,y, text_size, center=True):
  screen_text = pygame.font.SysFont("Calibri", text_size).render(text, True, color)
  if center:
    rect = screen_text.get_rect()
    rect.center = (to_x(x), to_y(y))
  else:
    rect = (to_x(x), to_y(y))
  screen.blit(screen_text, rect)

# TODO: Check for collisions
def isColliding():
  return 0


# Create ship class
class Ship:
  def __init__(self):
    self.angle = 0
    self.rotate = 0
  
  def update_ship(self):
    # TODO: Move Ship
    # Rotate Ship
    self.angle += self.rotate
  
  def draw_ship(self):
    # Draw ship
    pygame.draw.lines(screen, WHITE, True, [to_coord([0, -18]), to_coord([18, -24]), to_coord([0, 24]), to_coord([-18, -24])])

def game():
  # Init variables
  game_state = starting_state
  ship_state = "Alive"
  ship = Ship()

  # Run Game
  while game_state != "Exit":
    # Game menu
    while game_state == "Menu":
      screen.fill(BLACK)
      draw_text("ASTEROIDS", WHITE, 0, 100, 100)
      draw_text("Press any key to START", WHITE, 0, 0, 50)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_state = "Exit"
        if event.type == pygame.KEYDOWN:
          game_state = "Game"
      pygame.display.update()
    
    # Draw Initial Ship
    screen.fill(BLACK)
    ship.draw_ship()

    # User Inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_state = "Exit"

    # Update screen
    pygame.display.update()

# State game
game()

# End game
pygame.quit()
quit()