#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from shuffle.bet import Bet
from shuffle.player import Player
from shuffle.strategy.strategy import Strategy

# shuffle.player.Player.__init__()
class TestPlayerInit(unittest.TestCase):
  
  # check that init 
  def test_init(self):
    capital = 100.0
    s = Strategy()
    p = Player(s, capital)
    self.assertEqual(p.strategy, s)
    self.assertEqual(p.capital, capital)
    self.assertEqual(p.bets, [])

# shuffle.player.Player.bet()
class TestPlayerBet(unittest.TestCase):
  
  # check that we get a correct Bet object
  @patch('shuffle.strategy.strategy.Strategy.bet', return_value=100.0)
  def test_all_in_bet_amount(self, foo):
    p = Player(Strategy(), 100.0)
    expected = Bet(100.0)
    actual = p.bet(100.0)
    self.assertEqual(actual, expected)
  
  # check that the Bet object was saved
  @patch('shuffle.strategy.strategy.Strategy.bet', return_value=100.0)
  def test_bet_saved_bet(self, foo):
    p = Player(Strategy(), 100.0)
    expected = [Bet(100.0)]
    p.bet(100.0)
    self.assertEqual(p.bets, expected)

# shuffle.player.Player.funds()
class TestPlayerFunds(unittest.TestCase):

  # check that funds are correct without bets
  def test_funds_no_bets(self):
    p = Player(Strategy(), 100.0)
    expected = 100.0
    actual = p.funds()
    self.assertEqual(actual, expected)
  
  # check that funds are correct after a bet
  @patch('shuffle.strategy.strategy.Strategy.bet', return_value=100.0)
  def test_funds_one_bet(self, foo):
    p = Player(Strategy(), 100.0)
    p.bet(100.0).payout = 100.0
    expected = 200.0
    actual = p.funds()
    self.assertEqual(actual, expected)
    
  # check that funds are correct after a few bets, one of them unpaid yet
  @patch('shuffle.strategy.strategy.Strategy.bet', return_value=100.0)
  def test_funds_few_bets(self, foo):
    p = Player(Strategy(), 100.0)
    p.bet(100.0).payout = 400.0
    p.bet(100.0).payout = -100.0
    p.bet(100.0).payout = -100.0
    p.bet(100.0)
    expected = 300.0
    actual = p.funds()
    self.assertEqual(actual, expected)
    
  # check that funds stay at 0 even with bogus bet payouts going below 0
  @patch('shuffle.strategy.strategy.Strategy.bet', return_value=100.0)
  def test_funds_bogus_bets(self, foo):
    p = Player(Strategy(), 100.0)
    p.bet(100.0).payout = -400.0
    expected = 0.0
    actual = p.funds()
    self.assertEqual(actual, expected)
