nome = input("Escreva seu nome: ")
while True:  
    try:
        idade = int(input("Escreva sua idade: "))

        if idade >= 18:
            print("Olá ", nome, ".Você é maior de idade.")
            break
    
        else:
            print("Olá ", nome, ".Você não é maior de idade.")
            break

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números inteiros.")

import math
valor_pi = math.pi
print(valor_pi)

def calcular_media():
    media = (nota_um + nota_dois) / 2

nota_um = 7
nota_dois = 9
print("Sua Média é: ", calcular_media)