nos = list(map(int,input().split()))
k = int(input())

'''
no = { x:0 for x in sorted(list(set(nos)))}
for i in nos:
    no[i] += 1
for i,j in no.items():
    if j == k:
        print(i)
        break
'''

no = sorted(list(set(nos)))

for i in no:
    if nos.count(i) == k:
        print(i)
        break