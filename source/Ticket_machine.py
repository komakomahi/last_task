from msvcrt import getch

def input_num(sum_amount, goods_name_list, goods_list, goods_count_list):
    product_num = input('購入する商品番号（支払いに進む場合はc）')
    if product_num == "c":
        checkout(sum_amount, goods_name_list, goods_list, goods_count_list)
    elif product_num == '1':
        goods_count_list[0] += 1
        sum_amount += goods_list[0]
        input_num(sum_amount, goods_name_list, goods_list, goods_count_list)
    elif product_num == '2':
        goods_count_list[1] += 1
        sum_amount += goods_list[1]
        input_num(sum_amount, goods_name_list, goods_list, goods_count_list)
    elif product_num == '3':
        goods_count_list[2] += 1
        sum_amount += goods_list[2]
        input_num(sum_amount, goods_name_list, goods_list, goods_count_list)
    elif product_num == '4':
        goods_count_list[3] += 1
        sum_amount += goods_list[3]
        input_num(sum_amount, goods_name_list, goods_list, goods_count_list)
    else:
        print('存在しない番号です。')
        input_num(sum_amount, goods_name_list, goods_list, goods_count_list)

def checkout(sum_amount, goods_name_list, goods_list, goods_count_list):
    print('商品', '数量')
    if goods_count_list[0] > 0:
        print(goods_name_list[0], goods_count_list[0])
    if goods_count_list[1] > 0:
        print(goods_name_list[1], goods_count_list[1])
    if goods_count_list[2] > 0:
        print(goods_name_list[2], goods_count_list[2])
    if goods_count_list[3] > 0:
        print(goods_name_list[3], goods_count_list[3])
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
    import Manager
    main(goods_name_list, goods_list, goods_count_list)

def purchaser(goods_name_list, goods_list, goods_count_list):
    print('　　商品　　　金額')
    print('================================================================')
    print(f'1.ワッフル   {goods_list[0]}円')
    print(f'2.クレープ   {goods_list[1]}円')
    print(f'3.豚タン   {goods_list[2]}円')
    print(f'4.ベビーカステラ   {goods_list[3]}円')
    print('-----------------------------')
    sum_amount = 0
    input_num(sum_amount, goods_name_list, goods_list, goods_count_list)
    
def main(goods_name_list, goods_list, goods_count_list):
    print("***********************")
    print(" 券売機シミュレータ")
    print("***********************")

    print("Please Enter (Enterキー押下で画面がクリアされて処理が進む)\n             (ESCキー押下で管理画面に処理が進む)\n             (qキー押下でシミュレータ終了)\n")
    place_key = ord(getch())
    if place_key == 13:
        # 利用者画面へ
        goods_count_list = purchaser(goods_name_list, goods_list, goods_count_list)
    if place_key == 27:
        # 管理画面へ
        from Manager import manager
        manager(goods_name_list, goods_list, goods_count_list)
    if place_key == ord("q"):
        # fin
        exit()

