from queue import Queue

"""
paiza 君と kyoko さんは、キューの勉強の一環としてキューを使ったキューじゃんけんをすることにしました。
キューじゃんけんのルールは次の通りです。

・各プレイヤーはゲーム開始前に、じゃんけん N 回分の手が書かれたブロック（グー・チョキ・パーのいずれか）が入ったキューを作っておく。
・ゲームが始まったら、次の 3 つの手順をじゃんけん 1 回として、合計 K 回じゃんけんを行い、勝った回数が多い方が勝利となる。

1. 各プレイヤーは自分のキューの先頭に入っているブロックを取り出す。
2. お互いのブロックに書かれている手を確認し、通常のじゃんけんの通り勝敗を決定する。（ただし、あいこの場合であっても再度手を出さない）
3. 各プレイヤーは、出したブロックを「キューの末尾に挿入する」か、「追加せずに破棄する」かを決めて、その操作を行う。

各プレイヤーのはじめのキューの中身と、K 回のじゃんけんの 3. における選択が与えられるので、キューじゃんけんの勝敗を判定してください。
なお、K 回のじゃんけんの途中でキューが空になるような入力は与えられないことが保証されています。
"""

#最初にキューに入れるブロックの数 N, じゃんけんの回数 K 
N,K = map(int,input().split())

paiza_queue = Queue()
kyoko_queue = Queue()

paiza_win_count = 0
kyoko_win_count = 0


for _ in range(N):
    hands = input().split()
    paiza_queue.enqueue(hands[0])
    kyoko_queue.enqueue(hands[1])


for _ in range(K):
    paiza_hand = paiza_queue.dequeue()
    kyoko_hand = kyoko_queue.dequeue()

    #あいこの場合であっても再度手を出さない
    if(
        (paiza_hand == "P" and kyoko_hand == "R") or 
        (paiza_hand == "S" and kyoko_hand == "P") or 
        (paiza_hand == "R" and kyoko_hand == "S")
    ):
        paiza_win_count += 1 

    elif(
         (kyoko_hand == "P" and paiza_hand == "R") or 
         (kyoko_hand == "S" and paiza_hand == "P") or
         (kyoko_hand == "R" and paiza_hand == "S")
    ):
        kyoko_win_count += 1


    paiza_action,kyoko_action = input().split()
    
    if paiza_action == "push":
        paiza_queue.enqueue(paiza_hand)
    elif paiza_action == "discard":
        pass

    if kyoko_action == "push":
        kyoko_queue.enqueue(kyoko_hand)
    elif kyoko_action == "discard":
        pass

#勝者判定
if paiza_win_count > kyoko_win_count:
    print("paiza")
elif paiza_win_count < kyoko_win_count:
    print("kyoko")
else:
    print("draw")

    




