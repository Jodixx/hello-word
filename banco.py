#deposito = 0 #Somente valores positivos todos os depositos devem ser atribuidos a uma variavel e mostrado na opcao extrato
#saque = 0 #realizar 3 saques diarios com limite de 500 se n tiver conta informar mensagem valores armazenados em extrado
#extrato = #exibir salto atual e valores de deposito e saque RS000,00

# Listas para armazenar usuários e contas
usuarios = []
contas_correntes = []
numero_sequencial = 1

def cadastrar_cliente(nome, data_nascimento, cpf, endereco):
    # Validar CPF (somente números e único)
    if not cpf.isdigit() or any(usuario['cpf'] == cpf for usuario in usuarios):
        print("CPF inválido ou já cadastrado.")
        return False
    
    # Adicionar cliente à lista de usuários
    usuarios.append({
        'nome': nome,
        'data_nascimento': data_nascimento,
        'cpf': cpf,
        'endereco': endereco
    })
    print("Cliente cadastrado com sucesso.")
    return True

def criar_conta_corrente(cpf_usuario):
    global numero_sequencial

    # Verificar se o usuário existe
    usuario = next((usuario for usuario in usuarios if usuario['cpf'] == cpf_usuario), None)
    if not usuario:
        print("Usuário não encontrado.")
        return False
    
    # Criar nova conta corrente
    conta = {
        'agencia': '0001',
        'numero_conta': numero_sequencial,
        'usuario': usuario
    }
    contas_correntes.append(conta)
    numero_sequencial += 1
    print("Conta corrente criada com sucesso.")
    return True

def saque(*, saldo, valor, extrato, limite, numero_saques):
    if valor > saldo:
        print("Saldo insuficiente.")
        return saldo, extrato
    elif valor > limite:
        print("Valor excede o limite permitido.")
        return saldo, extrato
    elif numero_saques <= 0:
        print("Número máximo de saques excedido.")
        return saldo, extrato
    else:
        saldo -= valor
        extrato.append(f"Saque: R${valor:.2f}")
        numero_saques -= 1
        return saldo, extrato

def deposito(/, saldo, valor, extrato):
    saldo += valor
    extrato.append(f"Depósito: R${valor:.2f}")
    return saldo, extrato

def exibir_extrato(*, saldo, extrato):
    print("\nExtrato:")
    for transacao in extrato:
        print(transacao)
    print(f"\nSaldo atual: R${saldo:.2f}")

# Função principal com menu interativo
def main():
    saldo = 0
    limite = 500
    extrato = []
    numero_saques = 3
    LIMITE_SAQUES = 3

    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    => """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Digite o valor do depósito: R$"))
            if valor <= 0:
                print("Valor inválido")
            else:
                saldo, extrato = deposito(saldo, valor, extrato)
                print(f"O valor de R${valor} foi depositado com sucesso")

        elif opcao == "s":
            valor = float(input("Digite o valor do saque: R$"))
            saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques)
            if saldo != saldo:  # Verificação se saldo foi alterado, confirmando saque realizado
                numero_saques -= 1
                print(f"Operação realizada com sucesso! O valor de R${valor} foi retirado de sua conta")

        elif opcao == "e":
            exibir_extrato(saldo=saldo, extrato=extrato)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Exemplos de uso das funções de cadastro e criação de conta
cadastrar_cliente("João Silva", "01/01/1980", "12345678901", "Rua A, 100-Centro-Cidade/SP")
cadastrar_cliente("Maria Souza", "15/05/1990", "98765432100", "Av B, 200-Bairro-Cidade/SP")

criar_conta_corrente("12345678901")
criar_conta_corrente("98765432100")

# Chamar a função principal
main()
