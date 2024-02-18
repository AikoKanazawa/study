from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for menu_item in menu_items:
    print(str(index) + '. ' + menu_item.info())
    index += 1

print('--------------------')

order = int(input('メニューの番号を入力してください: '))
selected_menu_item = menu_items[order]
print('選択されたメニュー: ' + selected_menu_item.name)

count = int(input('個数を入力してください(3つ以上で1割引): '))
result = selected_menu_item.get_total_price(count)
print('合計は' + str(result) + '円です')
