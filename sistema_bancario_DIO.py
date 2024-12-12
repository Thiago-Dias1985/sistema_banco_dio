menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """
#variáveis para armazenamento dos valores.
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
#estrutura while para repetir o programa enquanto o usuário não optar por sair do sistema.
while True:

    opcao = input(menu)
#condição "d" executada caso o usuário decida depositar dinheiro na conta.
    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")
#condição "s" executada caso o usuário decida sacar dinheiro da conta.
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print (f"operação realizada com sucesso,R${valor:.2f} \n Aguarde contando as notas ....... ")

        else:
            print("Operação falhou! O valor informado é inválido.")
# condição "e" executada quando o usuário optar pela opção extrato.
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
# condição "q" executará o comando break ,quando o usuário decidir parar a interação com o programa.
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
print ("***=====OBRIGADO POR UTILIZAR NOSSO BANCO=====***")