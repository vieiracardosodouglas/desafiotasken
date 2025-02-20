# Função para contar o número de vogais em uma linha
def contar_vogais(linha):
    vogais = "aeiouAEIOU"
    return sum(1 for letra in linha if letra in vogais)

# Função para contar o número de consoantes em uma linha
def contar_consoantes(linha):
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    return sum(1 for letra in linha if letra in consoantes)

# Função principal
def analisar_arquivo():
    # Solicita ao usuário o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo (com a extensão .txt): ")

    try:
        # Abre o arquivo em modo de leitura
        with open(nome_arquivo, 'r') as arquivo:
            linhas = arquivo.readlines()

        # Inicializa variáveis para armazenar os índices das linhas com mais vogais e consoantes
        linha_com_mais_vogais = -1
        linha_com_mais_consoantes = -1
        max_vogais = 0
        max_consoantes = 0

        # Processa cada linha do arquivo
        for i, linha in enumerate(linhas):
            linha = linha.strip()  # Remove espaços em branco no começo e no final da linha
            num_vogais = contar_vogais(linha)
            num_consoantes = contar_consoantes(linha)

            # Verifica se essa linha tem mais vogais
            if num_vogais > max_vogais:
                max_vogais = num_vogais
                linha_com_mais_vogais = i

            # Verifica se essa linha tem mais consoantes
            if num_consoantes > max_consoantes:
                max_consoantes = num_consoantes
                linha_com_mais_consoantes = i

        # Exibe os resultados
        print(f"A linha com mais vogais é a linha {linha_com_mais_vogais + 1}:")
        print(linhas[linha_com_mais_vogais].strip())
        print(f"\nA linha com mais consoantes é a linha {linha_com_mais_consoantes + 1}:")
        print(linhas[linha_com_mais_consoantes].strip())

    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Chama a função principal para rodar o programa
analisar_arquivo()