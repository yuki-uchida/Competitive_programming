N, M, K = list(map(int, input().split()))

friendships = []
blocks = []

for _ in range(M):
    friendships.append(list(map(int, input().split())))
for _ in range(K):
    blocks.append(list(map(int, input().split())))

# aとbの間が友達関係なら友達候補

# N人の友達候補の数をだす
# 友達候補==自分から友達関係を伝って相手にたどり着ける AND 自分と相手がブロック関係にない
# 隣接行列を作って、深さ優先探索or幅優先探索でたどり着ける相手を記録。たどり着けた相手をlistに入れて、ブロック関係にある相手を外せば、残ったのが友達候補
for i in range(N):
