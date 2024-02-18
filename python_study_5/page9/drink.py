from menu_item import MenuItem

class Drink(MenuItem):
    # __init__ メソッドを定義してください
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount
    
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
