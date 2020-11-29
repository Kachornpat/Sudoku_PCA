import pygame
import sys

pygame.init()

#set window
screen = pygame.display.set_mode((800, 550))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

prev_x = 0
prev_y = 0

font = pygame.font.SysFont("Ariel.ttf", 50)
number = font.render("5", True, black)
#build white screen
screen.fill(white)
screen.blit(number, (65, 160))
def table(pos, dimension, color):
   for i in range(3):
      for j in range(3):
         pygame.draw.rect(screen, color,
                          (pos[0] + dimension*i, pos[1] + dimension*j, dimension, dimension), 3)
# draw small 3x3 table 9 times
for i in range(3):
   for j in range(3):
      table((50 + 150*i, 50 + 150*j), 50, gray)
# draw 3x3 one time
table((50, 50), 150, black)
# update screen
pygame.display.update()
run = True
while run:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         run = False
         pygame.quit()
         sys.exit()
   if pygame.mouse.get_pressed()[0]:
      pygame.draw.rect(screen, white, (prev_x, prev_y, 47.5, 47.5))
      if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 500:
         pygame.draw.rect(screen,(225, 225, 225),
                          ((pygame.mouse.get_pos()[0]//50)*50 + 1.5,
                           (pygame.mouse.get_pos()[1]//50)*50 + 1.5, 47.5, 47.5))
         prev_x = (pygame.mouse.get_pos()[0]//50)*50 + 1.5
         prev_y = (pygame.mouse.get_pos()[1]//50)*50 + 1.5
   pygame.display.update()
