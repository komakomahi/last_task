# # それぞれの金額
# goods_name_list = ["1.ワッフル", "2.クレープ", "3.豚タン", "4.ベビーカステラ"]
# goods_list = [180, 320, 500, 200]

def sum_checkout(goods_name_list, goods_list, goods_count_list):
    print(goods_count_list)
    all_sum_amount = 0
    for x in range(4):
        all_sum_amount += goods_list[x] * goods_count_list[x]
    return all_sum_amount


def manager_num(manager_code, goods_name_list, goods_list, goods_count_list):
    if manager_code == 1:
        code1_event(goods_name_list, goods_list, goods_count_list)
        print_goods(goods_name_list, goods_list, goods_count_list)
    elif manager_code == 2:
        code2_event(goods_name_list, goods_list, goods_count_list)
        print_goods(goods_name_list, goods_list, goods_count_list)
    elif manager_code == 3:
        code3_event(goods_name_list, goods_list, goods_count_list)
    else:
        print("管理者コードが正しくありません。")
        
def code1_event(goods_name_list, goods_list, goods_count_list):
    print("===")
    for x in range(4):
        goods_count_list[x] = 0
    print("売上をリセットしました。\n")
    
def code2_event(goods_name_list, goods_list, goods_count_list):
    print("===")
    change_number = int(input("価格を変更する商品の番号を入力してください。 >"))
    if change_number <= 0 or change_number > 4:
        print("正しい商品番号を入力してください。\n")
    else:
        change_amount = int(input("変更金額を入力してください。 >"))
        print(f"【{goods_name_list[change_number - 1]}  {change_amount}】円に変更します。")
        check_yn = input("よろしいですか（Y/N) >")
        if check_yn.upper() == "Y":
            goods_list[change_number - 1] = change_amount
            print("変更しました。\n")
            
def code3_event(goods_name_list, goods_list, goods_count_list):
    get_enter = input("Enterキー押下でタイトル画面の表示に戻る\n")
    if get_enter == "":
        # ここでメインに戻るーーーーー
        from Ticket_machine import main
        main(goods_count_list)

def print_goods(goods_name_list, goods_list, goods_count_list):
    print("======= 商品一覧 =======")
    print("商品      単価  販売数  売上金額")
    print("=======================")

    for num in range(4):
        print(f"{goods_name_list[num]} {goods_list[num]}円  {goods_count_list[num]}  {goods_list[num]*goods_count_list[num]}")
        
    print("———")
    print(f"総売上金額  {sum_checkout(goods_name_list, goods_list, goods_count_list)}円\n")

    print("=== 管理メニュー ====")
    print("1. 売上をリセットする")
    print("2. 商品の価格を変更する")
    print("※売上がリセットされていないと利用できません。")
    print("3. 管理画面を終了する")
    print("———")
    manager_code = int(input("管理コード入力:"))

    # 不正な受け取りに対するエラー文も出せるようにしておこう！！
    manager_num(manager_code, goods_name_list, goods_list, goods_count_list)
    
# 表示
def manager(goods_name_list, goods_list, goods_count_list):
    print ("***********************")
    print("       管理画面        ")
    print ("***********************\n")
    print_goods(goods_name_list, goods_list, goods_count_list)
    
    
    