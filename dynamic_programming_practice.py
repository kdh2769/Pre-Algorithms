# utility file
def printMatrix (d):
    m = len(d)
    n = len(d[0])

    for i in range (0, m):
        for j in range(0, n):
            print(f'{d[i][j]:4d}', end=" ")
        print()

def printMatrixF(d):
    n = len(d[0])
    for i in range(0, n):
        for j in range(0, n):
            print(f'{d[i][j]:5.2f}', end=" ")
        print()

def print_inOrder(root):
    if not root :
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return

    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)

# hw5 1번 문제
print ('-' * 15, "1번 문제", '-' * 15)

class Node :
    def __init__(self, data):
        self.l_child = None
        self.r_child = None
        self.data = data


def tree(key, r, i, j):
    k = r[i][j]
    if (k==0):
        return

    else :
        p = Node (key[k])
        p.l_child = tree(key, r, i, k-1)
        p.r_child = tree(key, r, k+1, j)
        return p



key = ["", "A", "B", "C", "D"]
p = [0, 0.375, 0.375, 0.125, 0.125]
n = len(p)-1

a = [[0 for j in range(0, n+2)]for i in range(0, n+2)]
r = [[0 for j in range(0, n+2)] for i in range(0, n+2)]

for i in range (1, n+1):
    a[i][i-1] = 0
    a[i][i] = p[i]
    r[i][i] = i
    r[i][i-1] = 0

a[n+1][n] = 0
r[n+1][n] = 0

for diagonal in range(1, n):
    for i in range(1, n-diagonal+1):
        j = i + diagonal
        min_v = 1000
        min_k = 0
        for k in range(i, j+1):
            if (a[i][k-1] + a[k+1][j]) < min_v:
                min_v = a[i][k-1]+a[k+1][j]
                min_k = k
        res = 0

        for m in range(i, j+1):
            res = res + p[m]

        a[i][j] = min_v + res
        r[i][j] = min_k


printMatrixF(a)
print()
printMatrix(r)

root = tree(key, r, 1, n)
print_inOrder(root)
print()
print_preOrder(root)

# hw5 2번 문제

print ('-' * 15, "2번 문제", '-' * 15)

a = ['A', 'A', 'C', 'A', 'G', 'T', 'T', 'A', 'C', 'C']
b = ['T', 'A', 'A', 'G', 'G', 'T', 'C', 'A']

m = len(a)
n = len(b)

table = [[0 for j in range(0, n+1)]for i in range(0, m+1)]
minindex = [[(0, 0) for j in range(0, n+1)] for i in range(0, m+1)]

for j in range(n-1, -1, -1):
    table[m][j] = table[m][j+1]+2

for i in range(m-1, -1, -1):
    table[i][n] = table[i+1][n]+2

# 구현

for i in range(m-1, -1, -1):
    for j in range(n-1, -1, -1):
        tmep = 0

        if (a[i] != b[j]):
            tmep = 1
        table[i][j] = table[i+1][j+1] + tmep
        minindex[i][j] = (i+1, j+1)

        if (table[i][j] > table[i+1][j]+2):
            table[i][j] = table[i+1][j]+2
            minindex[i][j] =(i+1, j)

        if (table[i][j] > table[i][j+1]+2):
            table[i][j] = table[i][j+1]+2
            minindex[i][j] = (i, j+1)


printMatrix(table)
x = 0
y = 0

while (x < m and y < n):
    tx, ty = x, y
    print(minindex[x][y])
    (x, y)= minindex[x][y]
    if x == tx+1 and y == ty+1 :
        print (a[tx], " ", b[ty])

    elif x == tx and y == ty + 1:
        print (" - ", " ", b[ty])

    else:
        print (a[tx], " ", " -")

