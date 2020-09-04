
from string import ascii_lowercase

def find_length(start, end, N, list_of_words):
    
    if start == end:
        return 0

    count = 0
    len_word = len(start)

    queue = [start]


    while len(queue):
        count += 1

        len_queue = len(queue)
        for _ in range(len_queue):
            word = queue.pop(0)
            
            #print(queue)
            
            for index in range(len_word):
                char = word[index]
                word = list(word)

                for c in ascii_lowercase:
                    word[index] = c

                    if str(''.join(word)) == end:
                        return count 
                    
                    if str(''.join(word)) not in list_of_words:
                        continue
                    list_of_words.remove(str(''.join(word)))

                    queue.append(str(''.join(word)))
                
                word[index] = char

            '''while i <(len(list_of_words)):
                z = [x for x in word if x in list_of_words[i] ]
                #if len(set(word)) - len(set(list_of_words[i]).intersection(set(word))) == 1:
                if len(word) - len(z) == 1:
                    #print(list_of_words[i])
                    if list_of_words[i] == end:
                        print(word_hopper)
                        return len(word_hopper) + 1

                    word_hopper.append(list_of_words[i])
                    temp += 1
                    queue.append(list_of_words[i])
                    list_of_words.remove(list_of_words[i])
                i += 1
            '''
        
    return 0






start = input()
end = input()

N = int(input())

list_of_words = []

for _ in range(N):
    list_of_words.append(input())

#print(list_of_words)

list_of_words.append(end)

print(find_length(start, end, N, list_of_words))




'''
git
dog
6
got
dot
log
fog
mot
pkm
'''
'''
toon
plea
6
poon
plee
same
poie
plie
poin

'''