from collections import deque

def lavar_stack(stack, instrucciones):
    while len(stack) > 0:
        for i in instrucciones:
            if i[0] == "lavar":
                stack.pop()
            elif i[0] == "nuevo":
                stack.append(i[1])
        return stack


def atender_cola(cola, instrucciones):
    for i in instrucciones:
        if i[0] == "nueva":
            cola.append(i[1])
        elif i[0] == "atender":
            cola.popleft()
        elif i[0] == "colar":
            cola.insert(i[2], i[1])
    return cola


def intercalar_colas(cola_1, cola_2):
    new_cola = deque()
    for i, j in zip(cola_1, cola_2):
        new_cola.append(i)
        new_cola.append(j)
    return new_cola


def ordenar_cola(cola):
    new_cola = deque(sorted(cola))
    return new_cola

