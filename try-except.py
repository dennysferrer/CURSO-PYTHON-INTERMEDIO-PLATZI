
def run():
    palabra = input('Digite una palabra: ')
    try:
        if (len(palabra) == 0):
            raise ValueError('No se puede ingresar una cadena vacia...')
        palindrome = lambda string: string == string[::-1]
        return palindrome
    except ValueError as ve:
        print(ve)
        return False



if __name__ == '__main__':
    run()