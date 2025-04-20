import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from src.w5_activity import (Planta, Casa, Menu, Enemigo)


def test_crear_planta():
    planta = Planta('Washingtonia filifera', 15)
    assert planta.especie == 'Washingtonia filifera'
    assert planta.altura == 15


def test_crear_casa():
    casa = Casa('Frente al mall 321', 1, 1, 20.0, True)
    assert casa.direccion == 'Frente al mall 321'
    assert casa.piezas == 1
    assert casa.baños == 1
    assert casa.metros_cuadrados == 20.0
    assert casa.urbana is True
    assert casa.precio() == 140.00
    casa_no_urbana = Casa('Frente al lago 123', 2, 2, 50, False)
    assert casa_no_urbana.precio() == 200.00


def test_crear_menu():
    menu = Menu(['Pato a la mostaza', 'Hamburguesa', 'Ensalada', 'Lasagna'],
                [20000, 8000, 6000, 9000])
    assert menu.comidas == [
        'Pato a la mostaza', 'Hamburguesa', 'Ensalada', 'Lasagna'
    ]
    assert menu.precios == [20000, 8000, 6000, 9000]
    assert str(
        menu
    ) == "Pato a la mostaza: 20000\nHamburguesa: 8000\nEnsalada: 6000\nLasagna: 9000"


def test_crear_enemigo():
    a = Enemigo('Esqueleto', 8, 6)
    b = Enemigo('Zombie', 10, 5)
    assert str(a) == 'Esqueleto - 8'
    assert str(b) == 'Zombie - 10'
    a.recibir_ataque(5)
    assert a.vida == 3
    assert str(a) == 'Esqueleto - 3'
    a.atacar(b)
    assert b.vida == 4
    assert str(b) == 'Zombie - 4'
    a.atacar(b)
    assert b.vida == 0
    assert str(b) == 'Zombie - 0'

def test_recibir_ataque_excede_vida():
    enemigo = Enemigo("Orco", 5, 3)
    enemigo.recibir_ataque(10) 
    assert enemigo.vida == 0