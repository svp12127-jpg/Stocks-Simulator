class Portfolio:
    def __init__(self):
        self.cash = 10000        #starting money
        self.holdings = {} 
        self.history = []

    def buy(self,stock,shares):
        total=stock.price*shares
        if self.cash>=total:
            self.cash=self.cash-total
            if stock.tick in self.holdings:
                self.holdings[stock.tick] += shares
            else:
                self.holdings[stock.tick] = shares
            self.history.append({"type": "BUY", "tick": stock.tick, "shares": shares, "price": stock.price, "total": total})
            return True
        else:
            print("Not enough cash!")
            return False
    
    def sell(self,stock,shares):
        sell=stock.price*shares
        
        if stock.tick in self.holdings and self.holdings[stock.tick] >= shares:
            self.holdings[stock.tick] -= shares
            self.cash=self.cash+sell
            self.history.append({"type": "SELL", "tick": stock.tick, "shares": shares, "price": stock.price, "total": sell})
            return True
        else:
            print("Not enough shares to sell!")
            return False

    def total(self,market):
        t=self.cash
        for tick, shares in self.holdings.items():
            for stock in market.stocks:
                if stock.tick==tick:
                    t+=stock.price*shares
        return round(t,2)            

    def showhistory(self):
        print("---Transaction History---")
        for t in self.history:
            sign = "-" if t['type'] == "BUY" else "+"
            print(f"{t['type']} | {t['tick']} | {t['shares']} shares | ${t['price']} each | {sign}${t['total']}")

    def display(self,market):
        print("Cash:", self.cash)
        for tick, shares in self.holdings.items():
            print(f"{tick}: {shares} shares")
        print(f"Total Value: ${self.total(market)}")