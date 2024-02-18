# Food クラスと Drink クラスをそれぞれ読み込んでください
from food import Food
from drink import Drink

# Food クラスのインスタンスを生成して変数 food1 に代入してください
food1 = Food('サンドイッチ', 500)

# food1 に対して info メソッドを呼び出して戻り値を出力してください
print(food1.info())

# Drink クラスのインスタンスを生成して変数 drink1 に代入してください
drink1 = Drink('コーヒー', 300)

# drink1 に対して info メソッドを呼び出して戻り値を出力してください
print(drink1.info())
