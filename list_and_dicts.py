def run():
    my_list = [1, "Hello", True, 5.4]
    my_dict = {"firtname":"Dennys", "lastname":"Ferrer"}

    super_list = [
        {"firtname":"Dennys", "lastname":"Ferrer"},
        {"firtname":"Dennys", "lastname":"Ferrer"},
        {"firtname":"Dennys", "lastname":"Ferrer"},
        {"firtname":"Dennys", "lastname":"Ferrer"}
    ]

    super_dict = {
        "natural nums": [1,2,3,5,7],
        "list name": ["Dennys", "Alexis", "Ferrer", "Yanez"]
    }

    for key, value in super_dict.items():
        print (f'La llave es {key} y el valor es {value}')

    for value in super_list:
        print (value)

if __name__ == '__main__':
    run()