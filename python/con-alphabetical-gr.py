
ip = input()

dic = {}

for i in ip:
    if i.lower() not in dic.keys():
        dic[i.lower()] = i
    else:
        dic[i.lower()] = dic[i.lower()] + i

dic = dict(sorted(dic.items()))
li = list(dic)
le = len(li)

for i in range(0,le//2):
    print(dic[li[i]]+dic[li[le-1-i]],end='')
print(dic[li[le//2]])