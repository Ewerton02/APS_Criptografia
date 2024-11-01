import os

# Função para a contagem de votos


def resultado(tiao, ze, branco, nulo, total):
    candidatos = ["Tião do gás", "Zé da feira", "Branco", "Nulo", "Total"]
    contagem = {candidatos[0]: tiao, candidatos[1]: ze, candidatos[2]                : branco, candidatos[3]: nulo, candidatos[4]: total}
    return contagem

# Função para confirmar voto assim como o BOTÃO VERDE na urna


def confirmacao():
    confirma = input("Digite \"c\" para confirmar o voto: ")
    if confirma == "c":
        print("-=-" * 8)
        print("FIM")
        print("-=-" * 8)
    else:
        print("-=-" * 8)
        print("Voto não confirmado")
        print("-=-" * 8)
    return confirma

# Função que simula UM voto


def voto():
    # Função do voto continuará enquanto a variável for True:
    voto_aberto = True
    voto_registrado = ""
    while voto_aberto:  # Mostra as opções de candidatos
        print("\n" + "-=-" * 8)
        print("Opções de Voto:")
        print("-=-" * 8)
        print("1 - Tião do Gás")
        print("2 - Zé da Feira")
        print("3 - Branco")
        print("-=-" * 8)
        voto_registrado = input("Digite sua opção de voto: ").strip()
        print("-=-" * 8)

        # Cria as condições para cada voto e chama a função 'confirmacao()'
        if voto_registrado == '1':
            print("Você votou no Tião do Gás")
            if confirmacao() == "c":
                voto_aberto = False
            else:
                print("Retornando à seleção de candidatos")
        elif voto_registrado == '2':
            print("Você votou no Zé da Feira")
            if confirmacao() == "c":
                voto_aberto = False
            else:
                print("Retornando à seleção de candidatos")
        elif voto_registrado == '3':
            print("VOTO BRANCO")
            if confirmacao() == "c":
                voto_aberto = False
            else:
                print("Retornando à seleção de candidatos")
        else:
            print("VOTO NULO")
            if confirmacao() == "c":
                voto_aberto = False
            else:
                print("Retornando à seleção de candidatos")

    return voto_registrado

# Função para criptografar os votos usando XOR


def criptografar_votos(resultados, chave):
    votos_criptografados = ""
    # Converte os resultados dos votos em uma string
    dados_votos = f"Tião do Gás: {resultados['Tião do gás']}, Zé da Feira: {
        resultados['Zé da feira']}, Branco: {resultados['Branco']}, Nulo: {resultados['Nulo']}, Total: {resultados['Total']}"

    # Aplica o XOR em cada caractere
    for char in dados_votos:
        votos_criptografados += chr(ord(char) ^ chave)
    return votos_criptografados

# Função para gerar um hash usando o sistema de randomização do os


def gerar_os_hash(dados):
    hash_valor = 0
    for char in dados:
        # Usa o PID para adicionar randomização
        hash_valor = (hash_valor + ord(char) + os.getpid()) % 256
        hash_valor = (hash_valor << 1) | (
            hash_valor >> 7)  # Faz uma rotação de bits
    return hex(hash_valor)
    # Retorna o valor como uma string hexadecimal

# Função para salvar os dados criptografados e o hash em um arquivo


def salvar_arquivo(votos_criptografados, hash_valor):
    try:
        with open("votos_criptografados.txt", "w", encoding="utf-8") as arquivo:
            # Salvando os votos criptografados
            arquivo.write(votos_criptografados + "\n")
            # Salvando o hash gerado
            arquivo.write(f"Hash: {hash_valor}\n")
        print("Dados criptografados e hash salvos no arquivo 'votos_criptografados.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função principal


def funcao_principal():
    seccao_aberta = True  # A secção continuará enquanto a variável for True

    # A urna começa com 0 votos para todos os candidatos
    votos_tiao = 0
    votos_ze = 0
    votos_branco = 0
    votos_nulo = 0

    # Variável que vai conter o resultado das eleições (pré-criptografia)
    results = ""

    # Iniciando a votação:
    print("-=-" * 8)
    print("Iniciando Votação")

    while seccao_aberta:  # Validação do mesário se terá um novo votante ou secção encerrada
        print("-=-" * 8)
        print("1 - Novo Votante")
        print("2 - Encerrar Secção")
        print("-=-" * 8)
        novo_voto = input("\n")

        if novo_voto == "1":  # Se houver um novo votante
            voto_individual = voto()
            if voto_individual == '1':  # Registra voto para Tião
                votos_tiao += 1
            if voto_individual == '2':  # Registra voto para Zé
                votos_ze += 1
            if voto_individual == '3':  # Registra voto branco
                votos_branco += 1
            if voto_individual != '1' and voto_individual != '2' and voto_individual != '3':
                votos_nulo += 1
            votos_totais = votos_tiao+votos_ze+votos_branco+votos_nulo

        elif novo_voto == "2":  # Encerrar secção
            print("Secção Encerrada")

            # Variável para armazenar os resultados
            results = resultado(votos_tiao, votos_ze,
                                votos_branco, votos_nulo, votos_totais)

            # Criptografando os resultados
            chave_criptografia = 12345
            votos_criptografados = criptografar_votos(
                results, chave_criptografia)
            print("Votos criptografados:", votos_criptografados)

            # Gerando o hash dos votos criptografados
            hash_valor = gerar_os_hash(votos_criptografados)
            print("Hash gerado:", hash_valor)

            # Salvando os dados criptografados e o hash no arquivo
            salvar_arquivo(votos_criptografados, hash_valor)
            print(
                "Dados criptografados e hash salvos no arquivo 'votos_criptografados.txt'.")

            seccao_aberta = False  # Fim da secção


# Chamada da função principal
funcao_principal()
