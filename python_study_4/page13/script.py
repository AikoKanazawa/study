# この行より上のコードを「 menu_item.py 」に移動してください

# menu_item.py から MenuItem クラスを読み込んでください
from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)

print(menu_item1.info())

result = menu_item1.get_total_price(4)
print('合計は' + str(result) + '円です')
