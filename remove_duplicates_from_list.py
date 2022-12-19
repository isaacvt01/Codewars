from os import remove
import codewars_test as test
def distinct(seq):
    for item in seq:
        contador_item = seq.count(item)
        if contador_item > 1:
            seq.remove(item)
        else:
            continue
    return seq





@test.describe("Fixed Tests")
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(distinct([1]), [1])
        test.assert_equals(distinct([1, 2]), [1, 2])
        test.assert_equals(distinct([1, 1, 2]), [1, 2])
        test.assert_equals(distinct([1, 1, 1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
        test.assert_equals(distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]), [1, 2, 3, 4, 5, 6, 7])