import textwrap


class StoryGameScreen:  # a class that constructs a single instance of the game screen
    # below a dictionary declaration
    # there are seven entries - each one for every line on the game screen
    gameScreenStringDictionary = {'string0': '', 'string1': '', 'string2': '', 'string3': '', 'string4': '',
                                  'string5': '',
                                  'string6': '', 'left': '', 'right': ''}

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

    @staticmethod
    def stringChopper(stringToChop, leftChoice, rightChoice):  # a function that slices the string into string displayed on one of the seven lines
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



currentScreen = StoryGameScreen(
                StoryGameScreen.string0,
                StoryGameScreen.string1,
                StoryGameScreen.string2,
                StoryGameScreen.string3,
                StoryGameScreen.string4,
                StoryGameScreen.string5,
                StoryGameScreen.string6,
                StoryGameScreen.left,
                StoryGameScreen.right)


StoryGameScreen.currentStoryString = "It's been almost 30 months since Marius left with proconsul Julius Caesar army's. You're looking at the sunset as slaves prepare the house for the night."
StoryGameScreen.currentLeftChoice = "Keep staring"
StoryGameScreen.currentRightChoice = "Close your eyes"
StoryGameScreen.stringChopper(StoryGameScreen.currentStoryString,
                              StoryGameScreen.currentLeftChoice,
                              StoryGameScreen.currentRightChoice)
