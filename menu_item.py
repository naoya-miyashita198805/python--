# coding: UTF-8
class MenuItem:
    def __init__(self, name, price):
                        # ↑は下のコードの右辺に当たるから右辺とは合わせる必要あり
        self.name = name
            # ↑ここはなんでもいいよ、ただわかり辛くなるから右辺に合わせた方が無難
            # Rubyでいう＠がselfになっているよって仕組みは一緒だから
            # 別のところでも使える
        self.price = price
            # インスタンスメソッドの中では、「self.変数名」でインスタンス変数を扱うことができるので、
            # 「self.変数名 = 値」でインスタンス変数に値を代入できる。

    # def validate(self, select_number):
    #     if select_number < 0 or select_number > 2:
    #         return False
    #     return True
    # バリデーション関係はindex.pyに記載これは備忘録のため残しておくこれは失敗のコード

    def info(self):
        return self.name + ': ¥' + str(self.price)
    
    def get_total_price(self, count):
        total_price = self.price * count

        if count >= 3:
            total_price *= 0.9

        return round(total_price) 
                # ↑四捨五入はこれ
    
    