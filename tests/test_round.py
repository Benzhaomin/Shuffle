#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from shuffle.bet import Bet
from shuffle.round import Round
from shuffle.player import Player
from shuffle.strategy.strategy import Strategy

# shuffle.round.Round.__init__()
class TestRoundInit(unittest.TestCase):
  
  # check that init set our attributes correctly
  def test_init(self):
    r = Round(100.0)
    self.assertEqual(r.pot, 100)

  # check that the pot init raises an exception on negative values
  def test_init_negative(self):
    self.assertRaises(Exception, Round, -100.0)
  
# shuffle.round.Round.pot()
class TestRoundPotGetter(unittest.TestCase):
  
  # check that the pot getter return the right value
  def test_pot_get(self):
    r = Round(100.0)
    self.assertEqual(r.pot, 100)

# shuffle.round.Round.pot(value)
class TestRoundPotSetter(unittest.TestCase):
  
  # check that the pot setter raises an exception
  def test_pot_set_negative(self):
    r = Round(100.0)
    self.assertRaises(Exception, r.pot, 100.0)

# shuffle.round.Round.odds()
class TestRoundOdds(unittest.TestCase):
  
  # check that odds are computed correctly
  def test_odds(self):
    r = Round(100.0)
    b = Bet(100.0)
    expected = 0.5
    actual = r.odds(b)
    self.assertEqual(expected, actual)
  
# shuffle.round.Round.winner()
class TestRoundWinner(unittest.TestCase):
  
  # check that the winner is in the [0..1] range
  def test_winner_range(self):
    # run 1000 rounds to have a better confidence
    for n in range(1000):
      r = Round(100.0)
      winner = r.winner()
      self.assertTrue(winner >= 0 and winner <= 1)
      
  # check that two rounds don't get the same winner
  def test_winner_randomness(self):
    # run 1000 rounds to have a better confidence
    for n in range(1000):
      winner1 = Round(100.0).winner()
      winner2 = Round(100.0).winner()
      self.assertNotEqual(winner1, winner2) 

# shuffle.round.Round.wins()
class TestRoundWins(unittest.TestCase):
  
  # check that the winning bet is correctly reported
  @patch('shuffle.round.Round.winner', return_value=0.2)
  def test_wins_winning_bet(self, foo):
    r = Round(100.0)
    b = Bet(100.0)
    # winning ticket set at 0.2, bet odds at 0.5
    self.assertTrue(r.wins(b))
  
  # check that the winning bet is correctly reported
  @patch('shuffle.round.Round.winner', return_value=0.2)
  def test_wins_losing_bet(self, foo):
    r = Round(90.0)
    b = Bet(10.0)
    # winning ticket set at 0.2, bet odds at 0.1
    self.assertFalse(r.wins(b))
  
# shuffle.round.Round.wins()
class TestRoundRun(unittest.TestCase):
  
  # check that a run gets a bet from the player and updates its value when winning
  @patch('shuffle.round.Round.winner', return_value=0.2)
  def test_run_win(self, foo):
    r = Round(100.0)
    p = Player(Strategy(), 1000.0)
    
    # check that we get a bet with the pot amount from the player
    with patch('shuffle.player.Player.bet', return_value=Bet(100.0)) as bet:
      
      # check that we update the bet following the win
      with patch('shuffle.bet.Bet.win') as win:
        r.run(p)
        bet.assert_called_once_with(100.0)
        win.assert_called_once_with(200.0)
        
  # check that a run gets a bet from the player and updates its value losing
  @patch('shuffle.round.Round.winner', return_value=1.1)
  def test_run_loss(self, foo):
    r = Round(100.0)
    p = Player(Strategy(), 1000.0)
    
    # check that we get a bet with the pot amount from the player
    with patch('shuffle.player.Player.bet', return_value=Bet(100.0)) as bet:
      
      # check that we update the bet following the win
      with patch('shuffle.bet.Bet.lose') as lost:
        r.run(p)
        bet.assert_called_once_with(100.0)
        lost.assert_called_once_with()
      
      
