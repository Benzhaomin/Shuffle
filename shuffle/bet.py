#!/usr/bin/python
# -*- coding: utf-8 -*-

from shuffle.strategy.strategy import Strategy

class Bet:
  
  def __init__(self, amount):
    super().__init__()
    
    self.amount = amount
    self.status = None
  
  # records a win
  def win(self):
    self.status = True
  
  # returns true if that bet won
  def won(self):
    return self.status == True
  
  # records a loss
  def lose(self):
    self.status = False
  
  # returns true if that bet lost
  def lost(self):
    return self.status == False
  
  # returns true if that bet got a result
  def done(self):
    return self.won() or self.lost()
