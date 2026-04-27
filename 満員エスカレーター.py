from queue import Queue

"""
ついに、paiza 君の経営する会社は長年の工事の末、大阪から東京へ移動することができる一方通行の上京エスカレーターを完成させました。
しかし、このエスカレーターには体重の合計が X kg を超えると故障してしまうという問題点がありました。
そこで、故障を防ぐために乗り降りの様子を管理することにしました。

エスカレーターの乗り降りの内容が与えられるので、
全ての乗り降りが終わった時点でエスカレーターに乗っている人数と乗っている人の体重の総和を求めてください。

なお、エスカレーターの乗り降りの内容は以下のいずれかの形式で与えられます。

・ride K w_1 w_2 ... w_K
体重が w_1 kg の人から順に合計 K 人の人がエスカレーターに乗る。
体重が w_i kg の人が乗ることで、エスカレーターに乗っている人の体重の総和が X kg を超えてしまう場合、体重が w_i の人はエスカレーターに乗らない。

・get_off K
エスカレーターの先頭から K 人が降りる。
エスカレーターの乗員が K 人未満の場合、全員降りる
"""

#エスカレーターの乗り降りの回数 N とエスカレーターの耐荷重 X
N,X = map(int,input().split())
sum_weight = 0

escalator_queue = Queue()

for _ in range(N):
    orders = input().split()
    action = orders[0]

    if action == "ride":
        K = int(orders[1])   #K人乗る
        for i in range(K):
            weight = int(orders[i+2])
            if sum_weight + weight > X:     #重量がXを超えるようには乗らない
                pass
            else:
                escalator_queue.enqueue(weight)
                sum_weight += weight

    elif action == "get_off":
        K = int(orders[1])   #K人降りる

        rest_num = escalator_queue.size()

        if rest_num <= K:
            for _ in range(rest_num):
                weight = escalator_queue.dequeue()
                sum_weight -= weight
        else:
            for _ in range(K):
                weight = escalator_queue.dequeue()
                sum_weight -= weight

#エスカレーターに乗ってる人数と合計体重を表示
print(escalator_queue.size())
print(sum_weight)

