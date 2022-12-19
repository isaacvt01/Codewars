import codewars_test as test
def nb_year(p0, percent, aug, p):
    resultado = 0
    contador = 0
    while p0 < p:
       p0 = int(p0*(1 + percent/100)) + aug
       contador = contador + 1
    return contador





@test.describe("nb_year")
def tests():
    @test.it("basic tests")
    def basics():
        test.assert_equals(nb_year(1500, 5, 100, 5000), 15)
        test.assert_equals(nb_year(1500000, 2.5, 10000, 2000000), 10)
        test.assert_equals(nb_year(1500000, 0.25, 1000, 2000000), 94)