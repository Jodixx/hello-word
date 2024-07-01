#deposito = 0 #Somente valores positivos todos os depositos devem ser atribuidos a uma variavel e mostrado na opcao extrato
#saque = 0 #realizar 3 saques diarios com limite de 500 se n tiver conta informar mensagem valores armazenados em extrado
#extrato = #exibir salto atual e valores de deposito e saque RS000,00

menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0
limite = 500
extrato_de_depositos = []
extrato_de_saques = []
numero_saques = 0
LIMITE_SAQUES = 3
deposito = 0


while True:
    opcao = input(menu)

    if opcao =="d":
        deposito=float(input("Digite o valor do deposito: R$"))        
        if deposito <=0:
            print("Valor inválido")
        
        else:
            deposito_formatada = ""
            deposito_formatada = f"R${deposito:.2f}"


            extrato_de_depositos.append(deposito_formatada)
            saldo += deposito
            print(f"O valor de R${deposito} foi depositado com Sucesso")
            
    
    elif opcao =="s":
        saque = float(input("Digite o valor de Saque: R$"))
        if saque > saldo:
            print(f"Operação Invalida! Saldo insuficiente para ação! Seu saldo atual é R${saldo}.")
        elif saque > 500:
            print("Limite de R$500,0 por Saque. Operação não realizada")
        
        elif LIMITE_SAQUES <= numero_saques:
            print(f"Limite de Saque no dia Excedido, operação Invalida")
            print(numero_saques)
        
        else:   
            saque_formatada = ""
            saque_formatada = f"R${saque:.2f}"
            saldo -= saque 
            numero_saques += 1
            
            extrato_de_saques.append(saque_formatada)
            print(f"Operação Realizada com Sucesso! O valor de R${saque} foi retirado de sua conta")

        

    elif opcao == "e":
        
        print(f"DEPOSITO (S):{extrato_de_depositos}")
        print(f"SAQUE (S):{extrato_de_saques}")
        print(f"Seu Saldo Atual é de: R${saldo:.2f}")
    elif opcao =="q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


