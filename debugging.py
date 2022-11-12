def divisors(num):
    divisors = [i for i in range(1, num + 1) if (num % i == 0)]
    return divisors

def run():
    try:
        num = int(input("Digite un numero: "))
        if (num <= 0):
            raise ValueError('Digite un numero entero positivo ...')
        print(divisors(num))
        print("Termino mi programa ...")

    except ValueError as ve:
        print(ve)
        return False


if __name__ == '__main__':
    run()