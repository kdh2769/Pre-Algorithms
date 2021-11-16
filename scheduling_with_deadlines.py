# scheduling with Deadlines (greedy)
# 0번째 작업은 공백
# 작업시간은 '1' 이라 가정


def feasible(K, deadline):
    '''
    now_time = 0
    for i in K:
        now_time+=1
        if (now_time > deadline[i]):
            return False
    '''
    for i in range (1, len(K)+1):
        if (i > deadline[K[i-1]]):
            return False
    return True

def schedule (deadline):
    n = len(deadline) -1
    j = [1]
    for i in range (2, n+1):
        K = insert(j, i, deadline)
        if (feasible(K, deadline)):
            j = K[:]
    return j

def insert (j ,i ,deadline):
    K = j[:]
    for q in range (len(K)-1,-1, -1):
        if (deadline[i] >= deadline[K[q]]):
            q+=1 # 해당 위치에서 q+1 위치에 insert 되어야 한다.
            break
    K.insert(q, i) # q_min = 0
    return K


deadline = [0, 3, 1, 1, 3, 1, 3, 2]
profit = [0, 40, 35, 30, 25, 20, 15 ,10]
J = schedule(deadline)
print ('schedule :', J)

best_profit = 0
for i in J:
    best_profit += profit[i]

print (best_profit)

