'''
https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/a-game-of-numbers-1-5d3a8cb3/
'''

def g(z,N):
    global A
    i = z
    z = z+1
    while z < N:
        if A[i] > A[z]:
            print(A[z], end=" ")
            break
        z += 1
    else:
        print(-1, end=' ')

def f(i,N):
    global A
    z = i + 1
    while z < N:
        if A[i] < A[z]:
            g(z,N)
            break
        z += 1
    else:
        print(-1, end=' ')
            


N = int(input())
A = []
for _ in range(N):
    A.append(int(input()))

for i in range(N):
    f(i,N)



