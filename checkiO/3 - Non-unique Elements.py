"""def checkio(lista):
    delete_num = []
    for num in lista: 
        if lista.count(num) < 2:
            lista.remove(num)
    return lista
"""
def checkio(lista):
    for num in set(lista):
        if lista.count(num) == 1:
            lista.remove(num)
    return lista


print(checkio([1, 2, 3, 1, 3]))       #== [1, 3, 1, 3]
print(checkio([1, 2, 3, 4, 5]))        #== []
print(checkio([5, 5, 5, 5, 5]))       #== [5, 5, 5, 5, 5]
print(checkio([10, 9, 10, 10, 9, 8])) #== [10, 9, 10, 10, 9]
