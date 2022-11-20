from turtle import pos
import pygame
import buttonMenu
import main_AND_test.Graph as Graph
import PreLoadedGraphs as preloadedOptions
import CreateNewGraph as drawGraph

global possibleNames 
possibleNames = ['A', 'B', 'C', 'D', 'E', 'F', 'G' , 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

global nameIndex
nameIndex = 0

global vertexLocations
vertexLocations = {}

global graph

pygame.init()

gameGraph = Graph(2)

#create game window
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Main Menu")

#game variables
game_paused = False
menu_state = "main"

#define fonts
font = pygame.font.SysFont("arialblack", 40)

#define colours
TEXT_COL = (255, 255, 255)

#load button images
resume_img = pygame.image.load("images/button_resume.png").convert_alpha()
options_img = pygame.image.load("images/button_options.png").convert_alpha()
quit_img = pygame.image.load("images/button_quit.png").convert_alpha()
video_img = pygame.image.load('images/button_video.png').convert_alpha()
audio_img = pygame.image.load('images/button_audio.png').convert_alpha()
keys_img = pygame.image.load('images/button_keys.png').convert_alpha()
back_img = pygame.image.load('images/button_back.png').convert_alpha()
choosePresetGraph_img = pygame.image.load('images/ChoosePresetGraph.png').convert_alpha()
createNewGraph_img = pygame.image.load('images/CreateNewGraph.png').convert_alpha()


#create menu button instances
resume_button = buttonMenu.Button(304, 125, resume_img, 1)
options_button = buttonMenu.Button(297, 250, options_img, 1)
quit_button = buttonMenu.Button(336, 375, quit_img, 1)
video_button = buttonMenu.Button(226, 75, video_img, 1)
audio_button = buttonMenu.Button(225, 200, audio_img, 1)
keys_button = buttonMenu.Button(246, 325, keys_img, 1)
back_button = buttonMenu.Button(332, 450, back_img, 1)

#create setup buttons
choosePresetGraph_button = buttonMenu.Button(304, 125, choosePresetGraph_img, 1)
createNewGraph = buttonMenu.Button(297, 250, createNewGraph_img, 1)


def getNextVertexName():
  global nameIndex
  global possibleNames
  nextName = ''
  if nameIndex > len(possibleNames) - 1:
    nameIndex+=1
    nextName = possibleNames[nameIndex]
  else:
    print("No Names Available")
  return nextName

def draw_text(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

def drawEdge(fromVertex, toVertex):
  pass

def drawVertex():
  #draw the drawEdge on the screen 
  nameOfVertex = getNextVertexName()
  gameGraph.addVertex(nameOfVertex)
  pass

def chooseDrawGraph():
  pass

def choosePreLoadedGraph(buttonChoice):
  global gameGraph
  gameGraph = preloadedOptions.chooseOption(buttonChoice)

def gameSetupMenu():
  pass

def startGame():
  '''GAME LOOP'''
  run = True
  while run:
    screen.fill((52, 78, 91))

    #check if game is paused
    gameSetupMenu()

    if game_paused == True:
      #check menu state
      if menu_state == "main":
        #draw pause screen buttons
        if resume_button.draw(screen):
          game_paused = False
        if options_button.draw(screen):
          menu_state = "options"
        if quit_button.draw(screen):
          run = False
      #check if the options menu is open
      if menu_state == "options":
        #draw the different options buttons
        if video_button.draw(screen):
          print("Video Settings")
        if audio_button.draw(screen):
          print("Audio Settings")
        if keys_button.draw(screen):
          print("Change Key Bindings")
        if back_button.draw(screen):
          menu_state = "main"
    else:
      draw_text("Press SPACE to pause", font, TEXT_COL, 160, 250)

    #event handler
    for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
          game_paused = True
      if event.type == pygame.QUIT:
        run = False

    pygame.display.update()


pygame.quit()