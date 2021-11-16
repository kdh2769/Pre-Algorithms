
# promising 조건
# 1. weight + total 이 W 보다 작은 경우는 False
# 2. weight + w[i+1] 값이 W 보다 초과하면 False

def promising(i, weight, total):
    if((weight + total >= W) and (weight == W or weight + w[i+1] <= W)):
        return 1
    else :
        return 0

def s_s(i, weight, total, include):
    n = len(w)
    if (promising(i, weight, total)):
        if (weight == W):
            print (include[0:n])
        else :
            # 다음 level을 포함 시켜준다.
            include[i+1] = 1
            s_s(i+1, weight + w[i+1], total - w[i+1], include)
            # 다음 level을 포함 시키지 않는다.
            include[i+1] = 0
            s_s(i+1, weight, total - w[i+1], include)


n = 6 # set 원소 개수
w = [1, 2, 3, 4, 5, 6]
W= 11 # subset 합

total = 0
for k in w:
    total += k # 남아있는 원소 합

include = [0]*(n)
print ('items =',w , ' W =',W )
s_s(-1, 0, total, include)