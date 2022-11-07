import math

def run():
    dict = {i: i**3 for i in range(1,101) if (i % 3 != 0)}
    dict2 = {i: math.sqrt(i) for i in range(1,1000)}

    """ for numero in range(0,101):
        if (numero % 3 != 0):
            dict[numero] = numero**3 """

    # print(dict)
    print(dict2)
 

if __name__ == '__main__':
    run()