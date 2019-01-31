import pygame
import sys
import gameScreenClasses
import config
import pickle
from pygame.locals import *

# -- pickle is a module for serialization: https://docs.python.org/3/library/pickle.html
# -- storyStrings and gameScreenClasses are parts of the project


# --------------- TO DO ---------------------------
# -- add information to the info screen
# ---------------------------------- git link
# ---------------------------------- experimental full screen
# ---------------------------------- ..............
# ---------------------------------- add a save feature
# ---------- use the save feature to add functionality to the gear icon?
# -------------------------------------------------

# global variables and initializations -------------------------------------------------------------------------
FPS = 30 # frames per second
WINDOWWIDTH = 1200
WINDOWHEIGHT = 600 # screen resolution for windowed mode
pygame.init()  # initialize
DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT)) # resolution
pygame.display.set_caption('Into the Elysium') # windows title
FPSCLOCK = pygame.time.Clock() # initialize the frame counter
gearIconInUnicode = u"\u2699" # unicode for gear character

chosenLeft = False
chosenRight = False
gameRunning = True
mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
mousePosition = pygame.mouse.get_pos()     # variable to store mouse position

gameMenuFont = pygame.font.Font("fonts\specialelite.ttf", 20)  # font used for menu and settings
titleScreenFont = pygame.font.Font("fonts\changa.ttf", 60)  # font used for the game title
gearIconFont = pygame.font.Font ("fonts\dejavu.ttf",80)

topMenuButtonHeight = WINDOWHEIGHT * 0.3 # for the first button in the main menu
secondMenuButtonHeight = WINDOWHEIGHT * 0.4 # for the second button in the main menu
thirdMenuButtonHeight = WINDOWHEIGHT * 0.5 # for the third button in the main menu
fourthMenuButtonHeight = WINDOWHEIGHT * 0.6 # for the fourth button in the main menu
fullScreenButtonHeight = WINDOWHEIGHT * 0.9 # the location of the fullscreen button in the main menu
fullScreenButtonWidth = WINDOWWIDTH * 0.9 # the location of the fullscreen button in the main menu
halfOfScreenWidth = WINDOWWIDTH / 2  # half of the screen's width (resolution) to calculate the center independently of the resolution
halfOfScreenHeight = WINDOWHEIGHT / 2  # half of the screen's height (resolution) to calculate the center independently of the resolution
bottomRightWidth = WINDOWWIDTH * 0.8  # relative position of the "click..." box
bottomRightHeight = WINDOWHEIGHT * 0.8  # relative position of the "click..." box
bottomLeftWidth = WINDOWWIDTH * 0.2 # position of the info button
bottomLefttHeight = WINDOWHEIGHT * 0.8 # position of the info button

gameButtonHeight = WINDOWHEIGHT / 20 # height of the button in the main menu
gameButtonWidth = WINDOWWIDTH / 5    # width of the button in the main menu
xButtonCoordinateCenterScreen = halfOfScreenWidth-gameButtonWidth/2 # coordinate to center buttons in main menu
gearButtonHeight =  WINDOWHEIGHT / 10
gearButtonWidth = WINDOWWIDTH / 20

xLeftButtonCoordinateGameWindow =  WINDOWWIDTH * 0.2 # the location of the left button in the game window [X]
yLeftButtonCoordinateGameWindow = WINDOWHEIGHT * 0.8 # the location of the left button in the game window [Y]
xRightButtonCoordinateGameWindow = WINDOWWIDTH * 0.6 # the location of the right button in tbe game window [X]
yRightButtonCoordinateGameWindow = WINDOWHEIGHT * 0.8 # the location of the left button in the game window [Y]

xGearButtonCoordinateGameWindow = halfOfScreenWidth-gearButtonWidth/2 # coordinate to center the gear in main menu
yGearButtonCoordinateGameWindow = WINDOWHEIGHT * 0.8 # the location of the gear button in the game window [Y]


# colours                           (R   G    B) ---------------------------------------------------------------
TITLESCREENCOLOUR =                 ( 41,  0,  0)
GAMETITLECOLOUR =                   (235, 90,  0)
BLACK =                             (  0,  0,  0)
GAMETITLECOLOURBRIGHTER =           (235,157,  0)
# --------------------------------------------------------------------------------------------------------------


def gameIntro():  # displays title screen
    intro = True  # flag to execute intro

    while intro:
        for event in pygame.event.get():  # escape key and closing window exits the program
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # ESC exits
                pygame.quit()
                sys.exit()

        mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
        mousePosition = pygame.mouse.get_pos()  # variable to store mouse position

        if mouseClicked[0] == 0:  # if the mouse hadn't been clicked, the title screen will be displayed
            gameTitle = titleScreenFont.render('Into the Elysium',
                                               True,
                                               GAMETITLECOLOUR,
                                               None)  # creates the title object
            gameTitlePosition = gameTitle.get_rect()  # object to position the title on the screen
            gameTitlePosition.center = (halfOfScreenWidth,
                                        halfOfScreenHeight)  # de facto position of the game title
            DISPLAYSURF.fill(TITLESCREENCOLOUR)  # title screen background
            DISPLAYSURF.blit(gameTitle,
                             gameTitlePosition)  # blit the  game title
            pressAnyKey = gameMenuFont.render('Click anywhere to continue',
                                              True,
                                              GAMETITLECOLOUR,
                                              None)  # click to access the main menu and settings
            pressAnyKeyPosition = pressAnyKey.get_rect()  # object to position "click..." box
            pressAnyKeyPosition.center = (bottomRightWidth,
                                          bottomRightHeight) # centers the box
            DISPLAYSURF.blit(pressAnyKey,
                             pressAnyKeyPosition)  # draws "click..." text

        # if the button is clicked and the main menu function is passed, it executes the main function
        if mouseClicked[0] == 1:
            pygame.time.delay(300)
            break

        pygame.display.update() # refreshes the screen
        FPSCLOCK.tick(FPS) # frame counter tick


def infoScreen():
    info = True  # flag to blit the window

    while info:
        for event in pygame.event.get():  # esc and closing windows exits the program
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        mouseClicked = pygame.mouse.get_pressed() # tracks mouse clicks
        mousePosition = pygame.mouse.get_pos() # tracks mouse position

        DISPLAYSURF.fill(TITLESCREENCOLOUR)  # screen background

        infoString0 = gameMenuFont.render('info screen',
                                          True,
                                          GAMETITLECOLOUR,
                                          None)  # info

        infoString0Position = infoString0.get_rect()  # string0 position
        infoString0Position.center = (halfOfScreenWidth,
                                      halfOfScreenHeight / 2)  # centers the box

        DISPLAYSURF.blit(infoString0,
                         infoString0Position)  # blits

        onScreenButton('Back',
                       xButtonCoordinateCenterScreen,
                       yGearButtonCoordinateGameWindow,
                       gameButtonWidth,
                       gameButtonHeight,
                       GAMETITLECOLOUR,
                       GAMETITLECOLOURBRIGHTER,
                       gameMainMenu,
                       gameMainMenu)  # goes back to the main menu

        pygame.display.update()  # refreshes the screen
        FPSCLOCK.tick(FPS)  # frame counter tick


def gameMainMenu(): # main menu and settings
    mainMenu = True # variable that controls the menu loop

    while mainMenu: # main menu loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill(TITLESCREENCOLOUR)

        onScreenButton('Play',  xButtonCoordinateCenterScreen, topMenuButtonHeight, gameButtonWidth, gameButtonHeight,
                       GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER, gameMainMenu,
                       gameWindowMain) # calls the button function - new game
        onScreenButton('Load', xButtonCoordinateCenterScreen, secondMenuButtonHeight, gameButtonWidth, gameButtonHeight,
                       GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER,
                       gameMainMenu, loadGame)  # calls the button function - load game
        onScreenButton('Save', xButtonCoordinateCenterScreen, thirdMenuButtonHeight, gameButtonWidth, gameButtonHeight,
                       GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER,
                       gameMainMenu, saveGame)  # calls the button function - save game
        onScreenButton('Quit', xButtonCoordinateCenterScreen, fourthMenuButtonHeight, gameButtonWidth, gameButtonHeight,
                       GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER,
                       gameMainMenu, quitQameButton)  # calls the button function - quit
        onScreenButton('[FS]', bottomRightWidth, bottomRightHeight, gameButtonWidth/4, gameButtonHeight*1.4,
                       GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER,
                       gameMainMenu, toggleFullScreen)  # calls the button function - go to full screen

        onScreenButton('[I]', bottomLeftWidth, bottomLefttHeight, gameButtonWidth/4, gameButtonHeight*1.4,
                       GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER,
                       gameMainMenu, infoScreen)  # calls the button function - quit

        # optionsButtonGear(xGearButtonCoordinateGameWindow, yGearButtonCoordinateGameWindow, gearButtonWidth,
        #                   gearButtonHeight, GAMETITLECOLOUR, GAMETITLECOLOURBRIGHTER,
        #                   gearResumeFunction)  # shifts between menu and gameplay

        # print(gameScreenClasses.currentStoryKey)
        # print(gameScreenClasses.currentLeftKey)
        # print(gameScreenClasses.currentRightKey)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


def onScreenButton(textOnButton,
                   xButtonCoordinate,
                   yButtonCoordinate,
                   buttonWidth,
                   buttonHeight,
                   initialColour,
                   secondColour,
                   fontUsedForButton,
                   actionInvokedByButton=None):

    mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
    mousePosition = pygame.mouse.get_pos()  # variable to store mouse position

    if xButtonCoordinate + buttonWidth > mousePosition[0] > xButtonCoordinate and \
            yButtonCoordinate + buttonHeight > mousePosition[1] > yButtonCoordinate:  # if the cursor is within the box
        # highlights the button with a brighter colour
        pygame.draw.rect(DISPLAYSURF, secondColour, (xButtonCoordinate,
                                                     yButtonCoordinate,
                                                     buttonWidth,
                                                     buttonHeight))
        # if the button is clicked
        # go to the function passed to onScreenButton with actionInvokedByButton
        if mouseClicked[0] == 1 and actionInvokedByButton != None:
            actionInvokedByButton()

    # if the cursor is outside the button
    # blits a darker colour
    else:
        pygame.draw.rect(DISPLAYSURF, initialColour, (xButtonCoordinate,
                                                      yButtonCoordinate,
                                                      buttonWidth,
                                                      buttonHeight))

    buttonText = gameMenuFont.render(textOnButton,
                                     True,
                                     BLACK,
                                     None)  # creates a text object

    buttonPosition = buttonText.get_rect()  # creates a rect
    buttonPosition.center = (((xButtonCoordinate)+(buttonWidth/2)),
                             ((yButtonCoordinate)+(buttonHeight/2)))  # centers the rect

    DISPLAYSURF.blit(buttonText, buttonPosition)   # blits the object


def goLeftString():  # preparing the data for the next screen after choosing left
    gameScreenClasses.StoryGameScreen.dictionaryCleaner()  # cleans the dict
    # passing strings and choices to the chopper
    gameScreenClasses.StoryGameScreen.stringChopper(gameScreenClasses.StoryGameScreen.currentStoryString,
                                                    gameScreenClasses.StoryGameScreen.currentLeftChoice,
                                                    gameScreenClasses.StoryGameScreen.currentRightChoice)
    # method sets new properties to the current screen instance
    gameScreenClasses.StoryGameScreen.current_screen_setter()
    # to set the second screen properly
    if gameScreenClasses.StoryGameScreen.currentLeftChoice == "Choose: Keep staring":
        gameScreenClasses.currentStoryKey = 'x01y00Left'
    gameScreenClasses.takeCurrentStoryString()
    pygame.time.delay(50)
    config.chosenLeft = True


def goRightString(): # preparing the data for the next screen after choosing right
    gameScreenClasses.StoryGameScreen.dictionaryCleaner()  # cleans the dict
    # passing strings and choices to the chopper
    gameScreenClasses.StoryGameScreen.stringChopper(gameScreenClasses.StoryGameScreen.currentStoryString,
                                                    gameScreenClasses.StoryGameScreen.currentLeftChoice,
                                                    gameScreenClasses.StoryGameScreen.currentRightChoice)
    # method sets new properties to the current screen instance
    gameScreenClasses.StoryGameScreen.current_screen_setter()
    # to set the second screen properly
    if gameScreenClasses.StoryGameScreen.currentRightChoice == "Choose: Close eyes":
        gameScreenClasses.currentStoryKey = 'x00y01Right'
    gameScreenClasses.takeCurrentStoryString()
    pygame.time.delay(50)
    config.chosenRight = True


def saveGame():  # saves the game state - writes contents of the story log into binary file
    with open('game_save.obj', 'wb') as output_file:
        pickle.dump(gameScreenClasses.storyLog, output_file, pickle.HIGHEST_PROTOCOL)
    with open('game_save2.obj', 'wb') as output_file2:
        pickle.dump(gameScreenClasses.currentLeftKey, output_file2, pickle.HIGHEST_PROTOCOL)
    with open('game_save3.obj', 'wb') as output_file3:
        pickle.dump(gameScreenClasses.currentRightKey, output_file3, pickle.HIGHEST_PROTOCOL)


def loadGame():  # loads a previously saved game state
    with open('game_save.obj', 'rb') as input_file:
        gameScreenClasses.storyLog = pickle.load(input_file)
        gameScreenClasses.currentStoryKey = gameScreenClasses.storyLog[len(gameScreenClasses.storyLog) - 1]
    with open('game_save2.obj', 'rb') as input_file2:
        gameScreenClasses.currentLeftKey = pickle.load(input_file2)
    with open('game_save3.obj', 'rb') as input_file3:
        gameScreenClasses.currentRightKey = pickle.load(input_file3)
    gameScreenClasses.assignStringsAfterLoad()
    gameScreenClasses.currentScreen.dictionaryCleaner()
    gameScreenClasses.currentScreen.current_screen_setter()
    goLeftString()
    goRightString()
    gameWindowMain()


# function draws the gear icon
def optionsButtonGear (xButtonCoordinateGear,
                       yButtonCoordinateGear,
                       gearWidth, gearHeight,
                       initialColour,
                       secondColour,
                       actionInvokedByGear=None):

    mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
    mousePosition = pygame.mouse.get_pos()  # variable to store mouse position

    # if the cursor is within the box, highlights the button with a brighter colour
    if xButtonCoordinateGear + gearWidth > mousePosition[0] > xButtonCoordinateGear and \
            yButtonCoordinateGear + gearHeight > mousePosition[1] > yButtonCoordinateGear:
        gearIcon = gearIconFont.render(gearIconInUnicode,
                                       True,
                                       secondColour,
                                       None)  # creates a text object
        gearIconPosition = gearIcon.get_rect()  # creates a rect
        gearIconPosition.center = (((xButtonCoordinateGear) + (gearWidth / 2)),
                                   ((yButtonCoordinateGear) + (gearHeight / 2)))  # centers the rect
        DISPLAYSURF.blit(gearIcon,
                         gearIconPosition)  # blits the object
        if mouseClicked[0] == 1 and actionInvokedByGear != None:    # if the button is clicked
                actionInvokedByGear()  # go to the function passed to onScreenButton witb actionInvokedByButton

    else:                                    # if the cursor is outside the button
        gearIcon = gearIconFont.render(gearIconInUnicode,
                                       True,
                                       initialColour,
                                       None)  # creates a text object
        gearIconPosition = gearIcon.get_rect()  # creates a rect
        gearIconPosition.center = (((xButtonCoordinateGear) + (gearWidth / 2)),
                                   ((yButtonCoordinateGear) + (gearHeight / 2)))  # centers the rect

        DISPLAYSURF.blit(gearIcon, gearIconPosition)  # blits the object


# main game window
def gameWindowMain():  # function to blit the game flow
    global gameRunning
    gameRunning = True  # variable the controls the game flow
    global chosenRight
    global chosenLeft

    while gameRunning:  # game loop running as long as not quit or back to menu
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # ESC exits
                pygame.quit()
                sys.exit()

        mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
        mousePosition = pygame.mouse.get_pos()  # variable to store mouse position

        DISPLAYSURF.fill(TITLESCREENCOLOUR)

        # strings to display are passed from gameScreenClasses file
        xLineCoordinate = 100  # position from left to x
        yLineCoordinate = 50  # posistion from top to y

        lines = [gameScreenClasses.currentScreen.string0,
                 gameScreenClasses.currentScreen.string1,
                 gameScreenClasses.currentScreen.string2,
                 gameScreenClasses.currentScreen.string3,
                 gameScreenClasses.currentScreen.string4,
                 gameScreenClasses.currentScreen.string5,
                 gameScreenClasses.currentScreen.string6]  # 95 characters per line

        for line in lines:  # for loop to display consecutive lines
            line = gameMenuFont.render(line,
                                       True,
                                       GAMETITLECOLOUR,
                                       None)  # render a line from "lines" array
            linePosition = line.get_rect()  # creates the object line
            linePosition.topleft = (xLineCoordinate,
                                    yLineCoordinate)  # centers the line from topleft to passed x and y
            DISPLAYSURF.blit(line,
                             linePosition)  # prints the game surface
            yLineCoordinate += 35  # goes to the new line

        # each button should have 12 characters
        # choices on buttons are passed from gameScreenClasses file
        onScreenButton(gameScreenClasses.currentScreen.left,
                        xLeftButtonCoordinateGameWindow,
                        yLeftButtonCoordinateGameWindow,
                        gameButtonWidth,
                        gameButtonHeight,
                        GAMETITLECOLOUR,
                        GAMETITLECOLOURBRIGHTER,
                        gameMainMenu,
                        goLeftString) # button for the left choice

        onScreenButton(gameScreenClasses.currentScreen.right,
                       xRightButtonCoordinateGameWindow,
                       yRightButtonCoordinateGameWindow,
                       gameButtonWidth,gameButtonHeight,
                       GAMETITLECOLOUR,
                       GAMETITLECOLOURBRIGHTER,
                       gameMainMenu,
                       goRightString)  # button for the right choice

        optionsButtonGear(xGearButtonCoordinateGameWindow,
                            yGearButtonCoordinateGameWindow,
                            gearButtonWidth,
                            gearButtonHeight,
                            GAMETITLECOLOUR,
                            GAMETITLECOLOURBRIGHTER,
                            gearPauseFunction)  # shifts between menu and gameplay

        # print(gameScreenClasses.currentStoryKey)
        # print(gameScreenClasses.currentLeftKey)
        # print(gameScreenClasses.currentRightKey)

        pygame.display.update()
        FPSCLOCK.tick(FPS)


def gearPauseFunction():
    global gameRunning
    gameRunning = False


def gearResumeFunction():
    global gameRunning
    gameRunning = True


def quitQameButton(): # function quits the game
    quit = True  # flag to execute the quit screen

    while quit:
        for event in pygame.event.get(): # esc key quits
            if event.type == pygame.QUIT or (event.type == KEYUP and event.key == K_ESCAPE):  # ESC exits
                pygame.quit()
                sys.exit()

        mouseClicked = pygame.mouse.get_pressed()  # variable to store mouse clicks
        mousePosition = pygame.mouse.get_pos()  # variable to store mouse position
        DISPLAYSURF.fill(TITLESCREENCOLOUR)  # background colour

        quitGamePrompt = gameMenuFont.render('Would you like to quit the game?',
                                             True,
                                             GAMETITLECOLOUR,
                                             None)  # prompt

        quitGamePromptPosition = quitGamePrompt.get_rect()  # object to position "click..." box

        quitGamePromptPosition.center = (halfOfScreenWidth,
                                         halfOfScreenHeight/2)  # centers the box

        DISPLAYSURF.blit(quitGamePrompt,
                         quitGamePromptPosition)  # draws "click..." text

        onScreenButton("Yes",
                        xLeftButtonCoordinateGameWindow,
                        yLeftButtonCoordinateGameWindow,
                        gameButtonWidth,
                        gameButtonHeight,
                        GAMETITLECOLOUR,
                        GAMETITLECOLOURBRIGHTER,
                        gameMainMenu,
                        quitGameAction) # button for the left choice

        onScreenButton("No",
                       xRightButtonCoordinateGameWindow,
                       yRightButtonCoordinateGameWindow,
                       gameButtonWidth,
                       gameButtonHeight,
                       GAMETITLECOLOUR,
                       GAMETITLECOLOURBRIGHTER,
                       gameMainMenu,
                       gameMainMenu)  # button for the right choice


        pygame.display.update()  # refreshes the screen
        FPSCLOCK.tick(FPS)  # frame counter tick


def quitGameAction():
    pygame.quit()
    sys.exit()


def toggleFullScreen(): # function goes full screen
    DISPLAYSURF = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)


def main():
    global FPSCLOCK, DISPLAYSURF  # global declaration of frame counter and display surface object

    while True:  # main game loop
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE): # x and ESC exits
                pygame.quit()
                sys.exit()

        gameIntro()
        if gameRunning:
            gameMainMenu()
        else:
            gameWindowMain()
        # gameMainMenu()

        pygame.display.update() # refreshes the screen
        FPSCLOCK.tick(FPS) # frame counter tick


if __name__ == '__main__': main()

