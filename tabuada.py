
#Tabuada em Pytho, um exercício básicp;


numero = int(input('Digite um número para as diferentes tabuadas! '))

print('Número digiado: ' .format(numero))









for i in range(1, 13):

    multiplicar = numero * i

    print('{} x {:2} = {}'.format(numero, i, multiplicar))

print('========'*200)

for i in range(1, 13):

    dividir = numero / i

    print('{} / {:2} = {}'.format(numero, i, dividir))

print('====='*100)

for i in range(1, 13):

    subtrair = numero - i

    print('{} - {:2} = {}'.format(numero, i, subtrair))







