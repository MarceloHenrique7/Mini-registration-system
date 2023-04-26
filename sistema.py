from datetime import date
import ast
from time import sleep

a = open("dadoscadastro.txt", "a+")
a.close()



def linha(tam=42):
    return '-' * tam


def cabecalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor, digite um número inteiro valido.\033[m')
        except KeyboardInterrupt:
            print('\033[31mO usuario preferiu não informar o número.\033[m')
        else:
            return n


def leiastr(msg):
    while True:
        try:
            n = str(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO! Digite um Sexo valido, Apenas M ou F\033[m')
        except KeyboardInterrupt:
            print('\033[31mERRO! Digite um Sexo valido, Apenas M ou F\033[m')
        else:
            return n

arquivo = open("dadoscadastro.txt", "r")
linhas = arquivo.readlines()
arquivo.close()
codigo = 0
for linhass in linhas:
    codigo += 1




def Cadastro(nome='<desconhecido>', idade=0, sexo='não informado'):

    arquivo = open("dadoscadastro.txt", "a")
    nome = input('Nome: ').upper()
    nascimento = leiaInt('Ano de nascimento: ')
    atual = date.today().year
    idade = atual - nascimento
    sexo = str(input('Sexo: [M/F] ')).upper()[0]
    while sexo not in 'MF':
        print('\033[31mERRO! Digite um Sexo valido, Apenas M ou F\033[m')
        sexo = str(input('Sexo: [M/F] ')).upper()[0]


    email = str(input('Digite o email: '))
    salario = float(input('Salario do funcionario: R$').replace(',', '').replace('.', ''))


    usuario = {"nome": nome,"data de nascimento": nascimento, "idade": idade, "sexo": sexo, "email": email, "salario": f'{salario:.2f}, "codigo": {codigo}'}
    arquivo.write(str(usuario) + "\n")
    arquivo.close()

    print(linha())
    print('\033[32mCadastrado com sucesso.\033[m')
    print(linha())


def ler_arquivo():
    print(linha())
    print('<FUNCIONARIOS CADASTRADOS>'.center(42))
    print(linha())
    arquivo = open("dadoscadastro.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    indice = 0
    for linhass in linhas:
        print(f'{linhass}')
        indice += 1

    if len(linhas) == 0:
        print('Não Existe Registros aqui.')

def remover_cadastro():
    codigo = leiaInt('Digite o código do funcionário a ser removido: ')
    arquivo = open("dadoscadastro.txt", "r")
    linhas = arquivo.readlines()
    arquivo.close()
    indice = 0
    encontrado = False
    for linha in linhas:
        if f'"codigo": {codigo}' in linha:
            encontrado = True
            break
        indice += 1
    if encontrado:
        del linhas[indice]
        arquivo = open("dadoscadastro.txt", "w")
        arquivo.writelines(linhas)
        arquivo.close()
        print('-'*42)
        print(f'\033[32mFuncionário com código {codigo} removido com sucesso.\033[m')
        print('-'*42)
    else:
        print('-'*42)
        print(f'\033[31mNão foi encontrado nenhum funcionário com código {codigo}.\033[m')
        print('-'*42)



while True:
    print(linha())
    print('CADASTRO DE FUNCIONARIOS DA EMPRESA'.center(42))
    print(linha())

    print('[1] - CADASTRAR NOVA PESSOA\n'
            '[2] - VER LISTA DE FUNCIONARIOS CADASTRADOS\n'
            '[3] - REMOVER CADASTRO\n'
            '[4] - SAIR')

    print(linha())
    opc = leiaInt('Digite sua opção: ')
    print(linha())

    while opc != 1 and opc != 2 and opc != 3 and opc != 4:
        print('\033[31mERRO!Digite uma opção valida!\033[m')
        opc = leiaInt('Digite sua opção: ')
    if opc == 1:
        Cadastro()
    if opc == 2:
        ler_arquivo()
    if opc == 3:
        remover_cadastro()
    if opc == 4:
        print('\033[97mUM MOMENTO...\033[m')
        sleep(3)
        print('\033[33mATÉ LOGO, VOLTE SEMPRE!\033[m')
        break
