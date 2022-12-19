def comp(array1, array2):
    for num in array1:
        num = num**2
        numero_veces = array2.count(num)
        if numero_veces == 0:
            return False
    return True


if __name__ == "__main__":
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        assert comp(a1, a2) == True
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*21, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
        assert comp(a1, a2) == False
        a1 = [121, 144, 19, 161, 19, 144, 19, 11]
        a2 = [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
        assert comp(a1, a2) == False
