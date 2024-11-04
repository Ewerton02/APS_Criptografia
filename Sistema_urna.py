import os

# Função para a contagem de votos
def resultado(tiao, ze, branco, nulo, total):
    candidatos = ["Tião do gás", "Zé da feira", "Branco", "Nulo", "Total"]
    contagem = {candidatos[0]: tiao,
                candidatos[1]: ze,
                candidatos[2]: branco,
                candidatos[3]: nulo,
                candidatos[4]: total}
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
    voto_aberto = True
    voto_registrado = ""
    while voto_aberto:
        print("\n" + "-=-" * 8)
        print("Opções de Voto:")
        print("-=-" * 8)
        print("1 - Tião do Gás")
        print("2 - Zé da Feira")
        print("3 - Branco")
        print("-=-" * 8)
        voto_registrado = input("Digite sua opção de voto: ").strip()
        print("-=-" * 8)

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
    dados_votos = (
        f"Tião do Gás: {resultados['Tião do gás']}, "
        f"Zé da Feira: {resultados['Zé da feira']}, "
        f"Branco: {resultados['Branco']}, "
        f"Nulo: {resultados['Nulo']}, "
        f"Total: {resultados['Total']}"
    )

    for char in dados_votos:
        votos_criptografados += chr(ord(char) ^ chave)
    return votos_criptografados

# Função para gerar um hash usando o PID do processo
def gerar_os_hash(dados, pid):
    hash_valor = 0
    for char in dados:
        hash_valor = (hash_valor + ord(char) + pid) % 256
        hash_valor = (hash_valor << 1) | (hash_valor >> 7)
    return hex(hash_valor)

# Função para salvar os dados criptografados, hash e PID em um arquivo
def salvar_arquivo(votos_criptografados, hash_valor, pid):
    try:
        with open("votos_criptografados.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write(votos_criptografados + "\n")
            arquivo.write(f"Hash: {hash_valor}\n")
            arquivo.write(f"PID: {pid}\n")
        print("Dados criptografados e hash salvos no arquivo 'votos_criptografados.txt'.")
    except Exception as e:
        print(f"Erro ao salvar o arquivo: {e}")

# Função principal de votação e criptografia
def funcao_principal():
    seccao_aberta = True
    votos_tiao = votos_ze = votos_branco = votos_nulo = 0

    print("-=-" * 8)
    print("Iniciando Votação")

    while seccao_aberta:
        print("-=-" * 8)
        print("1 - Novo Votante")
        print("2 - Encerrar Secção")
        print("-=-" * 8)
        novo_voto = input("\n")

        if novo_voto == "1":
            voto_individual = voto()
            if voto_individual == '1':
                votos_tiao += 1
            elif voto_individual == '2':
                votos_ze += 1
            elif voto_individual == '3':
                votos_branco += 1
            else:
                votos_nulo += 1
            votos_totais = votos_tiao + votos_ze + votos_branco + votos_nulo

        elif novo_voto == "2":
            print("Secção Encerrada")

            results = resultado(votos_tiao, votos_ze, votos_branco, votos_nulo, votos_totais)
            chave_criptografia = 12345
            votos_criptografados = criptografar_votos(results, chave_criptografia)
            pid = os.getpid()
            hash_valor = gerar_os_hash(votos_criptografados, pid)

            salvar_arquivo(votos_criptografados, hash_valor, pid)
            seccao_aberta = False

# Função para descriptografar e validar os votos
def descriptografar_e_validar(arquivo_votos, chave=12345):
    try:
        with open(arquivo_votos, 'r', encoding='utf-8') as file:
            dados_votos = file.readline().strip()
            hash_arquivo = file.readline().replace("Hash: ", "").strip()
            pid_arquivo = int(file.readline().replace("PID: ", "").strip())

        dados_descriptografados = ""
        for char in dados_votos:
            dados_descriptografados += chr(ord(char) ^ chave)

        hash_calculado = gerar_os_hash(dados_votos, pid_arquivo)
        if hash_calculado == hash_arquivo:
            print("Arquivo verificado com sucesso. Hash corresponde.")
            print("Votos descriptografados:", dados_descriptografados)
        else:
            print("Erro: Hash não corresponde. Arquivo pode estar corrompido.")
    except FileNotFoundError:
        print(f"Erro: O arquivo '{arquivo_votos}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Menu de opções
def main():
    print("Escolha uma opção:")
    print("1 - Iniciar votação")
    print("2 - Descriptografar e validar resultados")
    opcao = input("Opção: ")

    if opcao == "1":
        funcao_principal()
    elif opcao == "2":
        nome_arquivo = input("Digite o nome do arquivo para descriptografar (ex: votos_criptografados.txt): ")
        descriptografar_e_validar(nome_arquivo)
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()
