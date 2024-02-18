from menu_item import MenuItem

class Food(MenuItem):
    # info メソッドを定義してください
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'
    
    
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')