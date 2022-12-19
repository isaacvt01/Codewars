def square_digits(num):
    potenciar_num_lista = []
    contador = 0
    tamaño_num = len(str(num))
    num_actual = 0 
    while contador < tamaño_num:
        num_actual = str(num)[contador]
        num_actual = int(num_actual) ** 2
        num_actual = str(num_actual)
        potenciar_num_lista.append(num_actual)
        contador = contador + 1
        num_actual = 0
    final_lista = ''.join(potenciar_num_lista)
    final_lista = int(final_lista)
    return final_lista










if __name__ == "__main__":
rn    assert square_digits(9119) == 811181
    assert square_digits(0) == 0