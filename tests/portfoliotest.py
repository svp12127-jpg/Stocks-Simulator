import sys
sys.path.insert(0, './src')

from portfolio import Portfolio
from stock import Stock
from market import Market

apple = Stock("AAPL", "Apple", 180.00)
market = Market()
market.add(apple)
p = Portfolio()

print("--- Start Portfolio ---")
p.display(market)
print()

print("--- Buying 3 shares of AAPL ---")
p.buy(apple, 3)
p.display(market)
print()

print("--- Buying 2 more shares ---")
p.buy(apple, 2)    
p.display(market)
print()

print("--- Selling 4 shares ---")
p.sell(apple, 4)
p.display(market)
print()

print("--- Trying to sell more than we own ---")
p.sell(apple, 10)
p.display(market)
print()

print("--- Total Value ---")
print(f"Total Value: ${p.total(market)}")
print()

print("--- Transaction History ---")
p.showhistory()