#!/usr/bin/python
# -*- coding: utf-8 -*-

import random

from shuffle.strategy.strategy import Strategy

# return a random amount
class RandomStrategy(Strategy):
  
  def __init__(self):
    super().__init__()

  # returns the bet amount as a float
  def bet(capital=0.0,funds=0.0,pot=0.0):
    bet = funds * random.random()
    
    # careful about low and negative funds
    return max(0.0, min(bet, funds))
