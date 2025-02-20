def analisar_numeros():
    """
    Lê números positivos do teclado até que o número zero seja digitado e exibe um relatório.
    """

    numeros = []
    maior_numero = float('-inf')  # Inicializa com o menor valor possível
    menor_impar = float('inf')  # Inicializa com o maior valor possível
    ocorrencias = {}

    while True:
        try:
            numero = int(input("Digite um número positivo (ou 0 para sair): "))
            if numero < 0:
                print("Por favor, digite apenas números positivos.")
                continue  # Volta para o início do loop

            if numero == 0:
                break

            numeros.append(numero)

            # Atualiza o maior número
            maior_numero = max(maior_numero, numero)

            # Atualiza o menor número ímpar
            if numero % 2 != 0:
                menor_impar = min(menor_impar, numero)

            # Conta as ocorrências de cada número
            if numero in ocorrencias:
                ocorrencias[numero] += 1
            else:
                ocorrencias[numero] = 1

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    # Verifica se algum número foi digitado
    if not numeros:
        print("Nenhum número foi digitado.")
        return

    # Calcula a média dos números
    media = sum(numeros) / len(numeros)

    # Exibe o relatório
    print("\n--- Relatório ---")
    print(f"Quantidade de números lidos: {len(numeros)}")
    print(f"Maior número lido: {maior_numero}")
    print(f"Média dos números lidos: {media:.2f}")

    # Verifica se algum número ímpar foi digitado
    if menor_impar != float('inf'):
        print(f"Menor número ímpar lido: {menor_impar}")
    else:
        print("Nenhum número ímpar foi digitado.")

    print("\nOcorrências de cada número:")
    for numero, quantidade in ocorrencias.items():
        print(f"O número {numero} ocorreu {quantidade} vez(es).")


# Chama a função para executar o programa
analisar_numeros()