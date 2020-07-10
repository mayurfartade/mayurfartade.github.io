
ip1 = input()
ip2 = input()

longestCommonSubstring = ''

for i in range(len(ip1)):
    for j in range(i,len(ip1)):
        if ip1[i:j+1] in ip2:
            if len(longestCommonSubstring) < len(ip1[i:j+1]):
                longestCommonSubstring = ip1[i:j+1]
print(longestCommonSubstring)