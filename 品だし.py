from queue import Queue

"""
スーパーで働いている paiza 君は、お店に並んでいる商品一つひとつにつけられている識別番号の管理を任されました。
こちらのスーパーでは、棚に商品を補充する際はお客さんから最も遠い側（棚の末尾）に新しい商品を入れることになっています。
また、お客さんは棚の先頭の商品しか購入することができないようになっています。

商品の補充と購入に関する情報が時系列順に与えられるので、全ての補充と購入が終わった後に棚に残っている商品の識別番号を棚の先頭から順に答えてください。

なお、初め棚は空であるものとし、商品の補充と購入の情報は以下の形式で与えられるとします。

・add num
棚の末尾に識別番号が num の商品を 1 つ追加する。

・buy X
お客さんが棚の先頭から数えて X 個購入する。
"""

#商品の補充と購入の情報の個数 
N = int(input())

shelf_queue = Queue()

for _ in range(N):
    orders = input().split()

    #棚の末尾に識別番号が num の商品を 1 つ追加
    if orders[0] == "add":
        num = int(orders[1])    
        shelf_queue.enqueue(num)

    #お客さんが棚の先頭から数えて X 個購入
    elif orders[0] == "buy":
        #
        x = int(orders[1])

        for _ in range(x):
            shelf_queue.dequeue()

#棚に残っている商品の識別番号を棚の先頭から順に答える
shelf_queue.print_from_bottom()