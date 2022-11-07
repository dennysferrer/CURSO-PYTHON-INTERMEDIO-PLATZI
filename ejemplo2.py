def run():
    lista = [i**2 for i in range(1,101) if i % 3 != 0]
    lista2 = [i for i in range(1,100000) if i % 36 == 0]

    """ for item in range(1,101):
        if (item % 3 != 0):
            lista.append(item**2) """

    # print(lista)
    print(lista2)

if __name__ == '__main__':
    run()