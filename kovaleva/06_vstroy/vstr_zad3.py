class Item:
    def __init__(self, name, cost):
        self.Name = name
        self.Cost = cost

    def __str__(self):
        return f"{self.Name}: {self.Cost}"

class Busket:
    def __init__(self):
        self.TotalPrice = 0
        self.Items = []

    def __add__(self, item):
        self.Items.append(item)
        self.TotalPrice += item.Cost
        return self

    def __sub__(self, item):
        self.Items.remove(item)
        self.TotalPrice -= item.Cost
        return self

    def __str__(self):
        return f"{ ' '.join([str(item) for item in self.Items])} Total: {self.TotalPrice}"

busket = Busket()
tomato = Item("tomato", 1.55)
banana = Item("banana", 2.12)
vine = Item("vine", 14.90)

busket + tomato + banana + vine
print(busket)
busket - vine
print(busket)