import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))
)

from src.w6_activity import (Carta, Paquete)


def test_carta_no_envia_sin_estampilla(capsys):
    c = Carta("A", "B")
    c.enviar()
    captured = capsys.readouterr()
    assert captured.out == ""  # no debe imprimir nada


def test_carta_envia_con_estampilla(capsys):
    c = Carta("A", "B")
    c.poner_estampilla()
    c.enviar()
    captured = capsys.readouterr()
    assert "Enviado desde A a B" in captured.out


def test_paquete_no_envia_sin_cerrar(capsys):
    p = Paquete("Tienda", "Cliente", max_volumen=100)
    p.agregar_producto(10, 30)
    p.enviar()
    captured = capsys.readouterr()
    assert captured.out == ""  # no se debe enviar


def test_paquete_no_envia_si_pesa_mas_de_30kg(capsys):
    p = Paquete("Bodega", "Destino", max_volumen=100)
    p.agregar_producto(20, 50)
    p.agregar_producto(15, 30)  # peso total = 35
    p.cerrar()
    p.enviar()
    captured = capsys.readouterr()
    assert captured.out == ""  # no debe imprimirse nada


def test_paquete_envia_si_cerrado_y_ligero(capsys):
    p = Paquete("Depósito", "Cliente", max_volumen=100)
    p.agregar_producto(10, 40)
    p.agregar_producto(5, 30)
    p.cerrar()
    p.enviar()
    captured = capsys.readouterr()
    assert "Enviado desde Depósito a Cliente" in captured.out

def test_agregar_producto_reabre_paquete():
    p = Paquete("Origen", "Destino", max_volumen=100)
    p.agregar_producto(10, 20)
    p.cerrar()
    assert p.cerrado is True  # Verificamos que se cerró
    p.agregar_producto(5, 10)  # Esto debería reabrirlo
    assert p.cerrado is False  # ← Esto cubre la línea roja
    assert len(p.productos) == 2