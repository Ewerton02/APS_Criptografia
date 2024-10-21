# Importa a biblioteca padrão OS do Python
import os

# Sistema ALT de Votação:

# Função para a contagem de votos
# (SERÁ USADA PARA MOSTRAR O RESULTADO DAS ELEIÇÕES)
def resultado(tiao, ze, branco):
    candidatos = ["Tião do gás", "Zé da feira", "Branco"]
    contagem = {candidatos[0]: tiao, candidatos[1]: ze, candidatos[2]: branco}
    return contagem

# Função para confirmar voto assim como o BOTÃO VERDE na urna
# (SERÁ USADO DURANTE A FUNÇÃO DO VOTO ÚNICO aka 'voto()')
def confirmacao():
    confirma = input("Digite \"c\" para confirmar o voto:")
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
    voto_aberto = True  # Função do voto continuará enquanto a variável for True:
    voto_registrado = ""
    while voto_aberto:  # Mostra as opções de candidatos
        print("\n" + "-=-" * 8)
        print("Opções de Voto:")
        print("-=-" * 8)
        print("1 - Tião do Gás")
        print("2 - Zé da Feira")
        print("3 - Branco")
        print("-=-" * 8)
        voto_registrado = input("Digite sua opção de voto:").strip()
        print("-=-" * 8)
        # Cria as condições para cada voto
        # e chama a função 'confirmacao()' para confirmar o voto,
        # se não for confirmado volta à seleção de candidatos
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

seccao_aberta = True  # A secção continuará enquanto a variável for True

# A urna começa com 0 votos para todos os candidatos
votos_tiao = 0
votos_ze = 0
votos_branco = 0

results = ""  # Variável que vai conter o resultado das eleições (pré-criptografia)

# Iniciando a votação:

print("-=-" * 8)
print("Iniciando Votação")
while seccao_aberta:  # Validação do mesário se terá um novo votante ou secção encerrada
    print("-=-" * 8)
    print("1 - Novo Votante")
    print("2 - Encerrar Secção")
    print("-=-" * 8)
    novo_voto = input("\n")
    if novo_voto == "1":  # If para confirmação de um novo votante
        voto_individual = voto()
        if voto_individual == '1':  # If para registrar qual candidato esse voto único foi
            votos_tiao += 1
        if voto_individual == '2':
            votos_ze += 1
        if voto_individual == '3':
            votos_branco += 1
    elif novo_voto == "2":
        print("Secção Encerrada")
        # IMPORTANTE:
        results = resultado(votos_tiao, votos_ze, votos_branco)  # Variável para armazenar os resultados
        # print(results)  # Descomentar para verificar os resultados
        seccao_aberta = False  # Fim da secção

# Agora é a parte do código para criptografar os dados usando o XOR

#FUNÇÃO PARA CRIPTOGRAFIA XOR
def criptografar_votos(resultados, chave):
    votos_criptografados = ""
    #converte o resultados dos votos em uma string 
    dados_votos  = f"Tião do Gás: {resultados['Tião do gás']}, Zé da Feira: {resultados['Zé da feira']}, Branco: {resultados['Branco']}"

    #aplica o xor em cada caractere
    for char in dados_votos:
        votos_criptografados += chr(ord(char) ^ chave)

    return votos_criptografados

#definindo uma chave de criptografia
chave_criptografia = 12345

#criptografando os resultados
votos_criptografados = criptografar_votos(results, chave_criptografia)
print("Votos criptografados:", votos_criptografados)