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

  # check that the bet init raises an exception on negative values
  def test_init_negative(self):
    self.assertRaises(Exception, Bet, -100.0)
  
# shuffle.bet.Bet.amount()
class TestBetAmountGetter(unittest.TestCase):
  
  # check that the amount getter return the right value
  def test_bet_get(self):
    b = Bet(100.0)
    self.assertEqual(b.amount, 100)

# shuffle.bet.Bet.amount(value)
class TestBetPotSetter(unittest.TestCase):
  
  # check that the amount setter raises an exception
  def test_bet_set_negative(self):
    b = Bet(100.0)
    self.assertRaises(Exception, b.amount, 100)

# shuffle.bet.Bet.__eq__()
class TestBetEquality(unittest.TestCase):
  
  # check that a bet object is equal to itself
  def test_bet_eq_is_same(self):
    v = Bet(100.0)
    self.assertEqual(v, v)
  
  # check that two bet objects are equal
  def test_bet_eq_amount_is_equal(self):
    v1 = Bet(100.0)
    v2 = Bet(100.0)
    self.assertEqual(v1, v2)
  
  # check that two different bet objects are not equal
  def test_bet_eq_amount_is_different(self):
    v1 = Bet(200.0)
    v2 = Bet(100.0)
    self.assertFalse(v1 == v2)
  
  # check that two bet objects are equal
  def test_bet_eq_payout_is_equal(self):
    v1 = Bet(100.0)
    v1.payout = 100.0
    v2 = Bet(100.0)
    v2.payout = 100.0
    self.assertEqual(v1, v2)
  
  # check that two different bet objects are not equal
  def test_bet_eq_payout_is_different(self):
    v1 = Bet(100.0)
    v1.payout = 100.0
    v2 = Bet(100.0)
    v2.payout = 200.0
    self.assertFalse(v1 == v2)

# shuffle.bet.Bet.__ne__()
class TestBetNotEquality(unittest.TestCase):
  
  # check that a bet object is equal to itself
  def test_bet_ne_is_same(self):
    v = Bet(100.0)
    self.assertFalse(v != v)
  
  # check that two bet objects are equal
  def test_bet_ne_amount_is_equal(self):
    v1 = Bet(100.0)
    v2 = Bet(100.0)
    self.assertFalse(v1 != v2)
  
  # check that two different bet objects are not equal
  def test_bet_ne_amount_is_different(self):
    v1 = Bet(100.0)
    v2 = Bet(200.0)
    self.assertTrue(v1 != v2)
  
  # check that two bet objects are equal
  def test_bet_ne_payout_is_equal(self):
    v1 = Bet(100.0)
    v1.payout = 100.0
    v2 = Bet(100.0)
    v2.payout = 100.0
    self.assertFalse(v1 != v2)
  
  # check that two different bet objects are not equal
  def test_bet_ne_payout_is_different(self):
    v1 = Bet(100.0)
    v1.payout = 100.0
    v2 = Bet(100.0)
    v2.payout = 200.0
    self.assertTrue(v1 != v2)

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
