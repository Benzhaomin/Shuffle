#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('shuffle.logger')

from shuffle.bet import Bet

class Player:
  
  def __init__(self, strategy, capital):
    super().__init__()
    
    self.strategy = strategy
    self.capital = capital
    self.bets = []

  # returns the strategy's class name
  def __str__(self):
    return "{} player".format(self.strategy)
    
  @property
  # returns the amount of capital left as a float
  def funds(self):
    # add up money we won (we put x, we get y back, we won y-x)
    diff = sum([bet.payout - bet.amount for bet in self.bets if bet.won()])
    
    # add up all losses (payouts are negative)
    diff += sum([bet.payout for bet in self.bets if bet.lost()])
    
    # add up all bets placed but not paid yet
    diff += sum([-bet.amount for bet in self.bets if not bet.paid()])
    
    # careful about bogus bets payout
    return max(self.capital + diff, 0.0)
  
  # returns a Bet, with an amount computed by our strategy, and store it locally
  def bet(self, pot):
    # get bet size from our strategy
    amount = self.strategy.bet(capital=self.capital, funds=self.funds, pot=pot)
    
    # build and store the bet for further use
    bet = Bet(amount)
    self.bets.append(bet)
    logger.debug("[player] %s placed a %.2f bet on a %.2f pot", self, bet.amount, pot)
    
    return bet
