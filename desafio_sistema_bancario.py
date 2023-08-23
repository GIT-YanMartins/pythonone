import textwrap


def menu():
 menu = """ \n
 ============MENU============
 [d] \tDepositar
 [s] \tSacar
 [e] \tExtrato
 [nc] \tNova Conta
 [lc] \tListar contas
 [nu] \tNovo Usuário
 [t] \tSair
 => """
 return input (textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
 if valor > 0:
  saldo += valor
  extrato += f"Depósito:\tR$ {valor:.2f}\n"
  print("\n === Depósito realizado com sucesso! ===")
 else:
  print("Operação inválida")
 return saldo, extrato


def sacar (*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
      print ("\n@@@ saldo insuficiente @@@")
    elif excedeu_limite:
      print ("\n @@@ sem limite em conta. @@@")
    elif excedeu_saques:
      print ("\n @@@ excedeu o limite de saques @@@")
    elif valor > 0:
      saldo -= valor
      extrato += f"Saque\t\t R$ {valor: .2f} \n"
      print ("\n === Saque bem sucedido. ===")

    else:
      print ("\n @@@ Valor inválido @@@")
    return saldo, extrato 


def exibir_extrato (saldo, /, *, extrato):
    print("\n =========== EXTRATO ============")
    print ("não foram realizadas movimentações." if not extrato else extrato)
    print (f"\n Saldo: R$ {saldo:.2f}")
    print ("=================================")

def criar_usuario (usuarios):
    cpf = input("informe o CPF (somente número):")
    usuario = filtrar_usuario (cpf, usuarios)

    if usuario: 
      print ("\n @@@ Já existe usuário com esse cpf @@@")
      return
    
    nome = input ("informe o nome completo:")
    data_nascimento = input ("informe a sua data de nascimento")
    endereco = input ("informe o seu endereço completo")

    usuarios.append ({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print ("@@@ Usuário criado com sucesso! @@@")


def filtrar_usuario (cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario ["cpf"] = cpf]
    return usuarios_filtrados [0] if usuarios_filtrados else None


def criar_usuario(usuarios):
    

    cpf =  input("Informe o seu CPF")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
      print ("\n @@@ já existe usuário com esse CPF @@@") 
      return
    nome = input ("informe o seu nome completo:")
    data_nascimento = input ("informe a sua data de nascimento:")
    endereco = input ("informe o seu endereço completo, por favor:")

    usuarios.append ({"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco})
    print ("=== cadastro realizado com sucesso ===")
  

def criar_conta(agencia, numero_conta, usuario):    
  cpf = input("informe o seu CPF")
  usuario = filtrar_usuario (cpf, usuarios)

  if usuario:
    print ("\n === Conta criada com sucesso ===")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
  
  print("@@@ usuario não encontrado @@@")
  return None
  

def listar_contas (contas):
  for conta in contas:
    linha = f"""\
          Agência:\t {conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['none']}
    """
    print("=" * 100)
    print(textwrap.dedent(linha))


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


