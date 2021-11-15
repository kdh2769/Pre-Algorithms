print ('---1번 문제---')
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


n = 6

w = [1, 2, 3,4, 5,6]

W= 11

total = 0
for k in w:
    total += k

include = [0]*(n)
print ('items =',w , ' W =',W )
s_s(-1, 0, total, include)

