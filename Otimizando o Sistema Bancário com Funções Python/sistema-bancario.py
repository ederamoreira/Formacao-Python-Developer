contas = []
usuarios = []

saldo = 0
limite = 500
extrato = ''''''
numero_saques = 0
LIMITE_SAQUES = 3



def menu():
    menu = """
    [d] Depositar 
    [s] Sacar 
    [e] Extrato 
    [u] Novo usuário 
    [c] Nova conta
    [q] Sair 
    
    =>"""
    print(' Menu '.center(50, '='))
    print(menu, end=' ')
    botao = input()

    return botao


def arrumar_cpf(cpf):
    cpf_arrumado =  ''.join([i for i in cpf if (i != '.' and i != '-')])
    return cpf_arrumado


def sacar(*, saldo, saque, extrato, limite, numero_saques, limite_saques):

    if numero_saques < limite_saques:
        if saque <= saldo:
            if saque <= limite:
                saldo -= saque
                extrato += f'Saque: R$ {saque: .2f}\n'
                numero_saques += 1
            else:
                print('O valor máximo a ser sacado é de R$ 500.00')

        else: 
            print('Não é possível sacar o dinheiro, saldo insuficiente.')

    else:
        print('Saque não realizado. O limite de saques diários já foi atingido.')
    
    return saldo, extrato, numero_saques


def depositar(saldo, deposito, extrato, /):

    if deposito > 0:
        saldo += deposito
        extrato += f'Deposito: R$ {deposito:.2f}\n'

    else:
        print('O valor depositado deve ser maior que R$ 0.00')
    
    return saldo, extrato
    

def mostrar_extrato(saldo, *, extrato):

    if len(extrato) > 0:
        print(extrato)
        print(f'Saldo atual: R$ {saldo: .2f}')
    else:
        print('Não foram realizadas movimentações')


def criar_usuario(nome, nascimento, cpf, endereco : list):

    novo_usuario = {}
    cpf =  arrumar_cpf(cpf)
    criar_usuario = True

    for usuario_existente in usuarios:
        if cpf == usuario_existente['cpf']:
            criar_usuario = False
            print('Você já é um usuário.')
    
    if criar_usuario:
        novo_usuario['nome'] = nome.strip().title()
        novo_usuario['cpf'] = cpf
        novo_usuario['data de nascimento'] = nascimento
        Endereco = list(map(lambda x: x.title(), endereco))
        Endereco[3] = Endereco[3].upper()
        novo_usuario['endereço'] = f'{Endereco[0]} - {Endereco[1]} - {Endereco[2]}/{Endereco[3]}'
    
    usuarios.append(novo_usuario)

    print('Usuário cadastrado com sucesso!')
    

def criar_conta_corrente():

    cpf = input('Informe o cpf: ')
    cpf = arrumar_cpf(cpf)

    for usuario_existente in usuarios:
        if cpf == usuario_existente['cpf']:
            numero = 0
            for conta in contas:
                if conta['usuario'] == usuario_existente:
                    numero += 1
            nova_conta= {
                'agencia': '0001', 
                'numero': numero +1, 
                'usuario': usuario_existente
                }
            contas.append(nova_conta)
            print('Conta criada com sucesso!')
            print(f"Agência: {nova_conta['agencia']}, Número: {nova_conta['numero']}")
            return
    else:
        print('Não é possível criar uma conta.')
        print('Não existe um usuário com o cpf informado.')
    
    return
    

def display(botao, saldo, limite, extrato, numero_saques, limite_saques = LIMITE_SAQUES):

    operacao = {
            'd': 'Depositar', 
            's': 'Sacar', 
            'e': 'Extrato', 
            'u': 'Novo usuario', 
            'c': 'Nova conta', 
            'q': 'Sair'
            }

    continuar = True

    print(f' {operacao[botao]} '.center(50, '='))
    print('')

    if botao == 'd':
        valor = int(input('Informe o valor a ser depositado: R$ '))
        
        saldo, extrato = depositar(saldo, valor, extrato)
    
    elif botao == 's':
        valor = int(input('Informe o valor a se sacado: R$ '))
        saldo, extrato, numero_saques = sacar(
            saldo = saldo, 
            saque= valor, 
            extrato= extrato, 
            limite= limite, 
            numero_saques=numero_saques,
            limite_saques= limite_saques
            )

    elif botao == 'e':
        mostrar_extrato(
            saldo,
            extrato= extrato
        )
    
    elif botao == 'u':
        nome = input('Informe seu nome: ')
        nascimento = input('Informe sua data de nascimento: ')
        cpf = input('Informe seu cpf (não usar pontos e traços): ')
        logradouro = input('Informe o logradouro de sua residência: ')
        numero_residencia = input('Informe o número de sua residência: ')
        bairro = input('Informe o bairro onde mora: ')
        cidade = input('Informe a cidade onde mora: ')
        estado = input('Informe a sigla do estado: ')
        endereco = [logradouro, numero_residencia, bairro, cidade, estado]
        criar_usuario(nome, nascimento, cpf, endereco)
    
    elif botao == 'c':
        criar_conta_corrente()
        
    
    elif botao == 'q':
        continuar = False   


    return continuar, saldo, extrato, numero_saques

continuar = True

while continuar:
    print('')
    botao = menu()

    print('')

    continuar, saldo, extrato, numero_saques = display(
                                                    botao, 
                                                    saldo, 
                                                    limite, 
                                                    extrato, 
                                                    numero_saques, 
                                                    limite_saques = LIMITE_SAQUES
                                                    )