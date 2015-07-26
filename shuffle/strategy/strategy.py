#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
logger = logging.getLogger('shuffle.logger')

class Strategy:
  
  def __init__(self):
    super().__init__()
  
  # returns the class name
  def __str__(self):
    return str(type(self).__name__)

  # returns the bet amount as a float
  # bets must always be >= 0 and <= funds
  def bet(self, capital=0.0,funds=0.0,pot=0.0):
    raise NotImplementedError()
