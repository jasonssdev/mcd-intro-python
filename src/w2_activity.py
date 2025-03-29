from datetime import datetime

def vuelos_disponibles(vuelos, origen, destino, pasajeros):
    lista_de_vuelos = []
    for vuelo in vuelos:
        if origen == vuelo[0] and destino == vuelo[1] and pasajeros <= vuelo[3]:
            lista_de_vuelos.append(vuelo)
    return lista_de_vuelos

def vuelo_mas_barato(vuelos, origen, destino):
    lista_de_vuelos_mas_baratos = []
    for vuelo in vuelos:
        if origen == vuelo[0] and destino == vuelo[1]:
            lista_de_vuelos_mas_baratos.append(vuelo)
    if not lista_de_vuelos_mas_baratos:
        return None
    vuelo_barato = lista_de_vuelos_mas_baratos[0]
    for vuelo in lista_de_vuelos_mas_baratos:
        if vuelo[2] < vuelo_barato[2]:
            vuelo_barato = vuelo
    return vuelo_barato

def aplicar_descuento(vuelos, origen, destino, porcentaje):
    for vuelo in vuelos:
        if origen == vuelo[0] and destino == vuelo[1]:
            vuelo[2] = vuelo[2] * (1- porcentaje)
    return vuelos

def vuelos_con_escala(vuelos, origen, destino):
    vuelos_escala = []
    for vuelo_origen in vuelos:
        if vuelo_origen[0] == origen:
            ciudad_escala = vuelo_origen[1]
            for vuelo_destino in vuelos:
                if vuelo_destino[0] == ciudad_escala and vuelo_destino[1] == destino:
                    fecha_origen = datetime.strptime(vuelo_origen[4], "%d-%m-%Y")
                    fecha_destino = datetime.strptime(vuelo_destino[4], "%d-%m-%Y")

                    if fecha_origen < fecha_destino:
                        vuelos_escala.append((vuelo_origen, vuelo_destino))

    return vuelos_escala