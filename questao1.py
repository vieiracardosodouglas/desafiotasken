def print_square_pattern(n):
    if n <= 0:
        print("Erro: O valor deve ser um inteiro positivo.")
        return
    
    for i in range(n, 0, -1):
        squares = [x**2 for x in range(i, 0, -1)]  # Calcula os quadrados
        squares_str = [str(num) for num in squares]  # Converte para string
        line = " ".join(squares_str)  # Junta os elementos com espaço
        print(line)  # Exibe a linha


