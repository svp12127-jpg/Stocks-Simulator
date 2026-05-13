import random

class Stock:
    def __init__(self, tick, name, price):
        self.tick=tick
        self.name=name
        self.price=price
        self.oldprice=price

    def update_price(self):
        # Randomly move the price up or down by up to 5%
        change = random.uniform(-0.05, 0.05)
        self.oldprice = self.price
        self.price = round(self.price * (1 + change), 2)

    def get_change(self):
        return round(self.price - self.oldprice, 2)

    def display(self):
        change = self.get_change()
        arrow = "↑" if change > 0 else "↓" if change < 0 else "→"
        print(f"{self.tick} | {self.name} | ${self.price} | {arrow} {change}")


# Test it
if __name__ == "__main__":
    apple = Stock("AAPL", "Apple", 180.00)

    for i in range(5):
        apple.update_price()
        apple.display()