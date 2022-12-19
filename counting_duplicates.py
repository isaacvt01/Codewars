import codewars_test as test
def duplicate_count(text):
    letras_repetidas_cont = 0
    lista_repetidos = []
    text = text.lower()
    if text == '':
        return 0
    for item in text:
        if text.count(item) > 1 and item not in lista_repetidos:
            letras_repetidas_cont = letras_repetidas_cont + 1
            lista_repetidos.append(item)
        else:
            continue
    return letras_repetidas_cont








@test.describe("Fixed Tests")
def fixed_tests():
    @test.it("Basic Tests")
    def basic_tests():
        test.assert_equals(duplicate_count(""), 0)
        test.assert_equals(duplicate_count("abcde"), 0)
        test.assert_equals(duplicate_count("abcdeaa"), 1)
        test.assert_equals(duplicate_count("abcdeaB"), 2)
        test.assert_equals(duplicate_count("Indivisibilities"), 2)