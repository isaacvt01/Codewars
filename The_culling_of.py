import codewars_test as test
def purify(s: str) -> str:
    
    for item in s:
        if item == 'i' or item == 'I':
            index_letra = s.find(item)
            s = s[:index_letra - 1] + ' ' +  s[index_letra + 2:]
        else:
            continue
    return s





test.assert_equals(purify("CHILI"), "C")
test.assert_equals(purify("The eradication of the citizens of Stratholme"), "The eraan of the ens of Stratholme")

test.it("The resulting sentence should not contain leading or trailing white spaces")

test.assert_equals(purify("Kimi Imimi goes to our school"), "goes to our school")
test.assert_equals(purify("In heaven all the interesting people are missing"), "heaven all the teresg people are g")

test.it("All words in the resulting sentence should be separated by a single space")

test.assert_equals(purify("5I5 i39i9i1 139iii39i i5i9i 1"), "13 1")
test.assert_equals(purify("TIL that TIL means Today I learned"), "that means Today learned")
test.assert_equals(purify("zippity duppity bopity bip ZIPPITY DUPPITY BOPITY BIP"), "y dupy boy Y DUPY BOY")
test.assert_equals(purify("Six sick hicks nick six slick bricks with picks and sticks"), "k ks k sk bks h ks and sks")
test.assert_equals(purify("Do not go skiing in the summer"), "Do not go sg the summer")
test.assert_equals(purify("Id id ieididi eeiiowe diid owodiid"), "ewe owo")