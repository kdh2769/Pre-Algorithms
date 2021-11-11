
# Dijkstra
# Node : 0번째 부터 시작

def dijkstra (W):
    # 1. 초기화 단계
    n = len(W)
    F = []
    touch = n * [0]
    length = n * [0]
    save_length = n * [0]
    for i in range (1, n):
        touch[i] = 0
        length[i] = W[0][i]

    # 2. 가장 가까운 정점 찾고 F에 추가
    for _ in range(n - 1):
        minValue = INF
        for i in range(1, n):
            if (0 <= length[i] < minValue):
                minValue = length[i]
                vnear = i
        edge = (touch[vnear], vnear)

        F.append(edge)
        # 3. 길이 찾아주기
        save_length[vnear] = length[vnear]

        # 4. touch 리스트에서 길이 업데이트
        for i in range(1, n):

            if (length[i] > length[vnear] + W[vnear][i]):
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear

        # 5. 이미 지나간 정점은 거르기
        length[vnear] = -1

    return save_length, list(reversed(F))


INF = 1000

W = [
    [0, 7, 4, 6 , 1],
    [INF, 0, INF, INF ,INF],
    [INF, 2, 0, 5, INF],
    [INF, 3, INF, 0, INF],
    [INF, INF, INF, 1, 0],
    ]

D, F = dijkstra(W)

print ("(touch (vnear), vnear) : ", F)
print ("최단거리 : ",D)


