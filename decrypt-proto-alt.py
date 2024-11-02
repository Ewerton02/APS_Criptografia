# Código de validação e descriptografia do resultado das eleições

# Única falha é que eu não consegui gerar o hash igual ao do arquivo original,
#   é preciso fazer um troubleshooting da função hash_recriado()

def descriptografar(arquivo_votos, chave=12345):
    dados_descriptografados = ""

    # Lê a primeira linha e coloca seu conteúdo na variável 'dados_votos'
    with open(arquivo_votos, 'r', encoding='utf-8') as file:
        dados_votos = file.readline().strip()

    # Descriptografa cada caractere da variável 'dados_votos'
    for char in dados_votos:
        dados_descriptografados += chr(ord(char) ^ chave)
    return dados_descriptografados


def hash_original(arquivo_hash):  # Função para pegar o Hash do arquivo 'votos_criptografados.txt'

    with open(arquivo_hash, 'r', encoding='utf-8') as file:
        # Lê todas as linhas do arquivo
        hash_linhas = file.readlines()

        # Acessa a segunda linha e remove o prefixo 'Hash: ' e espaços extras
    hash_valor = hash_linhas[1].replace("Hash: ", "").strip()
    return hash_valor


def pid_original(arquivo_pid):  # Função para pegar o PID do arquivo 'validacao.txt'

    # Lê todas as linhas do arquivo
    with open(arquivo_pid, 'r', encoding='utf-8') as file:
        pid_linhas = file.readlines()

        # Acessa a primeira linha e remove o prefixo 'PID: ' e espaços extras
    pid_valor = pid_linhas[0].replace("PID: ", "").strip()
    pid_valor = int(pid_valor)
    return pid_valor


def hash_recriado(arquivo_votos, arquivo_validacao):
    # Gera variáveis com os dados da descriptografia e outra com o PID
    dados = descriptografar(arquivo_votos)
    pid = pid_original(arquivo_validacao)
    hash_valor = 0

    for char in dados:
        # Usa o PID dado para recriar o hash do arquivo 'votos_criptografados'
        hash_valor = (hash_valor + ord(char) + pid) % 256
        hash_valor = (hash_valor << 1) | (
                hash_valor >> 7)
    return hex(hash_valor)


def comparar_hashes():  # Função para comparar o hash original com o hash recriado

    if hash_original('votos_criptografados.txt') == hash_recriado('votos_criptografados.txt', 'validacao.txt'):
        hashes_iguais = True
    else:
        hashes_iguais = False

    return hashes_iguais


def fun_debug():  # Função para mostrar os valores importantes do código
    print("Votos descriptografados:")
    print(descriptografar('votos_criptografados.txt'))
    print("PID Original:")
    print(pid_original('validacao.txt'))
    print("Hash Original:")
    print(hash_original('votos_criptografados.txt'))
    print("Hash Recriado:")
    print(hash_recriado('votos_criptografados.txt', 'validacao.txt'))
    print("Comparação do hash original com o hash criado (True se forem iguais, False se forem diferentes):")
    print(comparar_hashes())


fun_debug()
