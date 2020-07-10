'''
a b d e g o p q A D O P Q R 0 4 6 9  has only 1 bounded region
B 8 has 2 bounded regions.

ip: abcdef
op - 4 ( a,b,d,e has one bounded region i.e. 1*4 = 4)

'''

from re import findall as fa
ip = input()

bound1 = fa(r'[abdegopqADOPQR0469]',ip)
bound2 = fa(r'[B8]',ip)

#print(bound1,bound2)
print(len(bound1)+2*len(bound2))