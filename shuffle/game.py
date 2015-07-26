#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('shuffle.logger')

from shuffle.player import Player
from shuffle.round import Round
from shuffle.strategy.allinstrategy import AllInStrategy
from shuffle.strategy.loweststrategy import LowestStrategy
from shuffle.strategy.randomstrategy import RandomStrategy
from shuffle.strategy.percentstrategy import PercentStrategy

class Game:
  
  def __init__(self, pot=100.0, capital=1000.0, rounds=10):
    super().__init__()
  
    # careful about negative values
    if pot <= 0:
      raise Exception("A game can't have an empty pot")
      
    if capital < 0:
      raise Exception("A game can't have players with a negative capital")
    
    if rounds <= 0:
      raise Exception("A game can't have no rounds")
    
    self.pot = pot
    self.capital = capital
    self.rounds = rounds
  
  # build players for each strategy
  def _get_player_list(self):
    return [
      Player(AllInStrategy(), self.capital),
      Player(LowestStrategy(), self.capital),
      Player(RandomStrategy(), self.capital),
      Player(PercentStrategy(), self.capital),
    ]
  
  # play the game, run all rounds for each player
  def play(self):
    # TODO: build the player list some other way
    self.players = self._get_player_list()
    rounds = [Round(self.pot) for n in range(self.rounds)]
    
    logger.debug("[game] playing a %s rounds game for %s players", self.rounds, len(self.players))
    
    for r in rounds:
      for p in self.players:
        r.run(p)
  
  
