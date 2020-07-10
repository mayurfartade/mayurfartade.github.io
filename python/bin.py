'''
# I/P: 1 2 6 100
# O/P: 621100
no = list(''.join(input().split()))
no.sort(reverse=True)
print(''.join(no))

'''

no = list(map(int,input().split()))
nos = sorted(no)
nos = dict(enumerate(nos))
nos = dict([(value,key) for key,value in nos.items()])
print(nos)
for i in no:
    print(nos[i],end=' ')