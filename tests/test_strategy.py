#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from shuffle.strategy.strategy import Strategy
from shuffle.strategy.allinstrategy import AllInStrategy
from shuffle.strategy.loweststrategy import LowestStrategy
from shuffle.strategy.randomstrategy import RandomStrategy
from shuffle.strategy.percentstrategy import PercentStrategy

# shuffle.strategy.strategy.Strategy
class TestStrategy(unittest.TestCase):
  
  # check that bet() is abstract
  def test_not_implemented_exception(self):
    s = Strategy()
    self.assertRaises(NotImplementedError, s.bet)

# shuffle.strategy.loweststrategy.LowestStrategy
class TestAllInStrategy(unittest.TestCase):
  
  # check that bet() return the right amount
  def test_default_bet_amount(self):
    s = AllInStrategy()
    funds = 100.0
    expected = funds
    actual = s.bet(funds=funds)
    self.assertEqual(actual, expected)
  
  # check that bet() stays over 0
  def test_default_bet_negative_funds(self):
    s = AllInStrategy()
    expected = 0.0
    actual = s.bet(funds=-100.0)
    self.assertEqual(actual, expected)

# shuffle.strategy.loweststrategy.LowestStrategy
class TestLowestStrategy(unittest.TestCase):
  
  # check that bet() return the right amount
  def test_default_bet_amount(self):
    s = LowestStrategy()
    expected = 10.0
    actual = s.bet(funds=100)
    self.assertEqual(actual, expected)
  
  # check that bet() stays within funds
  def test_default_bet_low_funds(self):
    s = LowestStrategy()
    expected = 5.0
    actual = s.bet(funds=5.0)
    self.assertEqual(actual, expected)
    
  # check that bet() stays over 0
  def test_default_bet_negative_funds(self):
    s = LowestStrategy()
    expected = 0.0
    actual = s.bet(funds=-10.0)
    self.assertEqual(actual, expected)

# shuffle.strategy.loweststrategy.RandomStrategy
class TestRandomStrategy(unittest.TestCase):
    
  # check that bet() stays within funds
  def test_default_bet_low_funds(self):
    s = RandomStrategy()
    funds = 100.0
    actual = s.bet(funds=funds)
    self.assertTrue(actual <= funds)
    self.assertTrue(actual >= 0)
    
  # check that bet() stays over 0
  def test_default_bet_negative_funds(self):
    s = RandomStrategy()
    funds = -100.0
    actual = s.bet(funds=funds)
    self.assertTrue(actual >= 0)

# shuffle.strategy.loweststrategy.PercentStrategy
class TestPercentStrategy(unittest.TestCase):
  
  # check that bet() return the right amount
  def test_default_bet_amount(self):
    s = PercentStrategy()
    expected = 50.0
    actual = s.bet(capital=1000.0, pot=1000.0, funds=1000.0)
    self.assertEqual(actual, expected)
  
  # check that bet() stays within funds
  def test_default_bet_low_funds(self):
    s = PercentStrategy()
    expected = 10.0
    actual = s.bet(capital=1000.0, pot=1000.0, funds=10.0)
    self.assertEqual(actual, expected)
    
  # check that bet() stays over 0
  def test_default_bet_negative_funds(self):
    s = PercentStrategy()
    expected = 0.0
    actual = s.bet(capital=1000.0, pot=1000.0, funds=-1000.0)
    self.assertEqual(actual, expected)
