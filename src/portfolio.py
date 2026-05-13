class Portfolio:
    def __init__(self):
        self.cash = 10000        #starting money
        self.holdings = {} 
    
    def buy(self,stock,shares):
        total=stock.price*shares
        if self.cash>=total:
            self.cash=self.cash-total
            if stock.tick in self.holdings:
                self.holdings[stock.tick] += shares
            else:
                self.holdings[stock.tick] = shares