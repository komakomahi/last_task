from msvcrt import getch

# それぞれの金額
goods_name_list = ["1.ワッフル", "2.クレープ", "3.豚タン", "4.ベビーカステラ"]
goods_list = [180, 320, 500, 200]

# 仮利用者から販売数を受け取り（後で置き換える）
goods1_count = 0
goods2_count = 0
goods3_count = 0
goods4_count = 0

goods_count_list = [goods1_count, goods2_count, goods3_count, goods4_count]
sum_amount = 0  # グローバル変数として宣言

def input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count):
    product_num = input('購入する商品番号（支払いに進む場合はc）')
    if product_num == "c":
        checkout(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count, goods_name_list)
    elif product_num == '1':
        goods1_count += 1
        sum_amount += 180
        input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)
    elif product_num == '2':
        goods2_count += 1
        sum_amount += 320
        input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)
    elif product_num == '3':
        goods3_count += 1
        sum_amount += 500
        input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)
    elif product_num == '4':
        goods4_count += 1
        sum_amount += 200
        input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)
    else:
        print('存在しない番号です。')
        input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)

def checkout(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count, goods_name_list):
    print('商品', '数量')
    if goods1_count > 0:
        print(goods_name_list[0], goods1_count)
    if goods2_count > 0:
        print(goods_name_list[1], goods2_count)
    if goods3_count > 0:
        print(goods_name_list[2], goods3_count)
    if goods4_count > 0:
        print(goods_name_list[3], goods4_count)
    print('===')
    print(f'合計{sum_amount}円')

    while True:
        money = input('現金を投入してください>')
        try:
            money = int(money)
            if money < sum_amount:
                print('金額が不足しています')
                return
            break
        except ValueError:
            print('金額が不足しています')
            return    

    change = money - sum_amount
    print(f'おつり{change}円です。')
    goods_count_list = [goods1_count,goods2_count,goods3_count,goods4_count]
    import Manager
    main(goods_count_list)

def purchaser(goods_list, goods_name_list):
    print('　　商品　　　金額')
    print('================================================================')
    print(f'1.ワッフル   {goods_list[0]}円')
    print(f'2.クレープ   {goods_list[1]}円')
    print(f'3.豚タン   {goods_list[2]}円')
    print(f'4.ベビーカステラ   {goods_list[3]}円')
    print('-----------------------------')
    input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)
    
def main(goods_count_list):
    print("***********************")
    print(" 券売機シミュレータ")
    print("***********************")

    print("Please Enter (Enterキー押下で画面がクリアされて処理が進む)\n             (ESCキー押下で管理画面に処理が進む)\n             (qキー押下でシミュレータ終了)\n")
    place_key = ord(getch())
    if place_key == 13:
        # 利用者画面へ
        goods_count_list = purchaser(goods_list, goods_name_list)
    if place_key == 27:
        print(goods_count_list)
        # 管理画面へ
        from Manager import manager
        manager(goods_name_list, goods_list, goods_count_list)
    if place_key == ord("q"):
        # fin
        pass

main(goods_count_list)