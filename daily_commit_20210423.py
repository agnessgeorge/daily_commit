# 4.23 friday
all_words = input("Type in: ")
all_words_split = all_words.split(' ')

single_words = []
for i in all_words_split:
    if i not in single_words:
        single_words.append(i) 
    else:
        continue
single_words.sort()
print((' ').join(single_words))