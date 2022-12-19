import codewars_test as test
def squares(x, n):
    lista_final = []
    contador = 0
    num_potenciado = x
    lista_final.append(num_potenciado)
    if n <= 0:
        return []
    while contador < n-1:
        num_potenciado = num_potenciado**2
        lista_final.append(num_potenciado)
        contador = contador + 1
    return lista_final



test.assert_equals(squares(2, 5), [2, 4, 16, 256, 65536])
test.assert_equals(squares(3, 3), [3, 9, 81])
test.assert_equals(squares(5, 3), [5, 25, 625])
test.assert_equals(squares(10, 4), [10, 100, 10000, 100000000])
test.assert_equals(squares(2, 0), [])
test.assert_equals(squares(2, -4), [])
