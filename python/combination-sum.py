#code
from itertools import combinations

for _ in range(int(input())):
    no = int(input())
    nos = list(map(int,input().split()))

    for i in range (len(nos)):
        comb = list(combinations(nos,i))
        for j in comb:
            if sum(j) == no:
                print(j)