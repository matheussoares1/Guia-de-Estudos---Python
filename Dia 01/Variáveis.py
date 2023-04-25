#Resolção de questões de logica de programação, retomando do basico ao avançado, utilizando a tecnologia Python.
#Variaveis e Estruturas de Condições

#Questão 01
#Escreva um pequeno algoritmo com uma variável de nome "cachorro" que tenha o valor em string de "Meu cachorro se chama Bilu", e imprima essa frase no console/terminal

cachorro = "O nome do meu cachorro é Cilibrina"
print(cachorro)

#Questão 02
#Escreva um pequeno algoritmo que declare o nome de uma pessoa, a idade que ela possue e quantos irmãos ela tem. Ao final da criação, faça com que as informações sejam impressas no terminal.

nome = "Matheus"
idade = 72
irmaos = 3
print(nome, idade, irmaos)

#Questão 03
# Crie um algoritmo que solicite o nome do usuário e imprima na tela uma mensagem de boas-vindas com o nome informado.

nome_user = input("Escreva o seu nome")
print(nome_user)

#Questões 04
# Crie um algoritmo que calcule a área de um retângulo a partir da entrada da largura e altura, e imprima o resultado na tela.

base = float(input("Escreva o valor da base "))
altura = float(input("Escreva o valor da altura "))
area = (base * altura)
print("A área do retangulo é igual a ", area)

#Questão 05
# Crie um algoritmo que solicite a idade do usuário e imprima na tela uma mensagem informando se ele é maior de idade ou não.
idade = int(input("Escreva a idade do atual usuario "))
if idade < 18 :
    print("O usuario é menor de idade")
else:
    print("O usuario é maior de idade")

#Questão 06
#Crie um algoritmo que solicite dois números ao usuário, some-os e imprima o resultado na tela.
num1 = float(input("Escreva um numero "))
num2 = float(input("Escreva o segundo numero "))
calc = num1 + num2
print(calc)


#Questão 07
base = float(input("Escreva o valor da base "))
altura = float(input("Escreva o valor da altura "))
area = (base * altura) / 2
print("A área do triangulo é igual a ", area)

#Questão 08
#Crie um algoritmo que solicite o nome, idade e altura do usuário, e imprima essas informações na tela.
nome1 = input("Digite o nome ")
idade1 = input("Digite a idade ")
altura1 = input("Digite a altura")
print("O nome da pessoa é ", nome1, ", sua idade é ", idade1, ", sua altura é de ", altura1)

#Questão 09
#Crie um algoritmo que solicite um número inteiro e verifique se ele é par ou ímpar, imprimindo na tela uma mensagem correspondente.

numero = int(input("Digite um numero para saber se ele é impar ou par "))
if numero % 2 == 0:
    print("O numero ", numero, " é Par")
elif numero % 2 == 0 :
    print("O numero ", numero, " é impar")

#Questão 10
#Crie um algoritmo que solicite o nome e a idade de duas pessoas, calcule a diferença de idade entre elas e imprima na tela.

nome2 = input("Qual é o nome da primeira pessoa? ")
idade2 = int(input("Qual é a idade da primeira pessoa? "))
nome3 = input("Qual é o nome da segunda pessoa? ")
idade3 = int(input("Qual é a idade da segunda pessoa? "))
diferenca = abs(idade2 - idade3)
print("A diferença de idade entre", nome2, "e", nome3, "é", diferenca, "anos.")

#Questão 11
#Crie um algoritmo que solicite o valor de uma compra e um desconto em porcentagem, calcule o valor final com o desconto e imprima na tela.






#Questão 12
#Crie um algoritmo que solicite três números ao usuário e imprima na tela o maior e o menor valor informados.



