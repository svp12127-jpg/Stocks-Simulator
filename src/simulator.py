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
        ticket=input("Which ticket would you like? ")
        share=int(input("Enter numberr of shares: "))
        for stock in market.stocks:
            if stock.tick == ticket:
                p.buy(stock, share)
                print(f"Bought {share} shares of {ticket}")
                break
        else:
            print("Stock not found!")

    elif c==3:
        print("Selling market")
        ticket=input("Which ticket would you like to sell? ")
        share=int(input("Enter number of shares: "))
        for stock in market.stocks:
            if stock.tick == ticket:
                if p.sell(stock, share):
                    print(f"Sold {share} shares of {ticket}")
                break
        else:
            print("Stock not found!")

    elif c==4:
        print("Displaying portfolio")
        p.display()

    elif c==5:
        print("Next day")
        market.update()
        market.display()
    elif c==6:
        print("Quitting")
        break
    else:
        print("Choose again")
        continue