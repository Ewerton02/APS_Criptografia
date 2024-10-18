# APS_Criptografia
Trabalho APS Criptografia para sistema de urna eletrônica em Python.

Projeto APS: Urna Eletrônica com Criptografia e Hash gerado com o OS

Descrição
Este projeto foi desenvolvido como parte da APS (Atividades Práticas Supervisionadas) para a disciplina de Introdução à Programação Estruturada. O objetivo é implementar uma urna eletrônica capaz de cadastrar votos, criptografar os dados usando um método simples de criptografia (XOR) e garantir a integridade do arquivo gerado utilizando uma função de hash customizada com base na biblioteca os. Posteriormente, será desenvolvido um segundo programa para validar e apurar os votos de maneira segura.

Estrutura do Projeto
Programa 1: Cadastramento de Votos, Criptografia e Geração de Hash

- Cadastra os votos de diferentes candidatos.
- Criptografa os dados dos votos utilizando a operação XOR com uma chave fixa.
- Gera um hash dos dados criptografados usando uma função de hash customizada com o os para garantir a integridade.
- Salva os votos criptografados e o hash em um arquivo de texto.

Programa 2 (A ser implementado): Validação, Descriptografia e Apuração

- Validará o arquivo com base no hash gerado.
- Descriptografará os votos.
- Apurará e exibirá os resultados.

Pré-requisitos
- Python 3.x instalado no sistema.
- Utilização da biblioteca padrão os para a geração de um hash simples e personalizado.

Como Executar o Programa 1
1.Clone o repositório ou faça o download dos arquivos:

git clone <URL_do_repositório>
cd <diretório_do_projeto>


2.Execute o programa principal:
python programa_urna.py


3.Siga as instruções no terminal:
Digite o nome dos candidatos e quantidades de votos.
Quando terminar, digite "fim" para encerrar o cadastramento.

4.Verifique o arquivo gerado:
O programa salvará um arquivo chamado votos_criptografados.txt, contendo os votos criptografados e o hash gerado com o os.
Esse arquivo será utilizado pelo segundo programa para a validação e apuração.


Arquivo votos_criptografados.txt

Este arquivo contém:

1.Os votos criptografados.
2.O valor do hash gerado com o os, que será utilizado para verificar a integridade dos dados no segundo programa.

Exemplo de Conteúdo do Arquivo Gerado
ÊëÜé:1ÍÝãÜÜÜñ:2îòñññç,
f4a2d3e9b7a5f948a19c471c

Linha 1: Dados criptografados.
Linha 2: Hash gerado com o os dos dados criptografados.

Estrutura dos Arquivos
├── programa_urna.py          # Código do primeiro programa: Cadastra, Criptografa e Gera Hash com 'os'
├── votos_criptografados.txt  # Arquivo gerado contendo os votos criptografados e o hash gerado
└── README.md                 # Este arquivo

Licença
Este projeto é de código aberto e está disponível sob os termos da Licença MIT.
