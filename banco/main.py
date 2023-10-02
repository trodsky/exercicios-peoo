contas_bancarias = []
def criar_conta(numero_conta, nome_pessoa, saldo_inicial):
    conta = {"Número da Conta": numero_conta, "Nome da Pessoa": nome_pessoa, "Saldo": saldo_inicial}
    contas_bancarias.append(conta)
    print(f'Conta criada com sucesso para {nome_pessoa}!')

def exibir_saldo(numero_conta):
    for conta in contas_bancarias:
        if conta["Número da Conta"] == numero_conta:
            print(f'Saldo da conta de {conta["Nome da Pessoa"]}: R${conta["Saldo"]}')
            return
    print(f'Conta com número {numero_conta} não encontrada.')

def sacar(numero_conta, valor):
    for conta in contas_bancarias:
        if conta["Número da Conta"] == numero_conta:
            if valor <= conta["Saldo"]:
                conta["Saldo"] -= valor
                print(f'Saque de R${valor} realizado com sucesso na conta de {conta["Nome da Pessoa"]}.')
            else:
                print('Saldo insuficiente para realizar o saque.')
            return
    print(f'Conta com número {numero_conta} não encontrada.')

def depositar(numero_conta, valor):
    for conta in contas_bancarias:
        if conta["Número da Conta"] == numero_conta:
            conta["Saldo"] += valor
            print(f'Depósito de R${valor} realizado com sucesso na conta de {conta["Nome da Pessoa"]}.')
            return
    print(f'Conta com número {numero_conta} não encontrada.')

def transferir(origem, destino, valor):
    for conta_origem in contas_bancarias:
        if conta_origem["Número da Conta"] == origem:
            for conta_destino in contas_bancarias:
                if conta_destino["Número da Conta"] == destino:
                    if valor <= conta_origem["Saldo"]:
                        conta_origem["Saldo"] -= valor
                        conta_destino["Saldo"] += valor
                        print(f'Transferência de R${valor} realizada com sucesso de {conta_origem["Nome da Pessoa"]} para {conta_destino["Nome da Pessoa"]}.')
                    else:
                        print('Saldo insuficiente para realizar a transferência.')
                    return
            print(f'Conta de destino com número {destino} não encontrada.')
            return
    print(f'Conta de origem com número {origem} não encontrada.')

#def emprestimo(valor):


def main():
    while True:
        print("Bem  Vindo ao Banco Mesa Verde")
        print("Opções disponíveis:")
        print("1. Criar nova conta")
        print("2. Exibir saldo")
        print("3. Sacar")
        print("4. Depositar")
        print("5. Transferir")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            numero = int(input("Digite o número da conta: "))
            nome = input("Digite o nome da pessoa: ")
            saldo = float(input("Digite o saldo inicial: "))
            criar_conta(numero, nome, saldo)
        elif opcao == '2':
            numero = int(input("Digite o número da conta: "))
            exibir_saldo(numero)
        elif opcao == '3':
            numero = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do saque: "))
            sacar(numero, valor)
        elif opcao == '4':
            numero = int(input("Digite o número da conta: "))
            valor = float(input("Digite o valor do depósito: "))
            depositar(numero, valor)
        elif opcao == '5':
            origem = int(input("Digite o número da conta de origem: "))
            destino = int(input("Digite o número da conta de destino: "))
            valor = float(input("Digite o valor da transferência: "))
            transferir(origem, destino, valor)
        elif opcao == '6':
            print("Obrigado por usar o nosso banco!")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
