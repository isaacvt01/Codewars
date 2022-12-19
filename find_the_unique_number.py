import codewars_test as test
def find_uniq(arr):
    ordenada = sorted(arr)
    if ordenada[0] == ordenada[1]:
        return ordenada[-1]
    return ordenada[0]





    



@test.describe("Basic Tests")
def f():
    @test.it("Simple tests")
    def _():
        test.assert_equals(find_uniq([ 1, 1, 1, 2, 1, 1 ]), 2)
        test.assert_equals(find_uniq([ 0, 0, 0.55, 0, 0 ]), 0.55)
        test.assert_equals(find_uniq([ 3, 10, 3, 3, 3 ]), 10)