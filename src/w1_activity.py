def calcular_promedio(tupla: tuple) -> tuple:
    """
    calculate the averege of number in the tuple

    Args:
    tupla: tuple with name and numbers

    Returns:
    tuple with name and average of numbers
    """
    name = tupla[0]
    average = sum(tupla[1:]) / len(tupla[1:])
    return (name, average)

tupla = ('Camila', 5.0, 6.2, 4.8, 6.0)
print(calcular_promedio(tupla))

def agregar_entero(lista: list, entero: int) -> list:
    """
    add an integer to the list in the right position to keep the list sorted

    Args:
    lista: list with numbers
    entero: integer to add

    Returns:
    list with the integer added
    """
    lista.append(entero)
    lista.sort()            
    return lista

lista = [-40, -1, 2, 5, 16, 72, 100]
entero = 13
print(agregar_entero(lista, entero))

def contar_repeticiones(lista: list) -> int:
    """
    count the number with the most repetitions in the list

    Args:
    lista: list with numbers

    Returns:
    repetition of the number with the most repetitions
    """
    dict_counter = {}
    for num in lista:
        if num in dict_counter:
            dict_counter[num] += 1
        else:
            dict_counter[num] = 1
    repetition = max(dict_counter.values())
    return repetition

lista = [1, 4, 3, 1, 4, 2, 5, 1, 2, 4, 1, 3, 1, 2, 4]
print(contar_repeticiones(lista))

def agregar_estudiante(lista: list, estudiante: str) -> list:
    """
    add a student to the list in the right position to keep the list sorted by last name then first name"

    Args:
    lista: list with students
    estudiante: student to add

    Returns:
    list with the student added in the right position to keep the list sorted
    """
    lista.append(estudiante)
    lista.sort(key=lambda name: (name.split()[1], name.split()[0]))
    return lista

lista = ['Francisca Avedaño', 'Pablo Avedaño', 'Juan Bravo', 'Javiera Hernández', 'Mario Huerta', 'David Morales', 'Eliza Morales']
estudiante = 'Daniela Gomez'
print(agregar_estudiante(lista, estudiante))