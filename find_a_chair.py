import codewars_test as test
def meeting(rooms, need):
    sillas_cogidas = []
    conteo_sillas = 0
    if need == 0:
        return 'Game On'
    for item in rooms:
        if conteo_sillas >= need:
            break
        personas_num = item[0].count('X')
        sillas_num = item[1]
        if sillas_num >= personas_num:
            sillas_libres = sillas_num - personas_num
            sillas_cogidas.append(sillas_libres)
            conteo_sillas = conteo_sillas + sillas_libres
        if sillas_num < personas_num:
            sillas_cogidas.append(0)
    if conteo_sillas < need:
        return 'Not enough!'
        
    return sillas_cogidas













test.describe("Basic tests")
test.assert_equals(meeting([["XXX", 3], ["XXXXX", 6], ["XXXXXX", 9]], 4), [0, 1, 3])
test.assert_equals(meeting([["XXX", 1], ["XXXXXX", 6], ["X", 2], ["XXXXXX", 8], ["X", 3], ["XXX", 1]], 5), [0, 0, 1, 2, 2])
test.assert_equals(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 0), "Game On")
test.assert_equals(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 8), "Not enough!")
test.assert_equals(meeting([["XX", 2], ["XXXX", 6], ["XXXXX", 4]], 2), [0, 2])