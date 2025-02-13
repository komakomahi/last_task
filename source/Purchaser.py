goods_name_list = ["1.ワッフル", "2.クレープ", "3.豚タン", "4.ベビーカステラ"]
goods_list = [180, 320, 500, 200]

goods1_count = 0
goods2_count = 0
goods3_count = 0
goods4_count = 0

sum_amount = 0

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
    import Main
    Main(goods_count_list)

def purchaser(goods_list, goods_name_list):
    print('　　商品　　　金額')
    print('================================================================')
    print('1.ワッフル')
    print('2.クレープ')
    print('3.豚タン')
    print('4.ベビーカステラ')
    print('-----------------------------')
    input_num(sum_amount, goods1_count, goods2_count, goods3_count, goods4_count)
    
purchaser(goods_list, goods_name_list)