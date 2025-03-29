import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.w1_activity import (
    calcular_promedio,
    agregar_entero,
    contar_repeticiones,
    agregar_estudiante
)

def test_calcular_promedio_returns_correct_average():
    input_data = ('Camila', 5.0, 6.2, 4.8, 6.0)
    expected = ('Camila', 5.5)
    result = calcular_promedio(input_data)
    assert result == expected

def test_agregar_entero_adds_and_sorts_correctly():
    input_data = [-40, -1, 2, 5, 16, 72, 100]
    number_to_add = 13
    expected = [-40, -1, 2, 5, 13, 16, 72, 100]
    result = agregar_entero(input_data.copy(), number_to_add)
    assert result == expected

def test_contar_repeticiones_returns_max_frequency():
    input_data = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 1, 1]
    expected = 6
    result = contar_repeticiones(input_data)
    assert result == expected

def test_agregar_estudiante_adds_and_sorts_by_lastname():
    student_list = [
        'Francisca Avedaño', 'Pablo Avedaño', 'Juan Bravo',
        'Javiera Hernández', 'Mario Huerta',
        'David Morales', 'Eliza Morales'
    ]
    new_student = 'Daniela Gomez'
    expected = [
        'Francisca Avedaño', 'Pablo Avedaño', 'Juan Bravo',
        'Daniela Gomez', 'Javiera Hernández',
        'Mario Huerta', 'David Morales', 'Eliza Morales'
    ]
    result = agregar_estudiante(student_list.copy(), new_student)
    assert result == expected