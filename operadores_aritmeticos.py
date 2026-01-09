
#Operadores Aritméticos: Os operadores aritméticos existentes em Python são:
# SOMA (+)
# SUBTRAÇÃO (-)
#MULTIPLICAÇÃO (*)
#EXPONENCIAÇÃO (**)
#DIVISÃO(/)
#DIVISÃO INTEIRA(//)
#MÓDULO(%)

#Ordem de precedência dos Operadores:
#Parêntes ()
#Exponenciação (**)
#* / // %
# + e -

operadores = 'Operadores Aritméticos em Python'
print(operadores)

n1 = int(input('Digite um valor: '))
print('Pimeiro valor ', n1)
n2 = int(input('Digite outro valor: '))
print('Segundo valor ', n2)
soma = n1 + n2
subr = n1 - n2
mult = n1 * n2
div = n1 / n2
divint = n1 // n2
rest = n1 % n2
exponente = n1 ** n2
print('Resultado: ' .format(soma))
print('Resultado: ' .format(subr))
print('Resuktados '.format(exponente))
print('Resultados' .format(mult,div, divint, rest,))