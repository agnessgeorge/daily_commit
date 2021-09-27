def pig_latin_translator(sentence):
    words = [str(word) for word in sentence.split()]
    con = 'bcdfghjklmnpqrstvwxyz'
    vow = 'aeiou'
    new_sentence = []

    for word in words:
        if (word[0] in con) and (word[1] in vow):
            new_word = word[1:] + word[0] + 'ay'
        elif (word[0] in con) and (word[1] in con):
            new_word = word[2:] + word[0] + word[1] + 'ay'
        elif word[0] in vow:
            new_word = word + 'way'
        new_sentence.append(new_word)
    return " ".join(new_sentence)


print(pig_latin_translator('happy birthday'))
print(pig_latin_translator('child'))
print(pig_latin_translator('awesome girl'))
print(pig_latin_translator('mr robot are you there'))
print(pig_latin_translator('agimoto'))
