import pygame

#init pygame
pygame.init 

#window dimensions
width = 600
height = 400
screen = pygame.display.set_mode((width,height))

#set window title
pygame.display.set_caption("Snake")

#fps
clock = pygame.time.Clock()
dt = 0
speed = 10

""" Game Loop """
running = True
while running:
  """Handle Events"""
  for event in pygame.event.get():
    if event.type == pygame.quit:
      running = False


  """Update Our Game State"""


  """Draw to our Screen"""
  #clear screen
  screen.fill("white")

  #update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed)/1000

#quit pygame
pygame.quit()

