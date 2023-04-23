def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Dennys", "lastname": "Ferrer"}

    super_list = [
        {
            "firstname": "Dennys",
            "lastname":"Ferrer"
        },
        {
            "firstname": "Lourdes",
            "lastname": "Camaron"
        },
        {
            "firstname": "Pedro",
            "lastname": "Perez"
        },
    ]

    for dict in super_list:
        print (dict)

    super_dict = {
        "natural_nums" : [1,2,3,4,5,6],
        "colores":["Amarillo", "Azul", "Rojo"],
        "integers_nums" : [-1,0,1,2,3,4]
    }

    for key, value in super_dict.items():
        print(f'{key}: {value}')


if __name__ == '__main__':
    run()
