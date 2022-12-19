def arr(n): 
    lista = []
    i = 0
    if n is None:
        return []
    while i < n:
        lista.append(i)
        i += 1
    return lista





if __name__ == "__main__":
        assert arr(4) == [0,1,2,3]
        assert arr(0) == []
        assert arr() == []