class MenuItem:
    def info(self):
        return self.name + ': ¥' + str(self.price)

    # get_total_price メソッドを定義してください
    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


menu_item1 = MenuItem()
menu_item1.name = 'サンドイッチ'
menu_item1.price = 500

print(menu_item1.info())

# get_total_price メソッドを呼び出してください
result = menu_item1.get_total_price(4)

# 「 合計は〇〇円です 」となるように出力してください
print('合計は' + str(result) + '円です')
