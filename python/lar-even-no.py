import re
ip = input()

nos = list(set(re.findall('\d',ip)))

nos.sort(reverse=True)
no = int(''.join(nos))

if no % 2 == 0:
    print(no)
else:
    for i in range(len(nos)-2, 0, -1):
        if int(nos[i]) % 2 == 0:
            i = nos[i]
            nos.remove(i)
            nos.append(i)
            print(''.join(nos))
            break
    else:
        print(-1)