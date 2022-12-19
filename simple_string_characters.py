import codewars_test as test
def solve(s):
    minusculas = ('a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z')
    mayusculas = ('A', 'E', 'I', 'O', 'U', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z')
    numeros = ('1', '2', '3', '4', '5', '6', '7', '8','9', '0')
    general = ('a', 'e', 'i', 'o', 'u', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z','A', 'E', 'I', 'O', 'U', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8','9', '0' )
    minusculas_cuenta = 0
    mayusculas_cuenta = 0
    numeros_cuenta = 0
    caracteres_cuenta = 0
    lista_cuentas = []
    for item in s:
        if item in minusculas:
            minusculas_cuenta = minusculas_cuenta + 1
            continue
        if item in mayusculas:
            mayusculas_cuenta = mayusculas_cuenta + 1
        if item in numeros:
            numeros_cuenta = numeros_cuenta + 1
        if item not in general:
            caracteres_cuenta = caracteres_cuenta + 1
    

    lista_cuentas.append(mayusculas_cuenta)
    lista_cuentas.append(minusculas_cuenta)
    lista_cuentas.append(numeros_cuenta)
    lista_cuentas.append(caracteres_cuenta)
    return lista_cuentas



test.it("Basic tests")
test.assert_equals(solve("Codewars@codewars123.com"),[1,18,3,2])
test.assert_equals(solve("bgA5<1d-tOwUZTS8yQ"),[7,6,3,2])
test.assert_equals(solve("P*K4%>mQUDaG$h=cx2?.Czt7!Zn16p@5H"),[9,9,6,9])
test.assert_equals(solve("RYT'>s&gO-.CM9AKeH?,5317tWGpS<*x2ukXZD"),[15,8,6,9])
test.assert_equals(solve("$Cnl)Sr<7bBW-&qLHI!mY41ODe"), [10,7,3,6])
test.assert_equals(solve("@mw>0=QD-iAx!rp9TaG?o&M%l$34L.nbft"), [7,13,4,10])