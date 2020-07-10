from math import factorial as fact

ip = input().split(',') #34,89,6,321,53,45,2211,81

sumOf = [sum(list(map(int,x))) for x in ip ] #find sum of each digit
count = [x for x in sumOf if sumOf.count(x)>1] # find sum whose count is more than 1
count = [ count.count(x) for x in set(count) ]  # 
'''
nCr = n!/(n-r)! r!
'''
total = 0
comb = lambda x: fact(x)/(fact((x-2))*2)

for i in count:
    total += comb(i)
print(int(total))

