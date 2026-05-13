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