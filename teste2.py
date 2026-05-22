#Calculadora básica de números inteiros

while True:
    try:
        numero1 = int(input("Digite o primeiro número:\n"))
        operacao = input("Digite a operação desejada: \n")
        numero2 = int(input("Digite o segundo número:\n"))
        
        if operacao == "+":
            resultado = numero1 + numero2

        elif operacao == "*":
            resultado = numero1 * numero2

        elif operacao == "-":
            resultado = numero1 - numero2

        elif operacao == "/":
            resultado = numero1 / numero2

        else:
            print("Digite apenas as operações válidas.")
            continue
        
        print("\nResultado:\n")
        print(numero1)
        print(operacao)
        print(numero2)
        print("-----------")
        print(resultado)
        break

    except ValueError:
        print("Digite apenas números inteiros")
    except ZeroDivisionError:
        print("Não é possivel dividir por 0")