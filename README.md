# Shuffle

Simulate outcomes of a shuffle game based on betting strategy and initial capital

## Rules

- Players can place one bet, lowest $10 (#TODO: 10 items max, in-round re-bets)
- Odds to win are bet/pot, eg. $10 on a $100 pot has 10% chance to win
- Winner chosen randomly

## Gameplay

- Round starts
- Game engine places random bets, increasing the pot
- Our simulated player looks at round state (pot size, owned capital) and uses his strategy to bet
- Round ends

## Stategies

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

