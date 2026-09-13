# BlackJack

A console-based Blackjack game written in pure Python. Play against the dealer with 1 or 2 players, place bets, and hit, stand, or fold your way to 21.

## How it works

- `mainmenu.py` — entry point; shows the game portal, collects player details, and launches the chosen game.
- `games.py` — `Game` base class shared by all games (player setup, readiness check, bet collection).
- `blackjack.py` — `BlackJack` class extending `Game` with the actual Blackjack rules and gameplay loop.

## Requirements

- Python 3 (no external dependencies)

## Running the game

```bash
python3 mainmenu.py
```

You'll be prompted to:
1. Confirm you're ready to play (`Y` to start).
2. Choose the number of players (1 or 2).
3. Enter each player's name and bet.
4. Select a game (currently only Blackjack is available).

## Rules

- Up to 2 players can participate against the dealer.
- Bets are placed before the round starts.
- On your turn, choose to **Hit** (draw a card), **Stand** (keep your current hand), or **Fold** (exit the round).
- Card values: number cards count at face value, `J`/`Q`/`K` count as their listed value, and `A` counts as 11 (recalculated to 1 if the hand would otherwise bust).
- If your total goes over 21, you bust and are out of the round.
- Hitting 21 on your first two cards pays out one and a half times your bet; a later 21 pays out your full bet.
- The dealer draws automatically based on their hand total until they stand, bust, or reach 21.
