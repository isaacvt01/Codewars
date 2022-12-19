import codewars_test as test
def sum_even_numbers(seq):
    pares_sumador = 0
    if seq == []:
        return 0
    for item in seq:
        if item % 2 == 0:
            pares_sumador = pares_sumador + item
        else:
            continue
    return pares_sumador


@test.describe("Simple integers input.")
def example_tests():
    test.assert_equals(sum_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 30)
    test.assert_equals(sum_even_numbers([]), 0)