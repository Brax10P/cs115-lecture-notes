import pygame
from pygame.constants import KEYDOWN

#init pygame
pygame.init() 

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

#Setting Snake Current Position
cur_pos = [300,200]
direction = "down"
snake_body = [
  [300,200],
  [300,180],
  [300,160],
  [300,140]
]


""" Game Loop """
running = True
while running:
  """Handle Events"""
  for event in pygame.event.get():
    if event.type == pygame.quit:
      running = False
    if event.type == KEYDOWN:
      if event.key == pygame.K_ESCAPE: #escape key
        running = False
      if event.key == pygame.K_w and direction != "down": #up direction
        direction = "up" #y-coord
      if event.key == pygame.K_s and direction != "up": #down
        direction = "down" #y-coord
      if event.key == pygame.K_a and direction != "right": #left
        direction = "left" #x-coord
      if event.key == pygame.K_d and direction != "left": #right
        direction = "right" #x-coord
        
        


  """Update Our Game State"""
  #update direction
  if direction == "up":
    cur_pos[1] -= 20
  if direction == "down":
    cur_pos[1] += 20
  if direction == "left":
    cur_pos[0] -= 20
  if direction == "right":
    cur_pos[0] += 20

  if cur_pos[0] < 0:
    cur_pos[0] = 0
    running = False
  if cur_pos[0] > width-20:
    cur_pos[0] = width-20 
    running = False
  if cur_pos[1] < 0:
    cur_pos[1] = 0
    running = False
  if cur_pos[1] > height-20: 
    cur_pos[1] = height-20
    running = False


  #Snake Movement
  snake_body.insert(0, list(cur_pos))
  snake_body.pop()

  #handle lose state

  """Draw to our Screen"""
  #clear screen
  screen.fill("white")

  #draw snake
  for body in snake_body:
    pygame.draw.rect(
      screen, 
      "blue", 
      pygame.Rect((body[0], body[1]), (20,20)))
  



  #update screen
  pygame.display.flip()

  #fps
  dt = clock.tick(speed)/1000

#quit pygame
pygame.quit()

