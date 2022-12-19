import codewars_test as test
def vowel_one(s):
    s = s.lower()
    vowel = ('a', 'e', 'i', 'o', 'u')
    final_string = ''
    for item in s:
        if item in vowel:
            final_string = final_string + '1'
        if item not in vowel:
            final_string = final_string + '0'
    return final_string


test.describe("Example Tests")

tests = [
    # [input, expected],
    ["vowelOne", "01010101"],
    ["123, arou", "000001011"],
    ["Codewars", "01010100"],
    ["Python", "000010"]
]