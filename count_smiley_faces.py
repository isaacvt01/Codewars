import codewars_test as test
def count_smileys(arr):
    contador = 0
    if arr == []:
        return 0
    for item in arr:
        if len(item) > 2:
            if item [0] == ':' or item [0] == ';':

                if item [1] == '-' or item [1] == '~':

                    if item [2] == ')' or item[2] == 'D':
                        contador = contador + 1
            else:
                continue
        if len(item) == 2:
            if item [0] == ':' or item [0] == ';':

                if item [1] == 'D' or item [1] == ')':
                    contador = contador + 1
            else: 
                continue
    return contador




test.describe("Basic tests")
test.assert_equals(count_smileys([]), 0)
test.assert_equals(count_smileys([':D',':~)',';~D',':)']), 4)
test.assert_equals(count_smileys([':)',':(',':D',':O',':;']), 2)
test.assert_equals(count_smileys([';]', ':[', ';*', ':$', ';-D']), 1)