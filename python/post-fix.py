ip = input()

stack = []
sym = ['*','/','+','-']

for i in ip:
    if i in sym:
        t1 = stack.pop()
        t2 = stack.pop()
        stack.append(t2+i+t1)
    else:
        stack.append(i)
print(stack)
print(eval(''.join(stack)))