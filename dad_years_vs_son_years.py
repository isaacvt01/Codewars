import codewars_test as test
def twice_as_old(dad_years_old, son_years_old):
    contador = 0
    if dad_years_old > (son_years_old * 2):
        while dad_years_old > (son_years_old * 2):
            dad_years_old = dad_years_old -1
            contador = contador + 1
        return contador
    if dad_years_old < (son_years_old * 2):
        while dad_years_old < (son_years_old * 2):
            dad_years_old = dad_years_old +1
            contador = contador + 1

        return contador
    return contador

@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(twice_as_old(36,7) , 22)
        test.assert_equals(twice_as_old(55,30) , 5)
        test.assert_equals(twice_as_old(42,21) , 0)
        test.assert_equals(twice_as_old(22,1) , 20)
        test.assert_equals(twice_as_old(29,0) , 29)


    

            