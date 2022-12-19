import codewars_test as test
def first_n_smallest(arr, n):
    result = []
    array_sort = sorted(arr)
    array_ordenada = array_sort[:n]

    for elem in arr:
        if elem in array_ordenada:
            result.append(elem)
            array_ordenada.remove(elem)
    return result











test.assert_equals(first_n_smallest([1,2,3,4,5],3), [1,2,3])
test.assert_equals(first_n_smallest([5,4,3,2,1],3), [3,2,1])
test.assert_equals(first_n_smallest([1,2,3,1,2],3), [1,2,1])
test.assert_equals(first_n_smallest([1,2,3,-4,0],3), [1,-4,0])
test.assert_equals(first_n_smallest([1,2,3,4,5],0), [])
test.assert_equals(first_n_smallest([1,2,3,4,5],5), [1,2,3,4,5])
test.assert_equals(first_n_smallest([1,2,3,4,2],4), [1,2,3,2])
test.assert_equals(first_n_smallest([2,1,2,3,4,2],2), [2,1])
test.assert_equals(first_n_smallest([2,1,2,3,4,2],3), [2,1,2])
test.assert_equals(first_n_smallest([2,1,2,3,4,2],4), [2,1,2,2])

