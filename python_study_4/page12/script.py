class MenuItem:
    # 引数 name と price を受け取るようにしてください
    def __init__(self, name, price):
        # 「 サンドイッチ 」の代わりに引数 name の値を代入してください
        self.name = name
        
        # 500 の代わりに引数 price の値を代入してください
        self.price = price

    def info(self):
        return self.name + ': ¥' + str(self.price)

    def get_total_price(self, count):
        total_price = self.price * count
        return total_price


# 引数を「 サンドイッチ 」と 500 としてください
menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')
