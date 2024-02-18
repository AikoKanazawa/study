from menu_item import MenuItem

class Drink(MenuItem):
    # info メソッドを定義してください
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'
    