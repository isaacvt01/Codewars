import codewars_test as test
def better_than_average(class_points, your_points):
    nuevo_num = 0
    for item in class_points:
        nuevo_num = nuevo_num + item
    divisor = len(class_points)
    resultado = nuevo_num / divisor
    if resultado < your_points:
        return True
    else:
        return False

test.describe("Basic Tests")

test.it("better_than_average([2, 3], 5) should return True")
test.assert_equals(better_than_average([2, 3], 5), True)

test.it("better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75) should return True")
test.assert_equals(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75), True)

test.it("better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69) should return True")
test.assert_equals(better_than_average([12, 23, 34, 45, 56, 67, 78, 89, 90], 69), True)

test.it("better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50) should return False")
test.assert_equals(better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50), False)

test.it("better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21) should return False")
test.assert_equals(better_than_average([29, 55, 74, 60, 11, 90, 67, 28], 21), False)
