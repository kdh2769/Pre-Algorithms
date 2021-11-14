# n-Queens problem 에서 2번째 답안 출력 및 총 경우의 수 출력
# 첫번째 depth는 0 (1 아님!!)

def promising(i, col):
    k = 0
    flag = True
    while (k < i and flag ):
        if (col[i] == col[k] or abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

def queens(n, i, col):
    global count
    if (promising(i, col)):
        if (i == n - 1):
            count += 1
            if (count == 2):
                print("두번째 경우 :", col)
        else:
            for j in range(0, n):
                col[i + 1] = j
                queens(n, i + 1, col)

count = 0

n = 7

col = n * [0]
queens(n, -1, col)
print("경우의 수 :", count)