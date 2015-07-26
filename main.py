#!/usr/bin/python
# -*- coding: utf-8 -*-

import argparse
import logging
logger = logging.getLogger('shuffle.logger')

import shuffle.game as game

if __name__ == "__main__":
  parser = argparse.ArgumentParser()
  
  parser.add_argument('--log', dest='loglevel', default='WARNING',
    help="set the level of messages to display")
  
  parser.add_argument('--capital', dest='capital', type=float, default=1000.0,
    help="set the players' starting capital")
  
  parser.add_argument('--pot', dest='pot', type=float, default=100.0,
    help="set the pot size")
    
  parser.add_argument('--rounds', dest='rounds', type=int, default=10,
    help="set how many rounds to run")
  
  args = parser.parse_args()
  
  # set logger level
  numeric_level = getattr(logging, args.loglevel.upper(), None)
  if not isinstance(numeric_level, int):
    raise ValueError('Invalid log level: %s' % loglevel)
  
  logging.basicConfig(level=numeric_level, format='%(asctime)s %(message)s')
  
  # set the game up
  g = game.Game(pot=args.pot, capital=args.capital, rounds=args.rounds)
  print("playing a {rounds} rounds game with a {pot} pot and {capital} capital".format(rounds=g.rounds, pot=g.pot, capital=g.capital))
  
  # and play
  g.play()
  
  # output stats about the game
  for p in g.players:
    print("{player} ended the game with {funds:.2f} funds".format(funds=p.funds, player=p))


# read options
## player capital
## round count
## average pot size

# create game with those options
## create players with the same capital using each strategy
## create n rounds with those player and the set pot size

# play the game
## run 'count' rounds

### run a round
#### create round with pot size
#### run
##### ask player to bet on the round
###### player asks its strategy to see what to do with its capital and given the pot size
##### find winner based on odds
##### update bets (won lost)

#| player runs out of fund
#| count rounds run
# print stats:
## for each player
### used strategy: strat
### won/lost x total
### win percentage
