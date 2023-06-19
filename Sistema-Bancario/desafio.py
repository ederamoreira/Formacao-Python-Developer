menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
=> """

saldo = 0
deposito = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == '1':
        deposito = float(input('Digite o valor para depósito:'))

        if deposito > 0:
            saldo = saldo + deposito
            print(f'Saldo: R${saldo}')
            extrato += (f'\nDepósito: R$ {deposito:.2f}')
        else:
            print('Digite um valor válido!')

    elif opcao == '2':

        while True:
            if numero_saques >= LIMITE_SAQUES:
                print('Limite máximo de saques exedido!')
                break

            saque = float(input('Digite o valor que deseja sacar:'))

            if saque > saldo:
                print('Saldo insuficiente!')
                break

            if saque >= 500:
                print('Limite máximo por saque de R$ 500,00 excecido.')
                break

            if saque > 0:
                if saque > 0 and deposito == 0:
                    break
                else:
                    saldo = saldo - saque
                    extrato += (f'\nSaque: R$ -{saque}')
                    print(f'Saldo: R${saldo}')
                    numero_saques += 1
                    break
            else:
                print('Valor informado inválido!')
    elif opcao == '3':
        print('=================EXTRATO=================')
        print('Não foram realizados movimentações em sua conta.' if not extrato else extrato)
        print(f'Saldo: R$ {saldo:.2f}')
        print('=========================================')

    elif opcao == '4':
        print('Saindo...')
        break
    else:
        print('Operação inválida!')
