class Planta:

    def __init__(self, especie: str, altura: int):
        self.especie = especie
        self.altura = altura


class Casa:

    def __init__(self, direccion, piezas, baños, metros_cuadrados, urbana):
        self.direccion = direccion
        self.piezas = piezas
        self.baños = baños
        self.metros_cuadrados = metros_cuadrados
        self.urbana = urbana

    def precio(self):
        if self.urbana:
            precio_urbana = (self.piezas +
                             self.baños) * self.metros_cuadrados + 100
            return precio_urbana
        else:
            precio_no_urbana = (self.piezas +
                                self.baños) * self.metros_cuadrados
            return precio_no_urbana


class Menu:

    def __init__(self, comidas: list[str], precios: list[int]):
        self.comidas = comidas
        self.precios = precios

    def __str__(self):
        return "\n".join([
            f"{comida}: {precio}"
            for comida, precio in zip(self.comidas, self.precios)
        ])


class Enemigo:

    def __init__(self, nombre, vida, fuerza_ataque):
        self.nombre = nombre
        self.vida = vida
        self.fuerza_ataque = fuerza_ataque

    def recibir_ataque(self, daño):
        self.vida -= daño
        if self.vida < 0:
            self.vida = 0

    def atacar(self, otro):
        otro.vida -= self.fuerza_ataque
        if otro.vida < 0:
            otro.vida = 0

    def __str__(self):
        return f"{self.nombre} - {self.vida}"

