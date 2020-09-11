# programa que passa de celsius para faren
celsius = float(input('Digite a temperatura em celsius: '))

# processamento
faren = (celsius * 9 / 5) + 32

# saída:
print('A temperatura em faren é: ', faren)

# Programa que pede 2 nummeros reais e um inteiro e mostra o dobro do primeiro com a metade do segundo e a soma do triplo com o terceiro e o terceiro elevado ao cubo
numero = float(input('Digite um numero real: '))
numero_2 = float(input('Digite outro numero real: '))
numero_int = float(input('Digite um numero inteiro: '))

# processamento
dobro = ((numero * 2) * (numero_2 / 2))
soma = ((numero * 3) + numero_int)
cubo = numero_int ** 3

# saída
print('O dobro do primeiro com a metade do segundo é: ', dobro)
print('A soma do triplo do primeiro com o terceiro é: ', soma)
print('O terceiro número elevado ao cubo é: ', cubo)

# variáveis
altura = float(input('Digite sua altura: '))

# processamento
peso = (72.7 * altura) - 58

# saída
print("Peso ideal: %.1kg", peso)

# variáveis
h = float(input('Digite sua altura: '))

# processamento
peso_homens = (72.7 * h) - 58
peso_mulheres = (62.1 * h) - 44.7

# saída
print('Peso ideal: %.1f kg', peso_homens)
print('Peso ideal: %.1f kg', peso_mulheres)

# variável
peso = float(input('Digite o peso: '))
excesso = multa = 0

# processamento
if peso >= 50:
    excesso = peso - 50
    multa = excesso * 4

# saída
print('Kilos pescados: ', peso)
print('excesso de kilo: ', excesso)
print('multa por excesso: ', multa)

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.
# calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

# varíaveis
valor = float(input('Digite o valor por horas:R$ '))
horas = float(input('Digite o numero de horas trabalhadas: '))

# processamento
salario = valor * horas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario - ir - inss - sindicato

# saída
print('O valor do salario é:R$ ', salario)
print('Pago ir:R$', ir)
print('Pago inss:R$', inss)
print('Pago sindicato:R$', sindicato)
print('Líquido:R$', salario_liquido)

#varíaveis
arquivo = float(input('Tamanho do arquivo em mb: '))
link = float(input('Velocidade do link em mpbs: '))

#processamento
taxa = link / 8
tempo = arquivo / taxa
minutos = tempo / 60

#Saída
print('Tempo aproximado do download: ', minutos)


