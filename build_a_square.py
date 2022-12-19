def generate_shape(n):
    signo_mas = ('+' * n) + '\n'
    mult_signo = signo_mas * n
    return mult_signo[:-1]

print (generate_shape(8))
