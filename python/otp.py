
no = input()

no = no[1::2]

sq = ''.join(list(map(str,(list(map(lambda x: int(x)*int(x),no))))))
print(sq[0:5])
