from stock import Stock
from market import Market
from portfolio import Portfolio

market = Market()
market.add(Stock("AAPL", "Apple", 180.00))
market.add(Stock("TSLA", "Tesla", 250.00))
market.add(Stock("GME", "GameStop", 20.00))

p = Portfolio()
while True:
    print()
    print("""--- Stock Simulator ---
1. View Market
2. Buy Stock
3. Sell Stock
4. View Portfolio
5. Next Day
6. Quit""")
    print()
    c=int(input("Enter your choice: "))
    if c==1:
        print("Displaying market")
        market.display()
    elif c==2:
        print("Buying market")
    elif c==3:
        print("Selling market")
    elif c==4:
        print("Displaying portfolio")
    elif c==5:
        print("Next day")
        market.update()
        market.display()
    elif c==6:
        print("Quit")
        break
    else:
        print("Choose again")
        continue