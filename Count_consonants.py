'''Write a function consonantCount, consonant_count or ConsonantCount that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels'''


def consonant_count(s):
    consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n',  'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
    suma = 0
    s = s.lower()
    for i in s:
        if i in consonantes:
            suma += 1
        else:
            continue
    return suma


print(consonant_count(''))
