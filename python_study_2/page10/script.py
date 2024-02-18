numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for number in numbers:
    # 変数 number の値が 3 の倍数のとき、繰り返し処理をスキップしてください
    if number % 3 == 0:
        continue
    
    print(number)