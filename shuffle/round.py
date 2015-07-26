#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

class Round:
  
  def __init__(self, pot):
    super().__init__()
    
    # careful about negative pots
    if pot < 0:
      raise Exception("A round can't have a negative pot")
    self._pot = pot
  
  @property
  def pot(self):
    return self._pot
    
  @pot.setter
  def pot(self, value):
    raise Exception("A round's pot can't be changed")
    
    self._pot = value
  
  # compute odds of winning in a [0..1] range
  def odds(self, bet):
    try:
      odds = abs(bet.amount) / (bet.amount + self.pot)
      
      # careful about bogus bets
      return max(0.0, min(1.0, odds))
    except DivisionByZero:
      return 0.0
  
  # get a winning number in a [0..1] range
  def winner(self):
    return random.random()
  
  # check if the bet won
  def wins(self, bet):
    return self.winner() <= self.odds(bet)
  
  # run the round for this player
  def run(self, player):
    # get a bet from the player
    bet = player.bet(self.pot)
    
    # check if the player won and update the bet
    if (self.wins(bet)):
      bet.win(bet.amount + self.pot)
    else:
      bet.lose()
  
  

