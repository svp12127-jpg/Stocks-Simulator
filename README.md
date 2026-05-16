# Stock Market Simulator

An educational stock market simulator built in Python. Buy and sell stocks, track your portfolio, and learn how markets work.

## Features

- View a live market with multiple stocks and real-time price changes
- Buy and sell stocks with cash balance tracking
- View your portfolio with total value calculated at current prices
- See your full transaction history
- Chart any stock's price history over time

## Project Structure

```
Stocks-Simulator/
├── src/
│   ├── stock.py        # Stock class with price simulation
│   ├── market.py       # Market class managing multiple stocks
│   ├── portfolio.py    # Portfolio class with buy, sell, and history
│   └── simulator.py    # Main CLI entry point
├── tests/
│   └── portfoliotest.py
└── README.md
```

## How to Run

```bash
python src/simulator.py
```

## Requirements

```bash
python -m pip install matplotlib
```

## How to Play

1. Start with $10,000
2. View the market to see current stock prices
3. Buy stocks you think will go up
4. Advance to the next day to update prices
5. Sell stocks to lock in profits
6. Track your portfolio value and transaction history