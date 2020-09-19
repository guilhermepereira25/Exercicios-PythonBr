# programa que pede dois números e dá o maior deles
# varíaveis
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))

# processamento
if num1 == num2:
    print('numeros iguais.')
elif num2 > num1:
    print('O maior é: ', num2)
else:
    print('O maior numero é: ', num1)

num1 = float(input('Digite um numero: '))

# processamento
if num1 >= 0:
    print('Numero positivo. ')
else:
    print('Numero negativo. ')

# variável
letra = input('Digite a opção: ')

# processamento
letra = letra.lower()
if letra == 'f':
    print('F - Feminino')
elif letra == 'm':
    print('M - Masculino')
else:
    print('Sexo inválido. ')

palavra = (input('Digite a opção: '))

# processamento
palavra = palavra.lower()
if letra not in 'aeiou':
    print('Letra consoante.')
else:
    print('Letra vogal. ')

# variável
nota1 = float(input('Digite a nota: '))
nota2 = float(input('Digite a nota: '))

# processamento
media = nota1 + nota2 / 2
if media >= 7:
    print('Aprovado')
elif media < 7:
    print('Reprovado.')
else:
    media = 10
    print('Aprovado com Distinção. ')

# programa que lê os numeros e mostra o maior deles
num1 = float(input('Digite um numero: '))
num2 = float(input('Digite um numero: '))
num3 = float(input('Digite um numero: '))

# processamento
if num1 > num2 and num1 > num3:
    print('O maior é o primeiro.')
elif num2 > num3:
    print('O maior é o segundo. ')
else:
    print('O maior é o terceiro. ')

# programa que lê os numeros e mostra o maior e menor deles
menor = maior = 0
num1 = float(input('Digite  o primeiro numero: '))
num2 = float(input('Digite o segundo numero: '))
num3 = float(input('Digite o terceiro numero: '))

# processamento
if num1 > num2:
    if num1 > num3:
        maior = num1
        if num2 < num3:
            menor = num2
        else:
            menor = num3
    elif num3 > num2:
        maior = num3
        menor = num2
else:
    if num2 > num3:
        maior = num2
        if num1 < num3:
            menor = num1
        else:
            menor = num3
    else:
        maior = num3
        menor = num1

# saída
print('O maior número é: ', maior)
print('O menor número é: ', menor)

# programa que lê o produto mais barato

# variáveis
p1 = float(input('Digite o preço do primeiro produto:R$ '))
p2 = float(input('Digite o preço do segundo produto:R$ '))
p3 = float(input('Digite o preço do terceiro produto:R$ '))

# processamento
if p1 < p2 and p1 < p2:
    print('O mais barato é o primeiro produto.')
elif p2 < p3:
    print('O mais barato é o segundo produto.')
else:
    print('O mais barato é o terceiro produto.')

# programa que lê os numeros em ordem decrescente

# variaveis =
primeiro = float(input('Digite o primeiro número: '))
segundo = float(input('Digite o segundo número: '))
terceiro = float(input('Digite o terceiro número: '))

# processamento
if terceiro > primeiro:
    terceiro, primeiro = primeiro, terceiro
if terceiro > segundo:
    terceiro, segundo = segundo, terceiro
if segundo > primeiro:
    segundo, primeiro = primeiro, segundo

# saída
print('A ordem descrescente é:', primeiro, segundo, terceiro)

# programa que pergunta o turno que voce estuda e reconhece com "Bom dia", etc.

# variável
turno = input("Digite em que turno você estuda: \nM para matutino\nV para vespertino\nN para noturno: ")

# processamento
turno = turno.upper()

if turno == 'M':
    print('Bom dia')
elif turno == 'V':
    print('Boa tarde')
elif turno == 'N':
    print('Boa noite')
else:
    print('Valor Inválido')

# varíavel
salario = input('Digite o valor do salário: ')

# processamento
if salario <= 280:
    percentual_aumento = 20
elif salario < 700:
    percentual_aumento = 15
elif salario < 1500:
    percentual_aumento = 10
else:
    percentual_aumento = 5

aumento = salario * (percentual_aumento / 100)
novo_salario = salario + aumento

# saída
print(f"Salário antes do reajuste: R${salario:.2f}")
print(f"Percentual do aumento aplicado: R${salario:.2f}")
print(f"Percentual do aumento aplicado: {percentual_aumento}%")
print(f"Valor do aumento: R${aumento:.2f}")
print(f"Novo salario: R${novo_salario:.2f}")