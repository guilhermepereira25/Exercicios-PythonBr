#varíavel
salario = float(input('Digite o valor do salário: '))

#processamento
if salario <=280:
    percentual_aumento = 20
elif salario < 700:
    percentual_aumento = 15
elif salario < 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

#saída
print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual do aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salario: R${novo_salario:.2f}")

#salario líquido = salario bruto - descontos
#varíavel
valor = float(input('Digite o valor por hora: '))
horas = float(input('Digite o numero de horas trabalhadas: '))
salario_bruto = valor * horas

#processamento
if salario_bruto < 900:
    percentual_desconto = 0
elif salario_bruto < 1500:
    percentual_desconto = -5
elif salario_bruto < 2500:
    percentual_desconto = -10
else:
    percentual_desconto = - 20

desconto_ir = salario_bruto * (percentual_desconto / 100)
desconto_inss = 0.3 * percentual_desconto
desconto_sindicato = salario_bruto * 0.3
fgts = salario_bruto * 0.11
Total_desconto = desconto_sindicato + desconto_inss + desconto_ir
salario_liquido = salario_bruto - Total_desconto

#saída
print(f"(+) Salário Bruto ({valor:.2f} * {horas}): R${salario_bruto:.2f}")
print(f"(-) IR ({percentual_desconto}%): R${desconto_ir:.2f}")
print(f"(-) Sindicato (3%): R${desconto_sindicato:.2f}")
print(f"(-) INSS (10%): R${desconto_inss:.2f}")
print(f"FGTS (11%): R${fgts:.2f}")
print(f"Total de Descontos: R${Total_desconto:.2f}")
print(f'Salário Líquido:R$ {salario_liquido}')

#programa que le os dias da semana

#variável
numero = float(input('Digite um numero: '))

#processamento
if numero == 1:
    print(' 1- Domingo')
elif numero == 2:
    print(' 2 - Segunda-Feira')
elif numero == 3:
    print('3 - Terça-Feira')
elif numero == 4:
    print('4 - Quarta-Feira')
elif numero == 5:
    print('5 - Quinta-Feira')
elif numero == 6:
    print('6 - Sexta-Feira')
elif numero == 7:
     print('7 - Sábado')
else:
    print('Valor inválido')

#varíavel
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2

#processamento
if media >= 9 and media <= 10:
    conceito = 'A'
elif media >= 7.5 and media < 9.0:
    conceito = 'B'
elif media >= 6.5 and media < 7.5:
    conceito = 'C'
elif media >= 4 and media < 6:
    conceito = 'D'
else:
    conceito = 'E'

if conceito == 'A' or conceito == 'B' or conceito == 'C':
    situação = 'Aprovado'
if conceito == 'D' or conceito == 'E':
    situação = 'Reprovado'

#saída
print(f"Nota1: {nota1}")
print(f"Nota2: {nota2}")
print(f"Media: {media}")
print(f"Conceito: {conceito}")
print(f"Situação: {situação}")

#programa que pede os lados de um triângulo

#varíavel
lado1 = float(input('Digite o lado: '))
lado2 = float(input('Digite o lado: '))
lado3 = float(input('Digite o lado: '))

#processamento
if lado1 == lado2 and lado2 == lado3:
    print("Triângulo Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Triângulo Isósceles")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Triângulo Escaleno")

#Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
# O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:
#Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os demais valores, sendo encerrado;
#Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
#Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
#Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

#varíavel
a = float(input('Digite o valor de a: '))

if a == 0:
    print('A equação não é do segundo grau.')
    exit()

b = int(input("Digite o segundo valor: "))
c = int(input("Digite o terceiro valor: "))
delta = (b**2) - (4 - 1 * c)

if delta < 0:
    print('Não possui raízes reais.')
    exit()
elif delta == 0:
    x = (b* - 1) / (2 - a)
    print('Possui apenas uma raiz real. ')
    exit()

x1 = ((b * -1) + (delta)) / (2*a)
x2 = ((b * -1) - (delta)) / (2*a)

print(f"Valor de x1 é: {x1}")
print(f"Valor de x2 é: {x2}")

#Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida
dia = int(input("Digite o dia - ex: 00: "))
mes = int(input("Digite o mes - ex: 00: "))
ano = int(input("Digite o ano - ex: 0000: "))

meses_com_30 = [2,4,6,9,11]

data_formatada = f"{dia}/{mes}/{ano}"

if dia > 31 or dia < 1:
    print(f"Data {data_formatada} inválida")
elif mes < 1 or mes > 12:
    print(f"Data {data_formatada} inválida")
elif ano < 0:
    print(f"Data {data_formatada} inválida")
elif mes == 2 and dia > 29:
    print(f"Data {data_formatada} inválida")
elif mes in meses_com_30 and dia > 30:
    print(f"Data {data_formatada} inválida")
else:
    print(f"Data {data_formatada} válida")

#Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais.
#O programa não deve se preocupar com a quantidade de notas existentes na máquina.
#Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
#Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1

valor_a_sacar = int(input("Digite o valor que deseja sacar: "))

notas_de_cem = valor_a_sacar // 100
resto = valor_a_sacar % 100

notas_de_cinquenta = resto //50
resto = resto % 50

notas_de_dez = resto // 10
resto = resto % 10

notas_de_cinco = resto // 5
moedas_de_um = resto % 5 #como o valor mínimo é de um, não preciso recalcular o valor restante. O próprio resto é o valor em si

if notas_de_cem > 0:
    print(f"{notas_de_cem} notas de 100 ")

if notas_de_cinquenta > 0:
    print(f"{notas_de_cinquenta} notas de 50 ")

if notas_de_dez > 0:
    print(f"{notas_de_dez} notas de 10")

if notas_de_cinco > 0:
    print(f"{notas_de_cinco} notas de 5")

if moedas_de_um > 0:
    print(f"{moedas_de_um} moedas de 1")

#Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
# Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e
#5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

suspeita = 0

if input("Telefonou para a vítima? [sim/nao]: ").lower() == "sim":
    suspeita += 1
if input("Esteve no local do crime? [sim/nao]: ").lower() == "sim":
    suspeita += 1
if input("Mora perto da vítima? [sim/nao]: ").lower() == "sim":
    suspeita += 1
if input("Devia para a vítima? [sim/nao]: ").lower() == "sim":
    suspeita += 1
if input("Já trabalhou com a vítima? [sim/nao]: ").lower() == "sim":
    suspeita += 1

if suspeita == 0:
    print("Inocente")
elif suspeita <= 2:
    print("Suspeita")
elif suspeita <=4:
    print("Cúmplice")
else:
    print("Assassino")


#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

numero = 11

#processamento
while numero > 10:
    numero = int(input('Digite um numero de 1 a 10: '))
    if numero > 10 or numero < 0:
        print('Numero invalido.')


#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

usuario_valido = False

#processamento
while usuario_valido == False:
    usuario = input('Digite um usuario: ')
    senha = input('Digite uma senha: ')

    if usuario == senha:
        print('Usuario nao pode ser igual a senha.')
    else:
         usuario_valido = True


#Faça um programa que leia e valide as seguintes informações:
#Nome: maior que 3 caracteres;
#Idade: entre 0 e 150;
#Salário: maior que zero;
#Sexo: 'f' ou 'm';
#Estado Civil: 's', 'c', 'v', 'd'

usuario_valido = False

#processamento
while usuario_valido == False:
    nome = input('Digite um nome: ')
    idade = int(input('Digite uma idade: '))
    salario = int(input('Digite um salario: '))
    sexo = input('Digite seu sexo: [f ou m]: ')
    estado_civil = input('Digite seu estado civil: [s, c, v, d]: ')


    if  (len(nome) > 3) and (idade >=0 and idade <= 150) and (salario > 0) and (sexo in ['f','m']) and (estado_civil in ['s','c','v','d']):
        usuario_valido = True
    else:
       print('Usuario inválido')



