from collections import Counter

n = int(input())
word = []
for o in range(n):
    word.append(input())
counts = []
     
print(len(set(word)))
print(*Counter(word).values())