# coding: UTF-8
from menu_item import MenuItem

class Food(MenuItem):
            # ↑ここの部分記入忘れがち、承継したなら書いておこう

    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie

    def info(self):
        return self.name + ':¥ '  + str(self.price) + ' ' + str(self.calorie) + 'kcal'

    # def choice_food(self,food_number):
    #     food_number = int(input('食べ物の番号を入力してください: '))
    #     self.food_number = food_number
    #     if self.food_number > 0 or self.food_number < 2:
    #         # select_food = foods[food_number]
    #         print('正しい数値を入力してください')
    #         return choice_food()
    #     else:
    #         return True
    # errorが起きたときのそのまま実行はtryとexcept、index.pyに記述済みこれは
    # こっちに関数作って色々やろうとしたが失敗に終わった
    