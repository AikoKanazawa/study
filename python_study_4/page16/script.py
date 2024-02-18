from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

index = 0

for item in menu_items:
    print(str(index) + '. ' + item.info())
    index += 1

print('--------------------')

# コンソールから入力を受け取り、変数 order に代入してください
order = int(input('メニューの番号を入力してください: '))

# 選択されたメニューを変数 selected_menu に代入してください
selected_menu = menu_items[order]

# 「 選択されたメニュー: 〇〇 」と出力してください
print('選択されたメニュー: ' + selected_menu.name)
