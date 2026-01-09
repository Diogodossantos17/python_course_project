
#Condições me Pytho, parte 1

nome =str(input('digite seu nome '))
print('Nome do estudante: {}'.format(nome))

nota1 = float(input('digite sua primeira nota '))

print('Primeira nota {:.1f}'.format(nota1))

nota2 = float(input('digite sua segunda nota '))

print('Segunda nota {:.1f}'.format(nota2))

media = (nota1 + nota2) / 2

print('média {:.1f}'.format(media))

if media >=10:

    print('Aluno dispensa a cadeira!')

else:

    print('Exame!')


