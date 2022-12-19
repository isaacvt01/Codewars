import codewars_test as test
def is_pangram(s):
    s = s.lower()
    pangram = ('a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    for item in pangram:
        if item in s:
            continue
        if item not in s:
            return False
        
    return True


@test.describe("sample tests")
def sample_tests():
    
    @test.it("Should return true for a pangram")
    def test_pangram():        
        test.assert_equals(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)

    @test.it("Should return false for not a pangram")
    def test_not_pangram():        
        test.assert_equals(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)