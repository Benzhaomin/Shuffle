#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from shuffle.bet import Bet

# shuffle.bet.Bet.__init__()
class TestBetInit(unittest.TestCase):
  
  # check that init set attributes correctly
  def test_init(self):
    expected = 100.0
    b = Bet(expected)
    self.assertEqual(b.amount, expected)
    self.assertEqual(b.payout, None)

# shuffle.bet.Bet.win()
class TestBetWin(unittest.TestCase):
  
  # check that win() updates the payout correctly
  def test_won(self):
    expected = 300.0
    b = Bet(100.0)
    b.win(expected)
    self.assertEqual(b.payout, expected)

# shuffle.bet.Bet.won()
class TestBetWon(unittest.TestCase):
  
  # check that won() is false by default
  def test_won_won(self):
    b = Bet(100.0)
    self.assertEqual(b.won(), False)
  
  # check that won() is true after a loss
  def test_won_lost(self):
    b = Bet(100.0)
    b.status = True
    self.assertEqual(b.won(), True)
  
  # check that won() is true after a loss
  def test_won_lost(self):
    b = Bet(100.0)
    b.status = False
    self.assertEqual(b.won(), False)

# shuffle.bet.Bet.lose()
class TestBetLose(unittest.TestCase):
  
  # check that lose() updates the status correctly
  def test_lose(self):
    expected = -100.0
    b = Bet(100.0)
    b.lose()
    self.assertEqual(b.payout, expected)

# shuffle.bet.Bet.lost()
class TestBetLost(unittest.TestCase):
  
  # check that lost() is false by default
  def test_lost_won(self):
    b = Bet(100.0)
    self.assertEqual(b.lost(), False)
  
  # check that lost() is false after a loss
  def test_lost_lost(self):
    b = Bet(100.0)
    b.payout = -100.0
    self.assertEqual(b.lost(), False)
  
  # check that lost() is true after a loss
  def test_lost_lost(self):
    b = Bet(100.0)
    b.payout = -100.0
    self.assertEqual(b.lost(), True)

# shuffle.bet.Bet.paid()
class TestBetPaid(unittest.TestCase):
  
  # check that paid() is false by default
  def test_done_not_done(self):
    b = Bet(100.0)
    self.assertEqual(b.paid(), False)
  
  # check that paid() is true after a win
  def test_done_won(self):
    b = Bet(100.0)
    b.payout = 100.0
    self.assertEqual(b.paid(), True)
    
  # check that paid() is true after a loss
  def test_done_lost(self):
    b = Bet(100.0)
    b.payout = -100.0
    self.assertEqual(b.paid(), True)
