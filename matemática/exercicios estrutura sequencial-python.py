#1 - função alo mundo

print('alo mundo')

#2 - programa que peça um numero e então mostre a mensagem O número informado foi [numero]

#variáveis
numero = 0

#processamento
num1 = float(input('Digite o numero: '))

#saída
print('O número informado foi: ', num1)

#3 - faça um programa que peça dois numeros e imprima a soma.

#Variaveis
num1 = num2 = 0

#Processamento
num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
soma = num1 + num2

#Saida
print("A soma dos numeros é: ", soma)

#4 - programa que calcula a media
def media():

#processamento
    nota_1 = float(input('Digite a nota: '))
    nota_2 = float(input('Digite a nota: '))
    nota_3 = float(input('Digite a nota: '))
    nota_4 = float(input('Digite a nota: '))
    media = nota_1 + nota_2 + nota_3 + nota_4 / 4

#saída
    print('A media é: ', media)
    return media

media()

#5 - programa que pede a area de um circulo, para calcular a area

#variáveis
raio = area = 0

#processamento
raio= float(input('Digite o raio do circulo: '))
area = (raio*raio)*3,14

#saída
print('A area do circulo é de: ', raio)

#6 - programa que calcula area do quadrado e mostra o dobro dela

#variaveis
lado = area = dobro = 0

#processamento
lado = float(input('Digite o lado do quadrado em cm: '))
area = (lado*lado)
dobro = area*area

#saída
print('O dobro da area do quadrado é: ', dobro)

# 7 - programa que calcula quanto voce ganha por hora e o numero de horas trabalhadas no mês + total do salário

#variaveis
valor = float(input('Digite o valor por hora: '))
horas = float(input('Digite o numero de horas: '))

#processamento
salario = valor*horas

#saída
print('Total do salário: R$ ', salario)

#8 - programa que transforma a temperatura de faren em celsius

#variaveis
faren = float(input('Digite a temperatura em faren: '))

#processamento
celsius = (5* ((faren-32) / 9))

#saída
print('A temperatura em celsius é: ', celsius)

#9 - programa que passa de celsius para faren
celsius = float(input('Digite a temperatura em celsius: '))

#processamento
faren = (celsius*9/5) + 32

#saída:
print('A temperatura em faren é: ', faren)

#10 - programa que passa de celsius para faren
celsius = float(input('Digite a temperatura em celsius: '))

#processamento
faren = (celsius * 9 / 5) + 32

# saída:
print('A temperatura em faren é: ', faren)

#11 - Programa que pede 2 nummeros reais e um inteiro e mostra o dobro do primeiro com a metade do segundo e a soma do triplo com o terceiro e o terceiro elevado ao cubo
numero = float(input('Digite um numero real: '))
numero_2 = float(input('Digite outro numero real: '))
numero_int = float(input('Digite um numero inteiro: '))

#processamento
dobro = ((numero * 2) * (numero_2 / 2))
soma = ((numero * 3) + numero_int)
cubo = numero_int ** 3

#saída
print('O dobro do primeiro com a metade do segundo é: ', dobro)
print('A soma do triplo do primeiro com o terceiro é: ', soma)
print('O terceiro número elevado ao cubo é: ', cubo)

#12 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 5

#variáveis
altura = float(input('Digite sua altura: '))

#processamento
peso = (72.7 * altura) - 58

#saída
print("Peso ideal: %.1kg", peso)

#13 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

#variáveis
h = float(input('Digite sua altura: '))

#processamento
peso_homens = (72.7 * h) - 58
peso_mulheres = (62.1 * h) - 44.7

#saída
print('Peso ideal: %.1f kg', peso_homens)
print('Peso ideal: %.1f kg', peso_mulheres)

#variável
peso = float(input('Digite o peso: '))
excesso = multa = 0

#processamento
if peso >= 50:
    excesso = peso - 50
    multa = excesso * 4

#saída
print('Kilos pescados: ', peso)
print('excesso de kilo: ', excesso)
print('multa por excesso: ', multa)

#15 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato
#faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato ( 5%) : R$
# = Salário Liquido : R$

#varíaveis
valor = float(input('Digite o valor por horas:R$ '))
horas = float(input('Digite o numero de horas trabalhadas: '))

#processamento
salario = valor * horas
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario_liquido = salario - ir - inss - sindicato

#saída
print('O valor do salario é:R$ ', salario)
print('Pago ir:R$', ir)
print('Pago inss:R$', inss)
print('Pago sindicato:R$', sindicato)
print('Líquido:R$', salario_liquido)


#18 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

#varíaveis
arquivo = float(input('Tamanho do arquivo em mb: '))
link = float(input('Velocidade do link em mpbs: '))

#processamento
taxa = link / 8
tempo = arquivo / taxa
minutos = tempo / 60

#Saída
print('Tempo aproximado do download: ', minutos)

