def contar_caracteres(s):
    """Função para contar os caracteres de um sprit

    Ex:

    >>> contar_caracteres('gui')
    {'g': '1', 'i': '1', 'u': '1'}
     >>> contar_caracteres('banana')
     {'a': '3', 'b': '2', 'n': '2'}

    :param s: sprit

     """

    resultado = {}

    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
         


    return resultado

if __name__ == '__main__':
    print(contar_caracteres('gui'))
    print()
    print(contar_caracteres('banana'))