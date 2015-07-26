#!/usr/bin/python
# -*- coding: utf-8 -*-

class Strategy:
  
  def __init__(self):
    super().__init__()

  # returns the bet amount as a float
  # bets must always be >= 0 and <= funds
  def bet(capital=0.0,funds=0.0,pot=0.0):
    raise NotImplementedError()
