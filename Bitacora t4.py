#hecho en base al lenguaje visual basic
#importamos la libreria para expresiones regulares
import re
#debemos seleccionar el archivo de entrada, en el que se debe encontrar el codigo fuente
archivo = open('calculation.vb', mode='r')
texto = archivo.read()
archivo.close()

n = 0
while n!=6:
    print()
    print('Menu de opciones - seleccione una opción')
    print()
    print('1 = Variables validas\n2 = Enteros y decimales\n3 = Expresiones aritmeticas\n4 = Operadores condicionales\n5 = Cadenas de caracteres\n6 = Salir del programa ')
    n = int(input())

    resultado = []
    if n == 1 :
        print()
        print('Variables válidas')
        print()
        reservadas=[ 'Dim','As','If','Then','ElseIf','End','Double','String','End','Public','Class','Sub','And']
        for item in re.finditer('[a-zA-Z]+[a-zA-Z0-9_]*',texto):
            if item.group() in reservadas: 
                print
            else:
                if item.group() in resultado: 
                    print
                else:
                    resultado.append(item.group())
    if n == 2:
        print()
        print('Enteros y decimales')
        print()
        for item in re.finditer('\d+(\.\d+)?',texto):
            resultado.append(item.group())    
    if n == 3:
        print()
        print('Expresiones aritméticas')
        print()
        for item in re.finditer('(\d+(\.\d+)?|(\w+(\w\d)*))\s?(\+|-|\*|\/)\s?(\d+(\.\d+)?|(\w+(\w\d)*))',texto):
            resultado.append(item.group())   
    if n == 4:
        print()
        print('Operadores condicionales')
        print()
        for item in re.finditer('((\w+(\w\d)*)|(\d+(\.\d+)?))\s?(>=|<=|<|>|=)\s?((\w+(\w\d)*)|(\d+(\.\d+)?))',texto):
            resultado.append(item.group())   
    if n == 5:
        print()
        print('Cadenas de caracteres')
        print()
        for item in re.finditer('(("[^"]*")|(\'[^\']*\'))',texto):
            resultado.append(item.group())   
    elif n == 6:
        break
        print()

    print(resultado)

##termina el programa