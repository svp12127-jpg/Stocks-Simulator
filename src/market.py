from stock import Stock

class Market:
    def __init__(self):
        self.stocks = []
    
    def add(self,stock):
        self.stocks.append(stock)
    
    def update(self):
        for stock in self.stocks:
            stock.update_price()

    def display(self):
        for stock in self.stocks:
            stock.display()

if __name__ == "__main__":
    market = Market()
    market.add(Stock("AAPL", "Apple", 180.00))
    market.add(Stock("TSLA", "Tesla", 250.00))
    market.add(Stock("GME", "GameStop", 20.00))
 
    for day in range(1, 4):
        print(f"\nDay {day}")
        market.update()
        market.display()