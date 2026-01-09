
#Condições Aninhadas em Python.

nome = str(input('Insira aqui o seu nome por favor'))
print('Nome do estudante {} ' .format(nome.upper()))

Idade =int(input('Insira a sua idade'))
print('Idade do cidadão : {} ' .format(Idade))

partido = str(input('Qual partido votas? '))
print('Partido:  {} '.format(partido))

AnoDeNascimento = int(input('Qual ano de nascimento? '))

print('Ano de Nascimento: {} ' .format(AnoDeNascimento))

mes = str(input('Mês de nascimento?'))

print('Mês de nascimento {}! ' .format(mes))




if Idade >= 18:
    print('Está na idade certa para exercer o seu direito de voto, e pode votar')

elif AnoDeNascimento == 2008 or mes == 'Julho'  or  Idade == 17:

    print('Fará 18 anos um mês antes ou  depois das eleiões, pode votar!')

else:
    print('Lamentamos é menor de idade para votar. Aguarde, a sua vez vai chegar!')
