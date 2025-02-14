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

from Ticket_machine import main
main(goods_name_list, goods_list, goods_count_list)
