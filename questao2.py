def compactar_string(s):
    if not s:  # Se a string estiver vazia, retorna vazio
        return ""

    resultado = []  # Lista para armazenar o resultado
    contador = 1  # Contador começa em 1, já que temos pelo menos um caractere

    # Percorre a string a partir do segundo caractere
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:  # Se o caractere for igual ao anterior, aumenta o contador
            contador += 1
        else:  # Se for diferente, adiciona ao resultado e reinicia o contador
            if contador > 1:
                resultado.append(s[i - 1] + str(contador))  # Adiciona caractere + número
            else:
                resultado.append(s[i - 1])  # Apenas o caractere

            contador = 1  # Reinicia a contagem para o novo caractere

    # Adiciona o último caractere que foi contado
    if contador > 1:
        resultado.append(s[-1] + str(contador))
    else:
        resultado.append(s[-1])

    return "".join(resultado)  # Junta a lista em uma única string


