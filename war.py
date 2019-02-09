import random
""" Welcome to the Card Game of War!
Rules:
1. Based on the number of players, the 52 cards of the deck will be
distributed evenly among all players.
2. For each round, each player will show one card. Whoever has the
highest valued card will sweep all cards, including their own.
3. When a player has all 52 cards, they win and the game ends. """
## a dictionary that defines id for each suit
suit_id_dict = {"spade":0, "heart":1, "diamond":2, "club":3}
######################################################################
##
"""Class Card:
  Purpose: Implementation of card
  Functions:
   cardDescription(): returns a list contains suit and value"""
######################################################################
##
class Card(object):
    ## constructor
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        self.id = suit_id_dict[self.suit]*13 + self.value
    ## cardDescription(): returns a list contains suit and value
    def cardDescription(self):
        return [self.suit, self.value]
######################################################################
##
"""class Person:
 Purpose: Implement a person
 Functions:
   getName(): returns the person's name"""
######################################################################
##
class Person:
    ## constructor
    def __init__(self, name):
        self.name = name
    def getName(self):
        return self.name
 ######################################################################
##
""" class Player:
  Purpose: Implement a player in a war game
  Functions:
    getCard(cards): player receives cards
    play(): player plays a card
    shuffle(): player shuffles cards at hand
    report(): prints out info of cards at hand"""
######################################################################
##
class Player(Person):
    ## constructor
    def __init__(self, name):
        Person.__init__(self, name)
        self.cards = []
    ## getCard(cards): player receives cards
    def getCard(self, cards):
        self.cards = self.cards + cards
    ## play(): player plays a card
    def play(self):
        c = self.cards[0]
        self.cards.pop(0)
        return c
    ## shuffle(): player shuffles cards at hand
    def shuffle(self):
        random.shuffle(self.cards)
    ## report(): prints out info of cards at hand
    def report(self):
        print("    " + self.name + " has " + str(len(self.cards)) + "cards")
######################################################################
##
""" Class CardDeck:
  Purpose: Implement a deck of cards
  Function:
    shuffle(): Shuffles all cards
    deal(numCards): Returns numCards of cards
    dealAll(players, numCards): Deal numCards of cards to each
player"""
######################################################################
##
class CardDeck:

     ## constructor
    def __init__ (self, numDecks=1):
        # implement later for multiple decks
        #self.stack = list(range(1, numCards+1))
        self.stack = []
        for i in range(0, numDecks):
            for suit in list(suit_id_dict.keys()):
                for val in range(1, 14):
                    self.stack.append(Card(suit, val))
    ## shuffle(): Shuffles all cards
    def shuffle(self):
        random.shuffle(self.stack)
    ## deal(numCards): Returns numCards of cards
    def deal(self, numCards):
        #for i in range (0, amount):
        dealCards = self.stack[0:numCards]
        self.stack = self.stack[numCards:]
        return dealCards
    ## dealAll(players, numCards): Deal numCards of cards to each
#player
def dealAll(self, players, numCards):
        while 1:
            for player in players:
                player.getCard(self.deal(numCards))
                if not self.stack:
                    return
######################################################################
###########
""" class WarGame
  Purpose: Implements the actions in a war game
  Functions:
    addPlayer(playerNameList): creates and adds players based on the
names list
    addPlayer(playerName): creates and adds one player based on
playerName
    initCards(): create a card deck
    shuffleCards(): shuffles all cards
    dealCards(): deals all cards to all players
    play(): plays the war game
    status(): prints out information of the game
    status(players): prints out information of the specified
players"""
######################################################################
###########

class WarGame:
    ## constructor
    def __init__(self):
        self.players = []
        self.cards = []
        self.numCardToDealAtOneTime = 1
    ## addPlayer(playerNameList): creates and adds players based on
#playerNameList
def addPlayers(self, playerNameList):
        for x in playerNameList:
            self.players.append(Player(x))
    ## addPlayer(playerName): creates and adds one player based on
#playerName
def addPlayer(self, playerName):
        self.players.append(Player(playerName))
    ## initCards(): create a card deck
def initCards(self, numDecks=1):
        self.cards = CardDeck(numDecks)
    ## shuffleCards(): shuffles all cards
def shuffleCards(self):
        self.cards.shuffle()
    ## dealCards(): deals all cards to all players
def dealCards(self, numDecks=1):
        self.cards.dealAll(self.players, self.numCardToDealAtOneTime)
    ## play(): plays the war game
def play(self):
        remainingPlayers = self.players
        playedCards = []
        global input
        ## play until only one player remains
        while len(remainingPlayers) != 1:
            ## pause when a player lost and leaves the game
            lostPlayers = list(filter(lambda x: len(x.cards)==0,remainingPlayers))
            if len(lostPlayers)>0:
                self.status(remainingPlayers)
                input(lostPlayers[0].name + " lost! Press Enter to continue ...\n")



## find remaining players (filter out players with no card at hand)
remainingPlayers = list(filter(lambda x: x.cards,remainingPlayers))
            ## print out status for this round
self.status(remainingPlayers)
            ## gather played cards from the players
playedCards.extend(list(map(lambda x: x.play(),
remainingPlayers)))
            ## get a list of card values on the table
cardValues = list(map(lambda x: x.id, playedCards))
            ## find out the card with largest value
maxCardValue = max(cardValues)
            ## find out if there is tie (multiple cards with the largest value)

## if so, continue playing without collecting the cars
## played are left on the table for the next winner to collect
if cardValues.count(maxCardValue) == 1:
    ## find out which player played the winning card
    winnerIndex = cardValues.index(maxCardValue)
    winner = remainingPlayers[winnerIndex]
    ## winner collects all the cards on the table
    winner.getCard(playedCards)
    playedCards = []
    ## winner shuffles cards at hand to increase
    random.shuffle(winner.cards)
else:
    input("There is a tie! Press Enter to continue ...\n")
#randomness
print("    !!! " + remainingPlayers[0].name + " wins !!!\n")
## status(): prints out information of the game
def status(self):
    for x in self.players:
        x.report()
print("")

## status(): prints out information of the specified players
def status(self, players):
        for x in players:
            x.report()
print("")
######################################################################
###########
#Main Program
######################################################################
###########
player_names = ["Player A", "Player B", "Player C", "Player D"]
game = WarGame()
game.addPlayers(player_names)
game.initCards()
game.shuffleCards()
game.dealCards()
game.play()
