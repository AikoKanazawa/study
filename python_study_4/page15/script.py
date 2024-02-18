from menu_item import MenuItem

menu_item1 = MenuItem('サンドイッチ', 500)
menu_item2 = MenuItem('チョコケーキ', 400)
menu_item3 = MenuItem('コーヒー', 300)
menu_item4 = MenuItem('オレンジジュース', 200)

menu_items = [menu_item1, menu_item2, menu_item3, menu_item4]

# 変数 index を定義し、数値の 0 を代入してください
index = 0

for item in menu_items:
    # 「 0. サンドイッチ: ¥500 」となるように出力してください
    print(str(index) + '. ' + item.info())
    
    # 変数 index に 1 を加えてください
    index += 1
