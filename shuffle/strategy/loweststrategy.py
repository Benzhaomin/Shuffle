#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('shuffle.logger')

from shuffle.strategy.strategy import Strategy

# always bet the lowest possible amount
class LowestStrategy(Strategy):
  
  def __init__(self):
    super().__init__()

  # returns the bet amount as a float
  def bet(self, capital=0.0,funds=0.0,pot=0.0):
    bet = 10.0
    
    # careful about low and negative funds
    return max(0.0, min(bet, funds))
