from collections import deque
N, K = map(int, input().split())
towns = list(map(int, input().split()))

# 閉路を求める問題。閉路が見つかれば、あとはそれを掛け算するだけ

seen_points = set([])
indexes = [-1 for _ in range(N)]
now_town = 1
index = 0
while K > 0:
    # print(f'now_town={now_town}', K, seen_points)
    # すでに見つかっているところに戻ってきたなら閉路が見つかっているはず。
    if now_town in seen_points:
        # 閉路でかかるコストはroop_count
        roop_count = index - indexes[now_town - 1]
        # なので、省略する
        if K > roop_count:
            # print(K, roop_count)
            K = K % roop_count
        seen_points = set([])
        continue
    seen_points.add(now_town)
    indexes[now_town - 1] = index
    now_town = towns[now_town - 1]
    index += 1
    K -= 1

print(now_town)
