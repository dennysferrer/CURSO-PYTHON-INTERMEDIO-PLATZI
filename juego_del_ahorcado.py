import random


def read():
    palabrasArray = []
    with open("./archivos/palabras.txt", "r", encoding="utf-8") as f:
        for palabra in f:
            palabrasArray.append(palabra.strip('\n'))
    
    rangoLimite = len(palabrasArray) - 2

    numeroRamdom = random.randint(0,rangoLimite)

    palabraSelec = palabrasArray[numeroRamdom]

    return palabraSelec

def compararPalabra(palabra):

    palabraArray = []
    palabraNueva = []

    for letra in palabra:
        palabraArray.append(letra)
    
    print(f'La palabra tiene {len(palabraArray)} digitos ...\n')
    print(palabraArray)


    for oportunidad in range(0,10):

        try:
            letra = input('Digite una letra: ')
            index = palabraArray.index(letra)
            palabraNueva.insert(index, letra)

            print(palabraNueva)

            if (palabraNueva == palabraArray):
                print('Ganaste!! ...')
                break

        except ValueError:
            print('No existe la letra en la palabra ...')

    print('Perdiste!!! No adivinaste la palabra ...')
    

def run():
    print('##### JUEGO DEL AHORCADO #####')
    palabraSelect = read()
    compararPalabra(palabraSelect)

    
    




if __name__ == '__main__':
    run()
