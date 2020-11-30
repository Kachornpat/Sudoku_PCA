import pygame
import sys

pygame.init()

#set window
screen = pygame.display.set_mode((800, 550))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

enable_row = 0
enable_column = 0
enable = False

value = ""
font = pygame.font.SysFont("Ariel.ttf", 50)
number = None

#build white screen
screen.fill(white)


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
      if enable == False:
         #enable box
         if pygame.mouse.get_pos()[0] > 50 and pygame.mouse.get_pos()[0] < 500 and pygame.mouse.get_pos()[1] > 50 and pygame.mouse.get_pos()[1] < 500:
            pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
            pygame.draw.rect(screen,(225, 225, 225),
                             ((pygame.mouse.get_pos()[0]//50)*50 + 2,
                              (pygame.mouse.get_pos()[1]//50)*50 + 2, 46, 46))
            enable_row = (pygame.mouse.get_pos()[0]//50)
            enable_column = (pygame.mouse.get_pos()[1]//50)
            enable = True
      elif enable == True:
         # unable box
         if enable_row == pygame.mouse.get_pos()[0]//50 and enable_column == pygame.mouse.get_pos()[1]//50:
            pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
            enable = False
         # enable another box
         else:
            pygame.draw.rect(screen, white, (enable_row*50 + 2, enable_column*50 + 2, 46, 46))
            if number != None and sudoku[enable_column-1][enable_row-1] != 0:
               number = font.render(f"{sudoku[enable_column-1][enable_row-1]}", True, black)
               screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
            pygame.draw.rect(screen,(225, 225, 225),
                             ((pygame.mouse.get_pos()[0]//50)*50 + 2,
                              (pygame.mouse.get_pos()[1]//50)*50 + 2, 46, 46))
            enable_row = (pygame.mouse.get_pos()[0]//50)
            enable_column = (pygame.mouse.get_pos()[1]//50)
         
      pygame.display.update()
      pygame.time.wait(300)
      
   if enable == True:
      if pygame.key.get_pressed()[pygame.K_KP1] or pygame.key.get_pressed()[pygame.K_1]:
         number = font.render("1", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 1
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
             
      elif pygame.key.get_pressed()[pygame.K_KP2] or pygame.key.get_pressed()[pygame.K_2]:
         number = font.render("2", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 2
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP3] or pygame.key.get_pressed()[pygame.K_3]:
         number = font.render("3", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 3
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP4] or pygame.key.get_pressed()[pygame.K_4]:
         number = font.render("4", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 4
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP5] or pygame.key.get_pressed()[pygame.K_5]:
         number = font.render("5", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 5
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP6] or pygame.key.get_pressed()[pygame.K_6]:
         number = font.render("6", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 6
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP7] or pygame.key.get_pressed()[pygame.K_7]:
         number = font.render("7", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 7
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP8] or pygame.key.get_pressed()[pygame.K_8]:
         number = font.render("8", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 8
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
      elif pygame.key.get_pressed()[pygame.K_KP9] or pygame.key.get_pressed()[pygame.K_9]:
         number = font.render("9", True, black)
         screen.blit(number, (enable_row*50 + 15, enable_column*50 + 10))
         sudoku[enable_column - 1][enable_row - 1] = 9
         print(sudoku)
         pygame.display.update()
         pygame.time.wait(300)
         
   
