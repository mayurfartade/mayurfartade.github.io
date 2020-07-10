
ip = input()

mid = len(ip) // 2

for i in range(mid, 0 ,-1):
    prefix = ip[0:i]
    suffix = ip[len(ip)-i : len(ip)]
    if prefix == suffix:
        print(len(prefix))
        break
else:
    print(-1)