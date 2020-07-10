
arr = list(map(int,input().split(',')))
le = len(arr)
arr.sort()
fib = []
for i in range(0,le):
    for j in range(i+1,le) :

        
        a = arr[i]
        b = arr[j]
        fi = [a,b]
        while True:
            t = a
            a = b
            b = t + a
            if b in arr:
                fi.append(b)
                continue
            else:
                break
        if len(fi) > 2:    
            fib.append(fi)        
le = []     
for i in range(len(fib)):
   if len(fib[i]) > len(le):
       le = fib[i]
print(le)        
