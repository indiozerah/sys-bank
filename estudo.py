print("Olá, seja bem vindo ao nosso banco!")
print("Selecione no menu abaixo o serviço que você deseja!")
menu = """
Para deposito digite [d] 

Para sacar digite [s]  

Para extrato digite [e]

Para sair digite [s]

Digite uma opção: """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do deposíto: "))

        if valor > 0:
            saldo += valor
        
        else:
            print("Operação falhou, o valor informado é inválido!")



    elif opcao == "s":
        valor = float(input("Informe o valor do saque"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação Falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques realizados.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}"
            numero_saques += 1
        
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("Extrato")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"Saldo R$ {saldo:.2f}")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


















