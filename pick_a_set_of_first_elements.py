import codewars_test as test
def first(seq, n=1): 
    contador = 1
    lista_final = []
    if n > len(seq):
        return seq
    while contador <= n:
        lista_final.append(seq[contador-1])
        contador = contador + 1

    return lista_final



@test.describe('Example Tests')
def example_tests():
    seq = ['a', 'b', 'c', 'd', 'e']
    test.assert_equals(first(seq), ['a'])
    test.assert_equals(first(seq, 0), []);
    test.assert_equals(first(seq, 1), ['a']);
    test.assert_equals(first(seq, 2), ['a', 'b']);
    test.assert_equals(first(seq, 10), ['a', 'b', 'c', 'd', 'e'])