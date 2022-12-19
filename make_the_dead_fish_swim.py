import codewars_test as test
def parse(data):
    lista_numeros = []
    valor = 0
    for item in data:
        if item == "i":
            valor = valor + 1
        if item =="o":
            lista_numeros.append(valor)
        if item == "d":
            valor = valor - 1
        if item == "s":
            valor = valor**2
    return lista_numeros















@test.describe("Sample tests")
def fixed_tests():
    @test.it("Some examples")
    def tests():
        test.assert_equals(parse("ooo"), [0,0,0])
        test.assert_equals(parse("ioioio"), [1,2,3])
        test.assert_equals(parse("idoiido"), [0,1])
        test.assert_equals(parse("isoisoiso"), [1,4,25])
        test.assert_equals(parse("codewars"), [0])