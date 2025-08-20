def calculadora():
    while True:
        print("Calculadora simples!")
        print()
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("s - Sair")

        operacao = (input("Selecione uma opção ou 's' para sair "))

        if operacao == "s" or operacao == "S":
            print("Obrigado por utilizar a Calculadora simples!")
            break

        if operacao not in ["1", "2", "3", "4"]:
            print("Opção inválida! Tente novamente.")
            continue

        numero_1 = float(input("Primeiro número:"))
        numero_2 = float(input("Segundo número:"))

        if operacao == "1":
            resultado = numero_1 + numero_2
            print("o resultado da operação soma é: ", resultado)
        elif operacao == "2":
            resultado = numero_1 - numero_2
            print("o resultado da operação subtração é: ", resultado)
        elif operacao == "3":
            resultado = numero_1 * numero_2
            print("o resultado da operação multiplicação é: ", resultado)
        else:
            if numero_2 == 0:
                print("Divisão por zero não é possivel, tente novamente.")
                continue
            else:
                resultado = numero_1 / numero_2
                print("o resultado da operação divisão é: ", resultado)

calculadora()