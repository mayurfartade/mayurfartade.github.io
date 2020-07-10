 
p = list(map(int,input().split()))

k = int(input())

counter = -1
while all(p):
    counter += 1
    a = [x for x in p if x>=k ]
    if len(a):
        p[p.index(max(a))] -= k
    else:
        p[p.index(max(p))] = 0

if counter%2 == 0:
    print("Sam")
else:
    print("Alex")

'''
sum of array % k == 
'''