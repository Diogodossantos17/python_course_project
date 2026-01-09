
#Módulos/Pacotes, em Python são Bibliotecas para dar mais funcionalidades ao nosso programa. As Bibliotecas, são importadas da seguinte forma:
#import Bibliotec
#from Biblioteca import:

import math



num =int(input('Digite um número por favor.'))

raiz = math.sqrt(num)

print('A raíz quadrada do número {} é {}  ' .format(num, math.ceil(raiz)))

