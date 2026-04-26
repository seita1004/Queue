from queue import Queue

"""
まずはキューを扱う練習として 3 つのキューを用意して、それらに基本操作を行いましょう。
はじめ 3 つのキューは空です。
次のいずれかの指示が N 回与えられるので、入力された順番に指示通りの操作をしてください。
全ての指示が終わった後、各キューに含まれる要素を先頭から順に出力してください。

・push S X
S 番目のキューの末尾に X を追加する。

・pop S
S 番目のキューの先頭の要素を取り出す。
"""


queue_1 = Queue()
queue_2 = Queue()
queue_3 = Queue()

queue_list = [queue_1,queue_2,queue_3]

N = int(input())

for _ in range(N):
    orders = input().split()

    if orders[0] == "push":     #エンキュ―
        q_num = int(orders[1]) - 1
        x = int(orders[2])
        queue_list[q_num].enqueue(x)

    elif orders[0] == "pop":    #デキュー
        q_num = int(orders[1]) - 1 
        queue_list[q_num].dequeue()

    
for queue in queue_list:
    queue.print_from_bottom()
