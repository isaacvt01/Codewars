import codewars_test as test
def shorter_reverse_longer(a,b):
    if len(a) == len(b):
        return b + a[::-1] + b
    if len(a) > len(b):
        return b + a[::-1] + b
    if len(a) < len(b):
        return a + b[::-1] + a

    

test.assert_equals(shorter_reverse_longer("first", "abcde"),"abcdetsrifabcde");
test.assert_equals(shorter_reverse_longer("hello", "bau"),"bauollehbau");
test.assert_equals(shorter_reverse_longer("abcde", "fghi"),"fghiedcbafghi");