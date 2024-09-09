
menu = """
[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair
"""

print(menu)

opcao = 0

saldo = 1000
LIMITE_SAQUE = 500
LIMITE_DIARIO = 3
extrato = ''

while opcao != 3 : 

    opcao = int(input("Escolha o tipo de transação: "))

    if opcao == 0:
        deposito = float(input("Informe o valor do deposito: "))
        saldo += deposito

        print('Depositando...')
        print(f'Saldo atual: R${saldo}')
    elif opcao == 1:
        if LIMITE_DIARIO <= 0:
            print('Limite de saque diário excedido.')
            break
        saque = float(input('Informe o valor do saque: '))
        if saque > 500:
            print('O valor máximo por saque é R$500.00.')
            break     
        if saque > saldo:
            print('Saldo insuficiente!')
            break
        saldo -= saque
        LIMITE_DIARIO = LIMITE_DIARIO - 1
        extrato += f'Saque realizado de R${saque:.2f}\n'
        print("Sacando...")
        print('Saque realizado com sucesso!')

    elif opcao == 2:
        print('Carregando extrato...')
        print(f'Saldo atual: R${saldo:.2f}')
        print(f'Valor total do depósito: R${deposito}')
        print(extrato)
        
    elif opcao == 3:
        print('Saindo...')
        break
    else:
        print('Opção inválida!')


























'''
        match opcao:
        case 0:
            deposito = float(input("kvlfkvcv"))
            saldo += deposito
            
            print('Depositando...')

        case 1:
            print("Sacando...")
        
        case 2:
            print("Extrato...")
        
        case 3:
            print("Saindo...")

        case _:
            print("Opção inválida")
            '''