menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """
saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
limite_de_saques = 3

while True:

    opcao = input(menu)

    if opcao == "d":
       valor = float(input("informe o valor do depósito: "))
    
       if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
       else:
        print("operação falhou, o valor informado é inválido.")
    
   
    elif opcao == "s":
      valor = float(input("informe o vavlor do seu saque:\n"))

      excedeu_saldo = valor > saldo

      excedeu_limite = valor > limite_de_saques

      numero_de_saques = numero_de_saques >= limite_de_saques 

      if excedeu_limite:
        print("operação falhou, você não tem limite suficiente")

      if numero_de_saques:
        print("operação falhou, você não tem mais saques disponíveis")

      if excedeu_saldo:
        print("você não tem saldo suficiente")
      
      elif valor > 0:
        saldo -= valor
        extrato += f"saque R$ {valor:.2f}\n"
        numero_de_saques += 1

      else:
        print("operação falhou, saldo inválido")
    
    elif  opcao == "e":
          print("\n =========== EXTRATO ============")
          print ("não foram realizadas movimentações." if not extrato else extrato)
          print (f"\n Saldo: R$ {saldo:.2f}")
          print ("=================================")

    elif opcao == "q":
         break
    else:
       print("operação inválida, selecione novamente.")


