# utils.py をモジュールとして読み込んでください
import utils

print('じゃんけんをはじめます')
player_name = input('名前を入力してください：')
print('何を出しますか？（0: グー, 1: チョキ, 2: パー）')
player_hand = int(input('数字で入力してください：'))

# utils モジュール内の関数 validate を呼び出してください
if utils.validate(player_hand):
    computer_hand = 1

    if player_name == '':
        # utils モジュール内の関数 print_hand を呼び出してください
        utils.print_hand(player_hand)
    else:
        # utils モジュール内の関数 print_hand を呼び出してください
        utils.print_hand(player_hand, player_name)

    # utils モジュール内の関数 print_hand を呼び出してください
    utils.print_hand(computer_hand, 'コンピュータ')
    
    # utils モジュール内の関数 judge を呼び出してください
    result = utils.judge(player_hand, computer_hand)
    print('結果は' + result + 'でした')
else:
    print('正しい数値を入力してください')
