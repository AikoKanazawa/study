from menu_item import MenuItem

class Food(MenuItem):
    # calorie_info メソッドを定義してください
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')
    