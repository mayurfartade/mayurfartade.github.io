no = list(map(int,input().split()))

nos = list(set(no))
nos.sort()

nos = {k : 0 for k in nos}

for i in no:
    nos[i] += 1

#max  = max([k for k,j in nos.items()])
print(max(nos, key=nos.get))