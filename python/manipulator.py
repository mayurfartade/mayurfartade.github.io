
ip = list(input())

for i in range(len(ip)):
    if ip[i] == '#':
        j = i-1
        while ip[j] == '#':
            j -= 1
       
        if ord(ip[j]) + 1 > 90:
            ip[j] = chr(64 + ord(ip[j]) - 90)
        else:
            ip[j] = chr(ord(ip[j]) + 1)
print(''.join([x for x in ip if x != '#']))


