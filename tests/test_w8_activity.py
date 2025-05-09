import sys
import os
from src.w8_activity import (distribucion_clientes, prob_compra_edad)

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
)

test_data = [
    ['User ID', 'Gender', 'Age', 'AnnualSalary', 'Purchased'],
    [1, 'Male', 25, 90000, 1],
    [2, 'Male', 50, 110000, 1],
    [3, 'Female', 32, 105000, 0],
    [4, 'Female', 60, 80000, 1],
    [5, 'Male', 38, 40000, 0],
    [6, 'Female', 45, 107500, 1],
    [7, 'Male', 55, 120000, 0],
    [8, 'Female', 27, 95000, 1],
    [9, 'Female', 22, 150000, 1],
]


def test_distribucion_clientes():
    expected = [
        [1, 1, 0, 0, 1, 1],  # Male
        [1, 0, 1, 1, 2, 0]   # Female
    ]
    assert distribucion_clientes(test_data) == expected


def test_prob_compra_edad():
    expected = {
        '20-29': 1.0,
        '30-39': 0.0,
        '40-49': 1.0,
        '50-59': 0.5,
        '60-69': 1.0
    }
    assert prob_compra_edad(test_data) == expected