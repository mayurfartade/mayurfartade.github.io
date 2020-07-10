
ip = input()
unique = ''
for i in range(0,len(ip)):

    for j in range(i+1,len(ip)):
       
        if len(ip[i:j+1]) == len(set(ip[i:j+1])) and len(unique) < len(set(ip[i:j+1])):
            unique = ip[i:j+1]
print(unique)
