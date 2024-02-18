class MenuItem:
    def __init__(self):
        # self.name に「 サンドイッチ 」を代入してください
        self.name = 'サンドイッチ'
        
        # self.price に 500 を代入してください
        self.price = 500

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
# 以下の2行は削除してください

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')
