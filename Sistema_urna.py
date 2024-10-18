import os

#Função para cadastrar os votos
def cadastrar_votos():
    votos = {"Tião do gás": 0, "Zé da feira": 0, "Branco": 0}
    while True:
        print("\nOpções de Voto:")
        print("1 - Tião do gás")
        print("2 - Zé da feira")
        print("3 - Branco")
        voto = input("Digite sua opção de voto (ou 'nulo' para encerrar): ").strip()

        if voto.lower() == 'nulo':
            break
        if voto == '1':
            votos["Tião do gás"] += 1
        elif voto == '2':
            votos["Zé da feira"] += 1
        elif voto == '3':
            votos["Branco"] += 1
        else:
            print("Voto inválido, tente novamente.")
    
    return votos

print("cadastro votos")
votos = cadastrar_votos()