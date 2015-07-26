#!/usr/bin/python
# -*- coding: utf-8 -*-

#OutOfFundsException

from shuffle.bet import Bet

class Player:
  
  def __init__(self, strategy, capital):
    super().__init__()
    
    self.strategy = strategy
    self.capital = capital
    self.bets = []

  # returns the amount of capital left as a float
  def funds(self):
    # add up all payouts
    diff = sum([bet.payout for bet in self.bets if bet.paid()])
    
    # careful about bogus bets payout
    return max(self.capital + diff, 0.0)
  
  # returns a Bet, with an amount computed by our strategy, and store it locally
  def bet(self, pot):
    # get bet size from our strategy
    amount = self.strategy.bet(capital=self.capital, funds=self.funds(), pot=pot)
    
    # build and store the bet for further use
    bet = Bet(amount)
    self.bets.append(bet)
    
    return bet
