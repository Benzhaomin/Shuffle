#!/usr/bin/python
# -*- coding: utf-8 -*-

from shuffle.strategy.strategy import Strategy

class Bet:
  
  def __init__(self, amount):
    super().__init__()
    
    self.amount = amount
    self.payout = None
  
  # use self.amount and self.payout for identity
  def __eq__(self, other):
    return isinstance(other, Bet) and self.amount == other.amount and self.payout == other.payout
  
  def __ne__(self, other):
    return not self == other
  
  # loads details about the video in a dict
  def load(self):
    if self.json:
      return self
  
  # records a win
  def win(self, amount):
    self.payout = amount
  
  # returns true if that bet won
  def won(self):
    return self.payout is not None and self.payout > 0
      
  # records a loss
  def lose(self):
    self.payout = -self.amount
  
  # returns true if that bet lost
  def lost(self):
    return self.payout is not None and self.payout <= 0
  
  # returns true if that bet got a result
  def paid(self):
    return self.won() or self.lost()
