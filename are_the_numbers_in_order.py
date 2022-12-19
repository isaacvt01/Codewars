def in_asc_order(arr):
    i = 0
    contador = 0
    for i in arr:
        if i < arr[contador + 1]:
            contador =+ 1
        elif i > arr[contador + 1]:
            return False
    return True

        






if __name__ == "__main__":
    arr = [1, 2]
    assert in_asc_order(arr) == True

    arr = [2, 1]
    assert in_asc_order(arr) == False
   
    arr = [1, 2, 3]
    assert in_asc_order(arr) == True
    arr = [3, 2, 1]
    assert in_asc_order(arr) == False