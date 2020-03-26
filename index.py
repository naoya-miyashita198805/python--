# coding: UTF-8
# 一番上をこのように書かないとpythonでは日本語を認識してくれないコメントアウトでOK

from food import Food
from drink import Drink


food1 = Food('サンドイッチ', 500, 300)
food2 = Food('カレーライス', 750, 600)
food3 = Food('ハンバーガー', 300, 480)
        # ↑は引数それぞれ　__init__で定義された情報へ渡しに行く　ここでは380はcalorieにあたる
        # ちなみにこれがインスタンスの生成だよそんでここからfrom menu_item import MenuItem
        # で__init__メソッドが働く！


foods = [food1, food2, food3]
# ↑をmenu_itemにすればood.pyもdrink.pyもいらない
# もしfood.pyもdrink.pyも使わないならmenu_itemで行けるけど
# どんどんfood drink さらに仮に tableとか色々増えたら厄介
# プロゲートでは言及あまりしてないんので書いておく極論menu_itemだけでもできる

drink1 = Drink('コーヒー', 200, 250)
drink2 = Drink('コーラ', 150, 300)
drink3 = Drink('ビール', 500, 330)

drinks = [drink1, drink2, drink3]

print('メニューから番号でお選びください：')

print('----------------------------')
print('お食事一覧です')

index = 0
for food in foods:
    print(str(index) + '.' + food.info())
                            # ↑food.pyのinfoを呼び出すぞ！
    index += 1

print('----------------------------')
print('お飲み物一覧です')

index = 0
for drink in drinks:
    print(str(index) + '.' + drink.info())
    index += 1

print('----------------------------')

# -----参考コード-----

# def How_many_players():
#     player_num = input("How many players? ... ")
#     try:
#         player_num = int(player_num)
#     except:
#         print("Please enter 2, 3 or 4.")
#         return How_many_players()
#     if player_num < 2 or player_num > 4:
#         print("This game is for 2 ~ 4 people.")
#         return How_many_players()
#     else:
#         return player_num

# player_num = How_many_players()
# 上記のコードの参考記事はここhttps://ushitora.net/archives/520


# 以下のコードによって文字の判別、範囲外の番号をカットしてくれる
def validate_food_number():
    food_number = input('食べ物の番号を入力してください: ')
    try:
        food_number = int(food_number)
    except:
        print('数字を入力してください')
        return validate_food_number()
    if food_number < 0 or food_number > 2:
        print('その数字はデータにありません')
        return validate_food_number()
    else:
        return food_number
                            # ↓ここのカッコにreturnとしてきたfood_numberが帰ってくる
food_num = validate_food_number()
                # ↑少々紛らわしいがvalidate_food_numberで処理されたfood_numberはこちらに入ってくる
select_food = foods[food_num]

def validate_drink_number():
    drink_number = input('飲み物の番号を入力してください: ')
    try:
        drink_number = int(drink_number)
    except:
        print('数字を入力してください')
        return validate_drink_number()
    if drink_number < 0 or drink_number > 2:
        print('その数字はデータにありません')
        return validate_drink_number()
    else:
        return drink_number

drink_num = validate_drink_number()
select_drink = drinks[drink_num]

count = int(input('何セット購入しますか？３セット以上で１割引きです: '))
        # ↑intで文字から半角数字に変換！
result = select_food.get_total_price(count) + select_drink.get_total_price(count)
            # ↑には選択されたfoodの情報が入っているぞそれに加えてcountがくっついてget_total_priceの処理に飛んでいくイメージ

print('合計金額は' + str(result) + '円です')