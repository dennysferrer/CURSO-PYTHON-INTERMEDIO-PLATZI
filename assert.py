def divisors(num):
    divisors = [i for i in range(1, num + 1) if (num % i == 0)]
    return divisors

def run():
    num = input("Digite un numero: ")
    assert num.isnumeric(), "Por favor ingrese un numero entero positivo"
    print(divisors(int(num)))
    print("Termino mi programa ...")



if __name__ == '__main__':
    run()