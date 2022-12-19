def descending_order(num):
    pasar_num_a_string = str(num)
    hacer_lista_num = list(pasar_num_a_string)
    nueva_lista_con_int = []
    for item in hacer_lista_num:
        nueva_lista_con_int.append(item)
    nueva_lista_con_int = nueva_lista_con_int.sort
    pasar_lista_a_string = ''.join(nueva_lista_con_int)
    alreves_num = int(pasar_lista_a_string)
    return alreves_num


if __name__ == "__main__":

    assert descending_order(0) == 0
    assert descending_order(15) == 51
    assert descending_order(123456789) == 987654321