def precio_total(boletas):
    suma = 0
    for boleta in boletas:
        suma += boleta['precio']
    return suma

def precio_por_mes(boletas):
    d = dict()
    for boleta in boletas:
        fecha = boleta['fecha_compra'][3:]
        precio = boleta['precio']
        if fecha in d:
            d[fecha] += precio
        else:
            d[fecha] = precio
    return d

def productos_frecuentes(boletas):
    cincuenta_porciento = round(len(boletas)/2)
    contador = {}
    c = set()
    for boleta in boletas:
        productos_boleta = set(boleta['productos'].keys())
        for producto in productos_boleta:
            if producto in contador:
                contador[producto] += 1
            else:
                contador[producto] = 1

    for producto, cuenta in contador.items():
        if cuenta >= cincuenta_porciento:
            c.add(producto)
    return c

def gasto_productos(boletas):
    d = dict()
    for boleta in boletas:
        productos_boleta = boleta['productos']
        for producto, tupla in productos_boleta.items():
            if producto in d:
                d[producto] += tupla[1]
            else:
                d[producto] = tupla[1]
    return d