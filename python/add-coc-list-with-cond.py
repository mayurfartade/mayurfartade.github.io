
ip = input().split(',')

ind_5 = ip.index('5')
ind_8 = ip.index('8')

no = ip[0:ind_5] + ip[ind_8+1:len(ip)]

sum_no = sum(list(map(int,no)))

no2 = int(''.join(ip[ind_5:ind_8+1]))

print(sum_no + no2)