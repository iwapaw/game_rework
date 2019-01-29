import textwrap
import config
import time


class StoryGameScreen:  # a class that constructs a single instance of the game screen
    # below a dictionary declaration
    # there are seven entries - each one for every line on the game screen
    gameScreenStringDictionary = {'string0': '',
                                  'string1': '',
                                  'string2': '',
                                  'string3': '',
                                  'string4': '',
                                  'string5': '',
                                  'string6': '',
                                  'left': '',
                                  'right': '',
                                  'leftFlag': 0,
                                  'rightFlag': 0}

    currentStoryString = " "
    currentLeftChoice = " "
    currentRightChoice = " "

    string0 = gameScreenStringDictionary['string0']
    string1 = gameScreenStringDictionary['string1']
    string2 = gameScreenStringDictionary['string2']
    string3 = gameScreenStringDictionary['string3']
    string4 = gameScreenStringDictionary['string4']
    string5 = gameScreenStringDictionary['string5']
    string6 = gameScreenStringDictionary['string6']
    left = gameScreenStringDictionary['left']
    right = gameScreenStringDictionary['right']

    def __init__(self, string0, string1, string2, string3, string4, string5, string6, left, right):
        self.string0 = string0
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
        self.string4 = string4
        self.string5 = string5
        self.string6 = string6
        self.left = left
        self.right = right

    @staticmethod
    def current_screen_setter():
        setattr(currentScreen, 'string0', StoryGameScreen.gameScreenStringDictionary.get("string0"))
        setattr(currentScreen, 'string1', StoryGameScreen.gameScreenStringDictionary.get("string1"))
        setattr(currentScreen, 'string2', StoryGameScreen.gameScreenStringDictionary.get("string2"))
        setattr(currentScreen, 'string3', StoryGameScreen.gameScreenStringDictionary.get("string3"))
        setattr(currentScreen, 'string4', StoryGameScreen.gameScreenStringDictionary.get("string4"))
        setattr(currentScreen, 'string5', StoryGameScreen.gameScreenStringDictionary.get("string5"))
        setattr(currentScreen, 'string6', StoryGameScreen.gameScreenStringDictionary.get("string6"))
        setattr(currentScreen, 'left', StoryGameScreen.gameScreenStringDictionary.get("left"))
        setattr(currentScreen, 'right', StoryGameScreen.gameScreenStringDictionary.get("right"))

    @staticmethod
    def current_screen_updater():
        StoryGameScreen.currentScreen = StoryGameScreen(currentScreen.string0,
                                                        currentScreen.string1,
                                                        currentScreen.string2,
                                                        currentScreen.string3,
                                                        currentScreen.string4,
                                                        currentScreen.string5,
                                                        currentScreen.string6,
                                                        currentScreen.left,
                                                        currentScreen.right)
        return StoryGameScreen.currentScreen

    # a function that slices the string into string displayed on one of the seven lines
    @staticmethod
    def stringChopper(stringToChop, leftChoice, rightChoice):
        j = 0  # a counter used to point to a specific entry in the dictionary
        global gameScreenStringDictionary  # accessing the global dictionary - function returns implicitly

        if len(stringToChop) > 95:  # for strings longer than one line
            StoryGameScreen.gameScreenStringDictionary["left"] = leftChoice
            StoryGameScreen.gameScreenStringDictionary["right"] = rightChoice
            choppedStringList = textwrap.wrap(stringToChop, width=95)  # using the text wrap to return list of lines
            for stringLine in choppedStringList:  # assign entries from the generated list to the dictionary
                StoryGameScreen.gameScreenStringDictionary["string{}".format(j)] = stringLine
                j += 1
        elif len(stringToChop) <= 95:  # for short strings just assign to the first dictionary entry
            StoryGameScreen.gameScreenStringDictionary["string0"] = stringToChop
            StoryGameScreen.gameScreenStringDictionary["left"] = leftChoice
            StoryGameScreen.gameScreenStringDictionary["right"] = rightChoice

    @staticmethod
    def dictionaryCleaner():
        global gameScreenStringDictionary
        StoryGameScreen.gameScreenStringDictionary.clear()


chosenLeft = False  # flags for left and rights choices
chosenRight = False
currentStoryKey = "start"  # stores the current key of the story dictionary
currentLeftKey = " "
currentRightKey = " "
currentStoryString = ""  # stores the current story strings
currentLeftChoice = ""
currentRightChoice = ""
storyLog = ['start']  # initializes the story log list
screen = 0


# below the initial story string
StoryGameScreen.currentStoryString = "It's been almost 30 months since Marius left with proconsul Julius Caesar's army. You're looking at the sunset as slaves prepare the house for the night."
StoryGameScreen.currentLeftChoice = "Choose: Keep staring"
StoryGameScreen.currentRightChoice = "Choose: Close eyes"
StoryGameScreen.stringChopper(StoryGameScreen.currentStoryString,
                              StoryGameScreen.currentLeftChoice,
                              StoryGameScreen.currentRightChoice)


currentScreen = StoryGameScreen(  # store the story in the dictionary
                                StoryGameScreen.gameScreenStringDictionary['string0'],
                                StoryGameScreen.gameScreenStringDictionary['string1'],
                                StoryGameScreen.gameScreenStringDictionary['string2'],
                                StoryGameScreen.gameScreenStringDictionary['string3'],
                                StoryGameScreen.gameScreenStringDictionary['string4'],
                                StoryGameScreen.gameScreenStringDictionary['string5'],
                                StoryGameScreen.gameScreenStringDictionary['string6'],
                                StoryGameScreen.gameScreenStringDictionary['left'],
                                StoryGameScreen.gameScreenStringDictionary['right'])


def sendToChopper(string, left, right):  # sends strings to the chopper
    StoryGameScreen.stringChopper(string,
                                  left,
                                  right)


# functions controls the flow of story strings
def takeCurrentStoryString():
        # a nested function that assigns proper story strings to keys
        def dictionarySetter(currentStoryKey, currentLeftKey, currentRightKey):
            global screen
            StoryGameScreen.currentStoryString = storyStringDictionary[currentStoryKey]
            StoryGameScreen.currentLeftChoice = storyStringDictionary[currentLeftKey]
            StoryGameScreen.currentRightChoice = storyStringDictionary[currentRightKey]
            screen += 1

        # ---- declarations ---------------------------------------------------------------------------------------
        global storyStringDictionary
        global currentStoryKey
        global currentLeftKey
        global currentRightKey
        global currentStoryString
        global currentLeftChoice
        global currentRightChoice
        global screen
        # dictionary for the actual story strings
        # each strings in a one story screen
        # strings are represented by Y&Z coordinates
        # storyStringDictionary = {
        #     'x01y00Left': 'left2',
        #     'x01y00Right': 'right2',
        #     'x01y00Story': 'eyes hurt',
        #     'x00y01Story': 'slaves working',
        #     'x00y01Left': 'left3',
        #     'x00y01Right': 'right3'
        # }

        # ---- story strings --------------------------------------------------------------------------------------
        # -- each function tests the current story string and picks a new one accordingly
        if currentStoryKey == 'x01y00Left':
            currentStoryKey = 'x01y00Story'
            currentLeftKey = 'x01y00Left'
            currentRightKey = 'x01y00Right'

        if currentStoryKey == 'x00y01Right':
            currentStoryKey = 'x00y01Story'
            currentLeftKey = 'x00y01Left'
            currentRightKey = 'x00y01Right'

        if currentStoryKey == 'x01y00Story' and screen == 2:
            currentStoryKey = 'x02y00Story'
            currentLeftKey = 'x02y00Right'
            currentRightKey = 'x02y00Right'

        if currentStoryKey == 'x00y01Story' and screen == 2:
            currentStoryKey = 'x00y02Story'
            currentLeftKey = 'x00y02Right'
            currentRightKey = 'x00y02Right'

        dictionarySetter(currentStoryKey, currentLeftKey, currentRightKey)

        if storyLog[len(storyLog) - 1] != currentStoryKey:  # adds to the story log while avoiding duplicates
            storyLog.append(currentStoryKey)


storyStringDictionary = {
    'x01y00Left': 'Ask him in',
    'x01y00Right': 'Go to the gate',
    'x01y00Story': 'Your eyes hurt but you can\'t turn your head away. The pain helps your forget about everything: loneliness, burdens of managing the farm without Marius, due taxes that are meant to be paid with Marius\' war spoils. An old slaves approaches you and says "Lady, there is a centurion at the gate asking to speak with you".',

    'x00y01Story': 'You go back to your memories. Last day before Marius left with the army. He didn\'t let slave clean his armor or tend to his horse. He had spent hours getting ready for the departure. It is easier to wage war than to tell goodbye. An old slaves approaches you and says "Lady, there is a centurion at the gate asking to speak with you".',
    'x00y01Left': 'Ask him in',
    'x00y01Right': 'Go to the gate',

    'x02y00Left': 'Pray to Jupiter',
    'x02y00Right': 'Pray to Mars',
    'x02y00Story': '"Let him into the atrium" - you command - "I will meet him there". Instantly you\'re petrified. Centurion\'s visit could mean one thing: something had happened to Marius. You wait for few moments as you don\'t want to seem desperate. You take a deep breathe and head to the atrium.',

    'x00y02Left': 'Pray to Jupiter',
    'x00y02Right': 'Pray to Mars',
    'x00y02Story': '"Did he say what is the reason of the visit at this time?" - you shout at the slave - "No, my lad. Lord centurion just asked to speak with you" - answers the old man with his eyes pointing to the ground. Your heart is pounding as you know what it means - oficer visiting woman\'s house at this time is to deliver grief news. You rush to the gate',
}


def assignStringsAfterLoad():
    StoryGameScreen.currentStoryString = currentStoryKey
    StoryGameScreen.currentLeftChoice = currentLeftKey
    StoryGameScreen.currentRightChoice = currentRightKey
    StoryGameScreen.stringChopper(StoryGameScreen.currentStoryString,
                                  StoryGameScreen.currentLeftChoice,
                                  StoryGameScreen.currentRightChoice)
