# Shuffle

Simulate outcomes of a shuffle game based on betting strategy and initial capital.

## Rules

- Players can place one bet, lowest $10 (#TODO: 10 items max, in-round re-bets)
- Odds to win are bet/pot, eg. $10 on a $100 pot has 10% chance to win
- Winner chosen randomly

## Gameplay

- Round starts
- Game engine sets a pot size
- Our simulated player looks at round state (pot size, owned capital) and uses his strategy to bet
- Round ends

## Strategies

### All-in

Simply go all-in every round. Very likely to work when your capital is much bigger than the average pot.
You will get bitten at times and lose it all when some guy with 1% chance to win does win.

### Lowest bet

Always place as low a bet as possible, hoping to last long enough that you win a 1% chance pot.

### Percent of capital

Look at the average pot size and your capital, find the amount that should allow you to last until you win your money back.
This strategy's goal is to break even and play for a long time.
It's a valid choice only if you make money some other way while you play (eg. streaming to 20k viewers).

### Random bet

Place random bets until you have no money left. See how you fare compared to those other clever strategies.

## Usage

- basic run with default settings ($1000 capital, $100 pot, 10 rounds): `python main.py`
- track bets of a strategy: `python main.py --log DEBUG 2>&1 | grep RandomStrategy | grep '\[player\]'`
- track rounds of a strategy: `python main.py --log DEBUG 2>&1 | grep LowestStrategy | grep '\[round\]'`

# License

> Shuffle, a simple Python 3 program to simulate outcomes of a shuffle game.
> Copyright (C) 2015 Benjamin Maisonnas

> This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as published by
the Free Software Foundation.

> This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

> You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/gpl-3.0.en.html>.
