import random
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__ (self, name):
        self.name = name
        self.prizeMoney = 0
        self.prizes = []
    def addMoney(self, amt = 0):
        self.prizeMoney += amt
    def goBankrupt(self):
        self.prizeMoney = 0
    def addPrize(self,prize):
        self.prizes.append(prize)
    def __str__(self):
        return "{} (${})".format(self.name, self.prizeMoney)
# Write the WOFHumanPlayer class definition (part B) here
class WOFHumanPlayer(WOFPlayer):
    def getMove(category, obscuredPhrase, guessed): 
        return input("Guess a letter, phrase, or type 'exit' or 'pass': ")
# Write the WOFComputerPlayer class definition (part C) here

class WOFComputerPlayer(WOFPlayer):
    def __init__(self, name, difficulty):
        self.difficulty = difficulty
        WOFPlayer.__init__(self, name)
        
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'
    def smartCoinFlip(self):
        randomnum = random.randint(1,10)
        if randomnum <= self.difficulty:
            return True
        else: 
            return False
    def getPossibleLetters(self, guessed): 
        listy = [x for x in LETTERS if x not in guessed]
        listy = [x for x in self.SORTED_FREQUENCIES if x in listy]
        if self.prizeMoney < VOWEL_COST:
            listy = [x for x in listy if x not in list(VOWELS)]
            return listy
        else:
            return listy
     
    def getMove(self,category, obscuredPhrase, guessed):
        possibleLetters = self.getPossibleLetters(guessed)
        print("guessed", guessed)
        print("possible : ", possibleLetters)
        print("problemo" ,[x for x in possibleLetters if x in guessed])
        flip = self.smartCoinFlip()
        if len(possibleLetters) == 0:
            return "pass"
        elif flip == True:
            flipTrue = self.possibleLetters[-1]
            print("flip {}, return : {}".format(flip, flipTrue))
            return flipTrue
        elif flip == False:
            flipFalse = random.choice(possibleLetters)
            print("flip {} return {}".format(flip, flipFalse))
            return flipFalse
        