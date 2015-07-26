#!/usr/bin/python
# -*- coding: utf-8 -*-

from shuffle.strategy import Strategy

# given the pot and our capital, try to last as long as possible by betting a percent of our capital
class PercentStrategy(Strategy):
  
  def __init__(self):
    super().__init__()

  # returns the bet amount as a float
  def bet(capital=0.0,funds=0.0,pot=0.0):
    try:
      # capital / capital + pot => long-term odds
      odds = capital / (capital + pot)
      bet = capital * odds * 0.1
      
      # careful about low and negative funds
      return max(0.0, min(bet, funds))
    except DivisionByZero:
      return 0.0
