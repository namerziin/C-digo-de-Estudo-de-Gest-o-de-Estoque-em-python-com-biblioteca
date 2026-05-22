"""while True:
    try:
        nota_um = float(input("Digite a nota da sua av1: "))
        nota_dois = float(input("Digite a nota da sua av2: "))

        media = (nota_um + nota_dois) / 2

        if media >= 6:
            print("Sua média é ", media, "e você passou")
            break

        else:
            print("Sua média é ", media, "e você não passou passou")
            break

    except ValueError:
        print("Digite apenas números usando o . como separação para decimal")"""

"""numero = 10
for numero in range(1,21):
    print(numero)"""

"""while True:
    try:
        km = float(input("Digite a distância que deseja converter: "))
        metros = km * 1000
        print("Sua distância em metros é:",metros,"metros.")
        break
    except ValueError:
        print("Digite apenas a distância em quilometros.")"""

"""while True: #Aqui a gente cria um loop, para que o programa consiga completar o seu objetivo.
    try: #Aqui a gente garante que o programa não quebre caso o usuário digite um valor inválido
        temperatura_graus_celsius = float(input("Digite a temperatura em Graus Celsius:")) #Aqui a gente recebe o valor já convertendo para o tipo float
        temperatura_graus_fahrenheit = (temperatura_graus_celsius * 9 / 5) + 32
        print(f"A temperatura convertida é {temperatura_graus_fahrenheit} graus Fahrenheit")
        break #Aqui a gente encerra a execução do programa caso ele complete sua função
    except ValueError: #Aqui a gente imprime para o usuário que ele digitou um valor inválido e exemplifica como deve ser digitado
        print("Digite apenas valores inteiros ou decimais usando o . (exemplo: 32.5).")"""

import math #Aqui Importamos a biblioteca.
while True: #Aqui criamos um loop para garantir que nosso programa seja executado da forma correta.
    try: #Aqui a gente garante que o valor digitado será válido
        numero_desejado = int(input("Digite o número de 1 a 10 que deseja descobrir o fatorial: ")) #Aqui a gente já recebe o valor convertendo para o tipo inteiro
        if numero_desejado <= 10: #Aqui a gente condiciona o usuário a escolher entre 1 e 10
            fatorial = math.factorial(numero_desejado) #Aqui usamos a operação da biblioteca
            print(f"O fatorial de {numero_desejado} é: {fatorial}") #Aqui imprimimos o resultado
            break #Aqui encerramos o programa caso ele seja executado da forma correta
        else: #Aqui o usuário recebe erro por digitar um valor inválido
            print("Valor inválido. Digite um número inteiro de 1 a 10.")
    except ValueError: #Aqui caso o valor digitado seja inválido, o programa não quebra e informa ao usuário.
        print("Valor inválido. Digite um número inteiro de 1 a 10.")
