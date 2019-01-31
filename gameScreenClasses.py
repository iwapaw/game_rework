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
            currentLeftKey = 'x02y00Left'
            currentRightKey = 'x02y00Right'

        if currentStoryKey == 'x00y01Story' and screen == 2:
            currentStoryKey = 'x00y02Story'
            currentLeftKey = 'x00y02Left'
            currentRightKey = 'x00y02Right'

        if currentStoryKey == 'x02y00Story' and screen == 3:
            currentStoryKey = 'x03y00Story'
            currentLeftKey = 'x03y00Left'
            currentRightKey = 'x03y00Right'

        if currentStoryKey == 'x00y02Story' and screen == 3:
            currentStoryKey = 'x00y03Story'
            currentLeftKey = 'x00y03Left'
            currentRightKey = 'x00y03Right'

        if currentStoryKey == 'x03y00Story' and screen == 4:
            currentStoryKey = 'x04y00Story'  # first ending
            currentLeftKey = 'x04y00Left'
            currentRightKey = 'x04y00Right'

        if currentStoryKey == 'x00y03Story' and screen == 4:
            currentStoryKey = 'x00y04Story'
            currentLeftKey = 'x00y04Left'
            currentRightKey = 'x00y04Right'

        if currentStoryKey == 'x00y04Story' and screen == 5:
            currentStoryKey = 'x05y00Story'
            currentLeftKey = 'x05y00Left'
            currentRightKey = 'x05y00Right'
            config.chosenLeft = False

        if currentStoryKey == 'x00y04Story' and screen == 5:
            currentStoryKey = 'x00y05Story'
            currentLeftKey = 'x00y05Left'
            currentRightKey = 'x00y05Right'
            config.chosenRight = False

        if (currentStoryKey == 'x00y05Story' or currentStoryKey == 'x05y00Story') and screen == 6:
            currentStoryKey = 'x06y00Story'
            currentLeftKey = 'x06y00Left'
            currentRightKey = 'x06y00Right'

        if currentStoryKey == 'x06y00Story' and screen == 7:
            currentStoryKey = 'x07y00Story'
            currentLeftKey = 'x07y00Left'
            currentRightKey = 'x07y00Right'

        if currentStoryKey == 'x07y00Story' and screen == 8:
            currentStoryKey = 'x08y00Story'
            currentLeftKey = 'x08y00Left'
            currentRightKey = 'x08y00Right'

        if currentStoryKey == 'x08y00Story' and screen == 9 and config.chosenLeft == True:
            currentStoryKey = 'x09y00Story'  # second ending
            currentLeftKey = 'x09y00Left'
            currentRightKey = 'x09y00Right'
            config.chosenLeft = False

        if currentStoryKey == 'x08y00Story' and screen == 9 and config.chosenRight == True:
            currentStoryKey = 'x00y09Story'
            currentLeftKey = 'x00y09Left'
            currentRightKey = 'x00y09Right'
            config.chosenLeft = False

        config.chosenLeft = False
        config.chosenRight = False

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
    'x02y00Story': '"Let him into the atrium" - you command - "I will meet him there". Instantly you\'re petrified. You had felt it: god\'s laughter trembling in the distance. Centurion\'s visit could mean one thing: something had happened to Marius. You wait for few moments as you don\'t want to seem desperate. You take a deep breathe and head to the atrium.',

    'x00y02Left': 'Pray to Jupiter',
    'x00y02Right': 'Pray to Mars',
    'x00y02Story': '"Did he say what is the reason of the visit at this time?" - you shout at the slave - "No, my lady. Lord centurion just asked to speak with you" - answers the old man with his eyes pointing to the ground. Your heart is pounding as you know what it means - oficer visiting woman\'s house at this time is to deliver grief news. You rush to the gate',

    'x03y00Left': 'May be the god\'s will',
    'x03y00Right': 'May be the god\'s will',
    'x03y00Story': 'You\'re managing to keep a straight face as you enter the atrium. Centurion is standing with his arms crossed looking at the house altar. He is dirty, he\'s legs are covered in mud, he seems tired as he clearly spent weeks on a horseback. Centurions\'s posture gets dignified and muscles tight when he notices you. Your eyes meet. "I am sorry, my lady" - he says - "for interrupting at this late time. I come to deliver the sad news. Centurion Marius had choined our brave heroes in Elysium when serving under great Consul Julius. Hail to hero Marius!" - he shouts. After a moment Centurion adds quietely - "I am sorry, my lady"',

    'x00y03Left': 'NO!!!',
    'x00y03Right': 'STOP!',
    'x00y03Story': 'Your robe is waving as you run to the household gate. Centurion is leaning against the stone wall while your slaves give food and water to his tired horse. He is dirty, he\'s legs are covered in mud, he seems tired as he clearly spent weeks on a horseback. Centurions\'s posture gets dignified and muscles tight when he notices you. Your eyes meet. "I am sorry, my lady" - he says - "for interrupting at this late time. I come to deliver the sad news. Centurion Marius had choined our brave heroes in Elysium when serving under great Consul Julius. Hail to hero Marius!" - he shouts. After a moment Centurion adds quietely - "I am sorry, my lady"',

    # first ending
    'x04y00Left': 'May be the god\'s will',
    'x04y00Right': 'May be the god\'s will',
    'x04y00Story': 'Marius\' body was never recovered. After the funeral ceremony Senate had paid honors to your brave husband and for a long time tales of his bravery were told by folks. You had lived a long file, farm and house had prospered under your wise hands. The rest of your life was lonely, though. You were never able to find peace. But what else could you do? And so may be the god\'s will',

    'x00y04Left': 'Threaten the gods',
    'x00y04Right': 'Stab yourself',
    'x00y04Story': 'Centurion is shocked by your outbreak - "I am sorry for your loss, my lady but please, do not spoil your husbands heroic name!" - he shouts. You are not listenning to this nonsens, you will not be gods\' toy. In fury you wrench Centurion\'s sword from a slave\'s hand and...',

    'x05y00Left': '...',
    'x05y00Right': '...',
    'x05y00Story': '"I will not let you take my husband away!" - you scream to the setting sun with the sword in your hand. - "I defy you, I defy you with your laws and games! Give me back my husband or I will hunt you down and make you pay for what you had done!" - you yell as the darknest clenches you.',

    'x00y05Left': '...',
    'x00y05Right': '...',
    'x00y05Story': '"I will not let you take my husband away!" - you scream to the setting sun with the sword in your hand. - "I command you to take me to my husband! I will rip him out of your claws!" - you scream as you press the sword firmly against your chest.',

    'x06y00Left': 'Who...',
    'x06y00Right': 'Where...',
    'x06y00Story': 'You wake up in a complete darkness and feel wet, cold stone beneath. You cannot hear or smell anything. Before you are able to gather your thoughts a giant, glowing spectre appears in front of you and you here its voice - "Quite a show out there"- it says.',

    'x00y06Left': '...',
    'x00y06Right': '...',
    'x00y06Story': '',

    'x07y00Left': 'Wait!',
    'x07y00Right': 'Am I...',
    'x07y00Story': '"No, no, no. We have just met and there are already too many questions" - you can sens the irritation in its voice. - "I will give you the basics around here. My name is Uf, simply Uf. Your name is inrelevant. You thouht you could challenge the gods and here you are. Uf will be your guide throught the misery" - said the specter and disappeared.',

    'x00y07Left': '...',
    'x00y07Right': '...',
    'x00y07Story': '',

    'x08y00Left': 'Wait for Uf',
    'x08y00Right': 'Just go',
    'x08y00Story': 'Once again your are left in the darkness. You check your pulse but you can\'t feel anything. You do not feel like being dead, however, you are not certain how being dead feels. You wait for a brief moment, wet stone beneath you does not get warmer but you are almost sure you can feel your own weight and body. What you will do?',

    'x00y08Left': '...',
    'x00y08Right': '...',
    'x00y08Story': '',

    # second ending
    'x09y00Left': 'A little bit longer',
    'x09y00Right': 'Just a moment',
    'x09y00Story': 'You wait for Uf to come back. Surely, it will be back any moment. You think about your farm and slaves, they need attention and guidance. You hope that Marius will step out of the darkness, grab your hand and take you back home.',

    'x00y09Left': 'Call Uf',
    'x00y09Right': 'Call Marius',
    'x00y09Story': 'You slow stand up in the darkness and focus to catch some sound or smell that might help you understand the surroundings. There is nothing no matter how hard you try. Nothing apart from the wet stone on the ground. But for some reason you feel like you cannot stay here.',
}


def assignStringsAfterLoad():
    StoryGameScreen.currentStoryString = currentStoryKey
    StoryGameScreen.currentLeftChoice = currentLeftKey
    StoryGameScreen.currentRightChoice = currentRightKey
    StoryGameScreen.stringChopper(StoryGameScreen.currentStoryString,
                                  StoryGameScreen.currentLeftChoice,
                                  StoryGameScreen.currentRightChoice)
