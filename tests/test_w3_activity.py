import sys
import os
from collections import deque

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.w3_activity import (
    lavar_stack,
    atender_cola,
    intercalar_colas,
    ordenar_cola
)


def test_lavar_stack():
    stack = deque(['plato', 'sartén', 'bowl'])
    instrucciones = [('lavar', ), ('lavar', ), ('nuevo', 'cuchara'), ('lavar', )]
    expected = deque(['plato'])
    result = lavar_stack(stack, instrucciones)
    assert result == expected


def test_atender_cola():
    cola = deque(['María', 'Felipe', 'Carlos'])
    instrucciones = [('nueva', 'Alejandra'), ('atender', ),
                    ('colar', 'Rocío', 1), ('atender', )]
    expected = deque(['Rocío', 'Carlos', 'Alejandra'])
    result = atender_cola(cola, instrucciones)
    assert result == expected


def test_intercalar_colas():
    cola_1 = deque([1, 2, 3, 4])
    cola_2 = deque([5, 6, 7, 8])
    expected = deque([1, 5, 2, 6, 3, 7, 4, 8])
    result = intercalar_colas(cola_1, cola_2)
    assert result == expected


def test_ordenar_cola():
    cola = deque([4, -1, -3, 6, 2, 5])
    expected = deque([-3, -1, 2, 4, 5, 6])
    result = ordenar_cola(cola)
    assert result == expected