from food import Food
from drink import Drink

# Food() に引数を追加してください
food1 = Food('サンドイッチ', 500, 330)

# 以下の1行は削除してください

print(food1.info())

drink1 = Drink('コーヒー', 300)
drink1.amount = 180
print(drink1.info())
