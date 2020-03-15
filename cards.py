# Play Your Cards Right
# Write a class that simulates a standard 52-card deck of playing cards. It must have methods for shuffling the cards and drawing cards from the deck. The shuffle method should randomly shuffle the cards. The draw method should return a given number of cards, removing them from the deck.
# Bonus challenges:
# - Make it work for multiple combined decks
# - Make it work for arbitrary card types and numbers of cards

import numpy as np
import math

class cards:

  def __init__(self, decks=1, suits=4, decksize=52):
    self.deck = []
    self.decks = decks
    self.suits = suits
    self.decksize = decksize

    for i in range(self.decksize*self.decks):
      self.deck.append(i)

  def shuffle(self):
    newdeck = []
    remaining = len(self.deck)
    cards = len(self.deck)

    for i in range(cards):
      card = np.random.randint(0, remaining)
      newdeck.append(self.deck[card])
      self.deck.remove(self.deck[card])
      remaining = remaining - 1
    
    self.deck = newdeck

  def draw(self, number):
    drawn = []

    for i in range(number):
      drawn.append(self.deck[0])
      self.deck.remove(self.deck[0])
    
    return(drawn)

  def showdeck(self):
    print(self.deck)

  def getcard(self, check):
    card = (int)(check % (self.decksize / self.suits) + 1)
    suit = math.floor(check/(self.decksize / self.suits)) + 1

    print("{0} of suit {1}".format(card, suit))
