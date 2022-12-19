def move_zeros(lst):
    numero_ocurrencias = lst.count(0)
    contador = 0
    while contador < numero_ocurrencias:
        contador = contador + 1
        lst.remove(0)
        lst.append(0)
    return lst







if __name__ == "__main__":
    assert move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]
    assert move_zeros( [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) == [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    assert move_zeros([0, 0]) == [0, 0]
    assert move_zeros([0]) == [0]
    assert move_zeros([]) == []