
n = int(input())
wt = list(map(float,input().split()))

wt.sort(reverse=True)
#trips = []
trip = 0
i = 0
while i < len(wt):
    diff = 3.00 - wt[i]
    #no1 = wt[i]
    wt.remove(wt[i])
    
    n1 = [x for x in wt if x<=diff]
    if len(n1) == 0:
        trip += 1
        #trips.append(no1)
    else:
        n1 = max(n1)
        wt.remove(n1)
        #print(n1)
        trip += 1
       # trips.append([no1,n1])
    #print(wt)
print(trip)
#print(trips)