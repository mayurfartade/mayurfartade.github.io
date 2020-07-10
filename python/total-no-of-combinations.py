from itertools import combinations

ip = list(map(int,input().split()))
su = int(input())

comb = list(combinations(ip,4))
print(comb)
for i in comb:
    
    if sum(i) == su:
        print(i)