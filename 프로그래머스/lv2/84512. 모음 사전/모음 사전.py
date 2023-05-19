from itertools import product
def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    word_list = []
    for i in range(1, 6):
        for j in product(vowels, repeat=i):
            word_list.append(''.join(j))
    word_list.sort()
    return word_list.index(word) + 1