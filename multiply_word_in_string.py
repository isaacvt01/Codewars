from audioop import mul
import codewars_test as test
def modify_multiply(st, loc, num):
    dividir_string = st.split()
    mult_string = (dividir_string[loc] + '-') * num 
    mult_string = mult_string[:-1]
    return mult_string











@test.describe("Fixed test")
def test_group():
    @test.it("Example tests")
    def test_case():
        test.assert_equals(modify_multiply("This is a string",3 ,5), "string-string-string-string-string", "The string is incorrect")
        test.assert_equals(modify_multiply("Creativity is the process of having original ideas that have value. It is a process; it's not random.",8 ,10), "that-that-that-that-that-that-that-that-that-that")
        test.assert_equals(modify_multiply("Self-control means wanting to be effective at some random point in the infinite radiations of my spiritual existence",1 ,1), "means")
        test.assert_equals(modify_multiply("Is sloppiness in code caused by ignorance or apathy? I don't know and I don't care.",6 ,8), "ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance-ignorance")
        test.assert_equals(modify_multiply("Everything happening around me is very random. I am enjoying the phase, as the journey is far more enjoyable than the destination.",2 ,5), "around-around-around-around-around")