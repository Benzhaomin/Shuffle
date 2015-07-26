#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from unittest.mock import patch

from shuffle.game import Game
from shuffle.player import Player
from shuffle.strategy.strategy import Strategy

#capital, rounds, pot):

# shuffle.round.Game.__init__()
class TestGameInit(unittest.TestCase):
  
  # check that init set our attributes correctly
  def test_init(self):
    g = Game(pot=100.0, capital=1000.0, rounds=10)
    self.assertEqual(g.pot, 100.0)
    self.assertEqual(g.capital, 1000.0)
    self.assertEqual(g.rounds, 10)

  # check that init raises an exception on negative and null values
  def test_init_negative_pot(self):
    self.assertRaises(Exception, Game, -1, 1, 1)
    
  def test_init_null_pot(self):
    self.assertRaises(Exception, Game, 0, 1, 1)
    
  def test_init_negative_capital(self):
    self.assertRaises(Exception, Game, 1, -1, 1)
    
  def test_init_negative_rounds(self):
    self.assertRaises(Exception, Game, 1, 1, -1)
    
  def test_init_null_rounds(self):
    self.assertRaises(Exception, Game, 1, 1, 0)
  
# shuffle.round.Game._get_player_list()
class TestGameGetPlayerList(unittest.TestCase):
  
  # check that init set our attributes correctly
  def test_get_player_list(self):
    g = Game(pot=100.0, capital=1000.0, rounds=10)
    players = g._get_player_list()
    
    # make sure we have players
    self.assertTrue(len(players) > 0)
    
    # make sure their capital was set correctly
    self.assertEqual(players[0].capital, 1000.0)

# shuffle.round.Game.play()
class TestGamePlay(unittest.TestCase):
  
  # check that we ran rounds for each player
  @patch('shuffle.game.Game._get_player_list', return_value=[Player(Strategy(), 100.0), Player(Strategy(), 100.0)])
  def test_play(self, foo):
    g = Game(pot=100.0, capital=1000.0, rounds=10)
 
    with patch('shuffle.round.Round.run') as run:
      g.play()
      
      self.assertEqual(run.call_count, 20)
