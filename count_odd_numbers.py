import codewars_test as test
def odd_count(n):
    # impares_num = 0
    # for i in range(1, n):
    #     if i % 2 != 0:
    #         impares_num += 1
    #     else:
    #         continue
    # return impares_num
    # impares_num = 0
    # lista_vacia = []
    # for i in range(1, n):
    #     if i %2 != 0:
    #         lista_vacia.append(i)
    # return len(lista_vacia)
    return n // 2

        





test.assert_equals(odd_count(15),7)
test.assert_equals(odd_count(15023),7511)