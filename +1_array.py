def up_array(arr):
    if arr == []:
        return None
    contador = len(arr)
    lista_final = []
    for item in arr:
        if item < 0:
            return None
        if item > 9:
            return None
        item = item * (10**(contador-1))
        lista_final.append(item)
        contador = contador - 1
    sumar_lista = (sum(lista_final)) + 1
    lista_final =list(map(int, str(sumar_lista)))
    while arr[0] == 0 and len(arr) > 1:
        arr.remove(0)
        lista_final.insert(0, 0)
    return lista_final

print (up_array([0, 0, 9]))

