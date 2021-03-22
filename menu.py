# This file is a proof of concept for drawing the menu
# Import pygame
import pygame

# initialize pygame
pygame.init()

# colors
BLACK = (0, 0 , 0)
WHITE = (255, 255, 255)

# constants
WIDTH = 1000
HEIGHT = 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
STARTING_STATE = 'Menu';

# convert cartesian coordinates to pygame coordinates
def to_coord(coords):
  return (WIDTH/2 + coords[0], HEIGHT/2 - coords[1])

def to_x(coord_x):
  return WIDTH/2 + coord_x

def to_y(coord_y):
  return HEIGHT/2 - coord_y

# Draw text on the screen
def draw_text(text, color, x, y, text_size, center=True):
  screen_text = pygame.font.SysFont("Calibri", text_size).render(text, True, color)
  if center:
    rect = screen_text.get_rect()
    rect.center = (to_x(x), to_y(y))
  else: 
    rect = (to_x(x), to_y(y))
  SCREEN.blit(screen_text, rect)

def game():
  # Init variables
  game_state = STARTING_STATE

  # Run game
  while game_state != "Exit":
    # Game menu
    while game_state == "Menu":
      SCREEN.fill(BLACK);
      draw_text("ASTEROIDS", WHITE, 0, 100, 100)
      draw_text("Press any key to START", WHITE, 0, 0, 50)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          game_state = "Exit"
        if event.type == pygame.KEYDOWN:
          game_state = "Game"
      pygame.display.update()

    # User Inputs
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        game_state = "Exit"
    
    pygame.display.flip()

# Start Game
game()

# Eng game
pygame.quit()
quit()