class Envio:

    def __init__(self, emisor, receptor):
        self.emisor = emisor
        self.receptor = receptor

    def enviar(self):
        print(f"Enviado desde {self.emisor} a {self.receptor}")

class Carta(Envio):
    def __init__(self, emisor, receptor):
        super().__init__(emisor, receptor)
        self.estampilla = False

    def poner_estampilla(self):
        self.estampilla = True

    def enviar(self):
        if self.estampilla:
            super().enviar()


class Paquete(Envio):

    def __init__(self, emisor, receptor, max_volumen):
        super().__init__(emisor, receptor)
        self.max_volumen = max_volumen
        self.productos = []
        self.cerrado = False

    def agregar_producto(self, peso, volumen):
        if self.cerrado:
            self.cerrado = False
        self.productos.append((peso, volumen))

    def cerrar(self):
        volumen_total = 0
        for producto in self.productos:
            volumen_total += producto[1]
        if volumen_total < self.max_volumen:
            self.cerrado = True

    def enviar(self):
        peso_total = 0
        for producto in self.productos:
            peso_total += producto[0]
        if self.cerrado and peso_total <= 30:
            super().enviar()
