import codewars_test as test
def duty_free(price, discount, holiday_cost):
    discount_price = (price * discount) / 100
    return (holiday_cost // discount_price)

test.describe("Basic tests")
test.assert_equals(duty_free(12, 50, 1000), 166)
test.assert_equals(duty_free(17, 10, 500), 294)
    
