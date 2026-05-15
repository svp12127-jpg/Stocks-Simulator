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
            return True
        else:
            print("Not enough cash!")
        return False
    
    def sell(self,stock,shares):
        sell=stock.price*shares
        
        if stock.tick in self.holdings and self.holdings[stock.tick] >= shares:
            self.holdings[stock.tick] -= shares
            self.cash=self.cash+sell
            return True
        else:
            print("Not enough shares to sell!")
            return False

    def display(self):
        print("Cash:", self.cash)
        for tick, shares in self.holdings.items():
            print(f"{tick}: {shares} shares")