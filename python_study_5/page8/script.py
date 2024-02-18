from food import Food
from drink import Drink

food1 = Food('サンドイッチ', 500, 330)
print(food1.info())

drink1 = Drink('コーヒー', 300)
drink1.amount = 180
print(drink1.info())
