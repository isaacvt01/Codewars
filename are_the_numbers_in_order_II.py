def in_asc_order(arr):
    new_list = list(arr)
    new_list.sort()
    if new_list == arr:
        return True
    else:
        return False



if __name__ == "__main__":
    arr = [1, 2]
    assert in_asc_order(arr) == True

    arr = [2, 1]
    assert in_asc_order(arr) == False
   
    arr = [1, 2, 3]
    assert in_asc_order(arr) == True
    arr = [3, 2, 1]
    assert in_asc_order(arr) == False