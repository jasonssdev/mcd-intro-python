import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.w4_activity import (
    precio_total,
    precio_por_mes,
    productos_frecuentes,
    gasto_productos
)

boletas = [
    {
        'fecha_compra': '29-05-23',
        'precio': 11800,
        'productos': {
            'Chocolate': (1, 2300),
            'Mantequilla': (1, 2500),
            'Huevos': (12, 4000),
            'Pan': (1, 3000)
        }
    },
    {
        'fecha_compra': '31-05-23',
        'precio': 5200,
        'productos': {
            'Pan': (1, 3000),
            'Leche': (2, 2200)
        }
    },
    {
        'fecha_compra': '01-06-23',
        'precio': 6800,
        'productos': {
            'Mantequilla': (2, 5000),
            'Azúcar': (1, 1800)
        }
    }
]


def test_precio_total():
    expected = 23800
    result = precio_total(boletas)
    assert result == expected


def test_precio_por_mes():
    expected = {
        '05-23': 17000,
        '06-23': 6800
    }
    result = precio_por_mes(boletas)
    assert result == expected


def test_productos_frecuentes():
    expected = {'Pan', 'Mantequilla'}
    result = productos_frecuentes(boletas)
    assert result == expected


def test_gasto_productos():
    expected = {
        'Chocolate': 2300,
        'Mantequilla': 7500,
        'Huevos': 4000,
        'Pan': 6000,
        'Leche': 2200,
        'Azúcar': 1800
    }
    result = gasto_productos(boletas)
    assert result == expected