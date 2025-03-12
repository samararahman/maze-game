# Author: Samara Rahman
# Date: May 3, 2023,
# Description: Maze Game 3

import time 
import pygame
pygame.init()

#################### setup and variables ###################

# global variables 
inGame = True
health = 100  #initialize health variable
startTime = time.time()
square_size = 40
playerRow = 0
playerColumn = 0
score = 0
room = []
current_level = 1
pygame.display.set_caption('Samara Maze Game')

# picture variables
mouse = pygame.image.load('mouse.png')
cat = pygame.image.load('cat.png')
door = pygame.image.load('door3.jpeg')
potion = pygame.image.load('potion1.jpeg')
diamond = pygame.image.load('diamond.jpeg')

# audio variables below

# background music
music = pygame.mixer.music.load('background.mp3')
pygame.mixer.music.play(-1) # -1 to play forever

# set up sound effects
coinSound = pygame.mixer.Sound('cash_register.wav')
winSound = pygame.mixer.Sound('clapping.wav')
wallSound = pygame.mixer.Sound('explosion.wav')
doorSound = pygame.mixer.Sound('doorcreak1.wav')
potionSound = pygame.mixer.Sound('ding.wav')
diamondSound = pygame.mixer.Sound('bounce.wav')


# define our colours
LEVEL_COLOUR = (0, 0, 0)
WALL_COLOUR = (242, 185, 234)
SPACE_COLOUR = (255, 255, 255)
GOLD = (246, 228, 168)
PLAYER_COLOUR = (158, 193, 240)
DOORWAY_COLOUR = (208, 122, 91)

# image variables
DEFAULT_IMAGE_SIZE = (square_size, square_size)
gold = pygame.transform.scale(mouse, DEFAULT_IMAGE_SIZE)
cat = pygame.transform.scale(cat, DEFAULT_IMAGE_SIZE)
door = pygame.transform.scale(door, DEFAULT_IMAGE_SIZE)
potion = pygame.transform.scale(potion, DEFAULT_IMAGE_SIZE)
diamond = pygame.transform.scale(diamond, DEFAULT_IMAGE_SIZE)

# design of the room:
level1 = [['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
        ['x', '*', ' ', ' ', 'x', ' ', ' ',' ', ' ',' ','2'],
        ['x', ' ', ' ', ' ', 'x', ' ',' ', ' ',' ', 'x', 'x'],
        ['x', 'x', 'x', ' ', 'x', ' ', ' ', ' ',' ','x', 'x'],
        ['x', ' ', 'x', ' ', ' ',' ', ' ',' ', ' ', ' ', 'x'],
        ['x', 'd', 'x', ' ','*', ' ',' ', 'x', 'x', 'x', 'x'],
        ['x', ' ', 'x', ' ', 'x', ' ','*',' ', ' ', 'p', 'x'],
        ['x', ' ', ' ', ' ', 'x',' ', ' ', 'x', 'x', 'x', 'x'],
        ['x', ' ', 'x', ' ', ' ', ' ', '*',' ', ' ', ' ', 'x'],
        ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]

level2 = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['1', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', '*', ' ', ' ', ' ', ' ', '3'],
    ['x', ' ', '*', 'x', 'x', ' ', '*', 'd', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', '*', 'x'],
    ['x', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', '*', 'x', '*', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', 'x', '*', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', '*', 'x'],
    ['x', 'd', ' ', 'x', ' ', ' ', ' ', 'p', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', 'p', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
]

level3 = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', 'd', ' ', 'x', 'x', ' ', ' ', ' ', 'x', ' ', '*', ' ', ' ', ' ', 'd', ' ', 'x'],
    ['x', 'p', 'x', 'x', 'x', ' ', 'x', 'x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', 'x', ' ', 'x', ' ', 'x'],
    ['x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'p', 'x'],
    ['2', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', '4'],
    ['x', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', ' ', ' ', 'x', 'x', ' ', 'x', 'x', ' ', ' ', 'x'],
    ['x', 'p', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'p', 'x'],
    ['x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', 'x', 'x', 'x', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', '*', ' ', 'x', 'x', 'x', 'x', ' ', 'x', 'x', 'p', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', 'x', 'x', 'x', ' ', '*', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

level4 = [
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
    ['x', ' ', ' ', '*', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'd', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', 'd', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', 'x', 'x', 'x', ' ', ' ', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', 'x'],
    ['x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', 'x'],
    ['x', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', 'x', ' ', ' ', 'p', ' ', 'x', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x'],
    ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '5'],
    ['x', ' ', 'x', ' ', ' ', ' ', ' ', 'x', ' ', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', ' ', ' ', 'x', 'x', 'x', ' ', ' ', ' ', ' ', '*', 'x'],
    ['x', 'x', 'x', 'x', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', 'x', ' ', 'x', 'p', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x', ' ', ' ', ' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
    ['x', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'p', ' ', ' ', ' ', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', '*', 'x', 'x', 'x', 'x', ' ', ' ', 'x', ' ', 'x', ' ', '*', ' ', 'x', 'x', ' ', ' ', ' ', 'x', 'x', 'x', 'x', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '*', ' ', 'x'],
    ['x', ' ', ' ', 'x', 'x', '*', 'x', 'x', 'x', ' ', 'x', ' ', ' ', 'x', 'x', ' ', ' ', 'x', ' ', 'x', 'x', ' ', 'x', ' ', ' ', ' ', ' ', 'x'],
    ['x', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'x'],
    ['x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x']
]

#################### function definitions ###################
def debug_show_room():
    for row in range(len(room)):
        for column in range(len(room[row])):
            print(room[row][column], end=" ")
        print()

#set screen parameters
def set_screen_size(level):
    global screen 
    global height
    global width
    numRows = len(level)
    numColumns = len(level[0])
    (width, height) = (square_size * numColumns, square_size * numRows+square_size)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Samara's Maze Game")

# load a new level map into your room 
def load_level(level, r, c):
    global current_level
    global LEVEL_COLOUR

    if level == level1:
        current_level = 1
        LEVEL_COLOUR = (242, 185, 234)
    elif level == level2:
        current_level = 2
        LEVEL_COLOUR = (117, 207, 255)
    elif level == level3:
        current_level = 3
        LEVEL_COLOUR = (184, 101, 199)      
    elif level == level4:
        current_level = 4
        LEVEL_COLOUR = (91, 186, 162)

    # set the screen size to match the new level
    set_screen_size(level)

    # remove old room
    del room[:]

    # intialize the room with spaces
    numRows = len(level)
    numColumns = len(level[0])
    for i in range(numRows):
        room.append([' '] * numColumns)
    
    # write contents of level into room
    for row in range(len(level)):
        for column in range(len(level[row])):
            room[row][column] = level[row][column]
   
    room[r][c] = 'P'
 
    # debug_show_room() # console area
        
def draw_room():
    global inGame

    # check if time ran out
    fullTime = int(startTime + 200 - time.time())
    if fullTime <= 0:
        inGame = False

    # game over screen
    if score >= 340 or inGame == False:
        winSound.play()
        screen.fill((255, 105, 180))  #pink background
        fontsize = min(width, height) // 15  #adjusting the font size based on screen size
        myFont = pygame.font.SysFont('Comic Sans MS', fontsize)

        textSurface1 = myFont.render('Game Over!', False, (255, 255, 255))
        textSurface2 = myFont.render('Your score: '+str(score), False, (255, 255, 255))
    
        #centering the text
        textRect1 = textSurface1.get_rect()
        textRect2 = textSurface2.get_rect()
        textRect1.center = (width // 2, height // 2 - textRect1.height)
        textRect2.center = (width // 2, height // 2 + textRect2.height)
    
        #displaying the text
        screen.blit(textSurface1, textRect1)
        screen.blit(textSurface2, textRect2)
    
    else:
        screen.fill((0, 0, 255))
        for row in range(len(room)):
            for column in range(len(room[row])):
                rectangle = pygame.Rect(column * square_size, row * square_size, square_size, square_size)
                if room[row][column] == 'x' or room[row][column] == 'h':
                    pygame.draw.rect(screen, LEVEL_COLOUR, rectangle)
                elif room[row][column] == '*':
                    screen.blit(gold, (column * square_size, row * square_size))
                elif room[row][column] == 'P':
                    screen.blit(cat, (column * square_size, row * square_size))
                elif room[row][column] == 'p':
                    screen.blit(potion, (column * square_size, row * square_size))
                elif room[row][column] == 'd':
                    screen.blit(diamond, (column * square_size, row * square_size))
                elif room[row][column] == '1' or room[row][column] == '2' or room[row][column] == '3' or room[row][column] == '4' or room[row][column] == '5':
                    screen.blit(door, (column * square_size, row * square_size))
                else:
                    pygame.draw.rect(screen, SPACE_COLOUR, rectangle)

        # write the current score on the screen
        pygame.font.init()
        myFont = pygame.font.SysFont('Comic Sans MS', 30)
        scoreSurface = myFont.render('score: '+str(score), False, (255, 255, 255))
        screen.blit(scoreSurface, (10, height-square_size))

        #draw the timer
        font = pygame.font.SysFont('Comic Sans MS', 20)  # smaller font for the timer
        showMin = fullTime // 60
        showSec = fullTime % 60
        timeText = font.render('time: ' + str(showMin) + ":" + str(showSec).zfill(2), False, (0, 0, 0))
        screen.blit(timeText, ((width - timeText.get_width() - 10, 10))) #top right corner

        # write the current level on the screen
        level_text_surface = myFont.render('level: '+str(current_level), False, (255, 255, 255))
        screen.blit(level_text_surface, (width-100, height-square_size))
    
        # draw the health value
        health_font = pygame.font.SysFont('Comic Sans MS', 20)  # using smaller font for the health
        health_text = health_font.render('health: ' + str(health), False, (0, 0, 0))
        screen.blit(health_text, (10, 10))  #top left corner

        # check if time ran out
        if fullTime <= 0:
            inGame = False

def locate_player():
    global playerRow
    global playerColumn

    for row in range(len(room)):
        for column in range(len(room[row])):
            if room[row][column] == 'P':
                playerRow = row
                playerColumn = column
                break 

# determine what object is in the direction the player is moving
def get_object(direction):
    if direction == "right":
        return room[playerRow][playerColumn + 1]
    elif direction == "left":
        return room[playerRow][playerColumn - 1]
    elif direction == "up":
        return room[playerRow - 1][playerColumn]
    elif direction == "down":
        return room[playerRow + 1][playerColumn]
    else:
        return 'B'

# move the player
def perform_move(move_type):
    room[playerRow][playerColumn] = ' '
    if move_type == "right":
        room[playerRow][playerColumn + 1] = 'P'
    elif move_type == "left":
        room[playerRow][playerColumn - 1] = 'P'
    elif move_type == "up":
        room[playerRow - 1][playerColumn] = 'P'
    elif move_type == "down":
        room[playerRow + 1][playerColumn] = 'P'

# determine how to handle the keyboard input
def move(direction):
    global inGame
    global score
    # find the player
    locate_player()
    object = get_object(direction)
    if object == '*':
        score += 10
        coinSound.play()
        perform_move(direction)
    if object == ' ':
        perform_move(direction)
    if object == 'p':
        potionSound.play()
        global health
        health+=20 # gain 20 health
        perform_move(direction)
    if object == 'x':
        wallSound.play()
        health-=10 # lose 10 health
        if health <= 0:
            inGame = False
    if object == 'd':
        diamondSound.play()
        score += 15
        perform_move(direction)
    if object == '2':
        doorSound.play()
        perform_move(direction)
        load_level(level2, 1, 1)
    if object == '1':
        doorSound.play()
        perform_move(direction)
        load_level(level1, 1, 6)
    if object == '3':
        doorSound.play()
        perform_move(direction)
        load_level(level3, 6, 1)
    if object == '4':
        doorSound.play()
        perform_move(direction)
        load_level(level4, 6, 6)
    if object == '5':
        doorSound.play()
        perform_move(direction)
        inGame = False
    if score >= 340:
        inGame = False

####################### START OF GAME ########################
debug_show_room()
load_level(level1, 1, 1) # load the first level
while inGame:
    events = pygame.event.get()
    move_ticker = 0

    for event in events:
        if event.type == pygame.QUIT:
            inGame = False
        keys = pygame.key.get_pressed()
        if move_ticker == 0:
            if keys[pygame.K_LEFT]:
                move_ticker = 10
                move("left")
            elif keys[pygame.K_RIGHT]:
                move_ticker = 10
                move("right")
            elif keys[pygame.K_UP]:
                move_ticker = 10
                move("up")
            elif keys[pygame.K_DOWN]:
                move_ticker = 10
                move("down")
    
        if move_ticker > 0:
            move_ticker -= 1
    draw_room()
    pygame.display.update()

if not inGame:
    pygame.time.delay(4000)  #showing the game over screen for 4 seconds

####################### END OF GAME LOOP ########################
pygame.quit()
quit()
   