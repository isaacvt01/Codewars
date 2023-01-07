'''Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid.
'''


def high(x):
    abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
    string_separado = x.split()
    suma_final = 0
    for i in string_separado:
        suma_cada_uno = 0

        for j in i:
            suma_cada_uno += (abecedario.index(j) + 1)

        if suma_cada_uno > suma_final:
            suma_final = suma_cada_uno
            palabra_mayor_punt = i
        else:
            continue
    return palabra_mayor_punt


print(high('man i need a taxi up to ubud'))
