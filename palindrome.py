
def run():
    palabra = input('Digite la palabra: ')
    palindrome = lambda string: string == string[::-1]

    if(palindrome(palabra)):
        print('La palabra ingresada es palindromo')
    else:
        print('La palabra ingresada no es palindromo')


if __name__ == '__main__':
    run()