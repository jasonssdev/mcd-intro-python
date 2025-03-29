from datetime import datetime
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.w2_activity import (
    vuelos_disponibles,
    vuelo_mas_barato,
    aplicar_descuento,
    vuelos_con_escala
)

# flights base
vuelos_base = [
    ['Santiago', 'Puerto Montt', 35000, 30, '11-01-2024'],
    ['Santiago', 'Concepción', 30000, 40, '12-02-2024'],
    ['Concepción', 'Puerto Montt', 22000, 50, '13-02-2024'],
    ['Santiago', 'Puerto Montt', 20000, 2, '19-01-2024'],
    ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024'],
    ['Concepción', 'Puerto Montt', 22000, 50, '25-01-2024'],
    ['Antofagasta', 'Santiago', 27000, 14, '08-04-2024']
]

def test_vuelos_disponibles_returns_correct_matches():
    expected = [
        ['Santiago', 'Puerto Montt', 35000, 30, '11-01-2024'],
        ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024']
    ]
    result = vuelos_disponibles(vuelos_base, 'Santiago', 'Puerto Montt', 5)
    assert result == expected

def test_vuelo_mas_barato_returns_cheapest_flight():
    expected = ['Santiago', 'Puerto Montt', 12000, 100, '20-03-2024']
    result = vuelo_mas_barato(vuelos_base, 'Santiago', 'Puerto Montt')
    assert result == expected

def test_vuelo_mas_barato_returns_none_if_no_match():
    result = vuelo_mas_barato(vuelos_base, 'Valdivia', 'Osorno')
    assert result is None

def test_aplicar_descuento_applies_correct_discount():
    vuelos_test = [fila[:] for fila in vuelos_base]  # copia manual
    aplicar_descuento(vuelos_test, 'Santiago', 'Puerto Montt', 0.1)

    actual = [
        vuelo[2] for vuelo in vuelos_test
        if vuelo[0] == 'Santiago' and vuelo[1] == 'Puerto Montt'
    ]
    expected = [31500.0, 18000.0, 10800.0]
    assert actual == expected

def test_vuelos_con_escala_returns_valid_tuples():
    expected = [
        (
            ['Santiago', 'Concepción', 30000, 40, '12-02-2024'],
            ['Concepción', 'Puerto Montt', 22000, 50, '13-02-2024']
        )
    ]
    result = vuelos_con_escala(vuelos_base, 'Santiago', 'Puerto Montt')
    assert result == expected