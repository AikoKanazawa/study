from menu_item import MenuItem

class Food(MenuItem):
    # __init__ メソッドを定義してください
    def __init__(self, name, price, calorie):
        self.name = name
        self.price = price
        self.calorie = calorie
    
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'
    
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')