ip = input()  #abcdaeiou

vowels = ['a','e','i','o','u']

i = 0
c = []
while i < len(ip):
    if ip[i] in vowels:
        j = i+1
        while j < len(ip):
            if ip[j] in vowels:
                j += 1
                continue
            else:
                c.append(ip[i:j])
                i = j+1
                break
        else:
            c.append(ip[i:j])
            i = j
    else:
        i += 1            
if len(c):
    print(max(c))
else:
    print(-1)