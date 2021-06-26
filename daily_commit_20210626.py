import collections
def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']

    
def occ_words(words):
    ctr = collections.Counter(words)
    unique_words = []
    freq = []
    for wrd in words:
        if wrd not in unique_words:
            unique_words.append(wrd)
            freq.append(ctr[wrd])
    print(*freq)
    
    
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1
    return score
    occ_words(words)


n = int(input())
words = input().split()
print(score_words(words))