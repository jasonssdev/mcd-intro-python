def distribucion_clientes(lista):
    tabla = [
            [0, 0, 0, 0, 0, 0],  
            [0, 0, 0, 0, 0, 0]   
        ]
    for person in lista[1:]:
        user_id, gender, age, salary, purchased = person
        if gender == 'Male':
            row_index = 0
        else:
            row_index = 1
        if salary < 100000:
            if age < 30:
                column_index = 0
            elif 30 <= age <= 53:
                column_index = 1
            else:
                column_index = 2
        else:
            if age < 30:
                column_index = 3
            elif 30 <= age <= 53:
                column_index = 4
            else:
                column_index = 5

        tabla[row_index][column_index] += 1
    return tabla


def prob_compra_edad(lista):  
    total_purchases_by_group = dict()
    total_customers_by_group = dict()

    for person in lista[1:]:
        _, _, age, _, purchased = person

        start = (age // 10) * 10
        end = start + 9
        key = f"{start}-{end}"

        if key not in total_purchases_by_group:
            total_purchases_by_group[key] = 0
            total_customers_by_group[key] = 0

        total_customers_by_group[key] += 1
        if purchased == 1:
            total_purchases_by_group[key] += 1

    diccionario = dict()
    for key in total_customers_by_group:
        probabilidad = total_purchases_by_group[key] / total_customers_by_group[key]
        diccionario[key] = round(probabilidad, 2)
    return diccionario