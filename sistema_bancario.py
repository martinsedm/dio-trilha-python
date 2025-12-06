import textwrap

def menu():
menu_text = """\n
========== BANCO ESCOLAR ==========
[d] Depositar
[s] Sacar
[e] Exibir extrato
[nu] Novo usuário
[nc] Nova conta
[lc] Listar contas
[q] Sair
=> """
return input(textwrap.dedent(menu_text)).strip().lower()

def depositar(saldo, valor, extrato):
"""Deposita um valor positivo no saldo e registra no extrato."""
if valor <= 0:
print("\nOperação falhou: informe um valor de depósito positivo.")
return saldo, extrato

saldo += valor
extrato += f"Depósito:\tR$ {valor:.2f}\n"
print(f"\nDepósito realizado! Novo saldo: R$ {saldo:.2f}")
return saldo, extrato
def sacar(saldo, valor, extrato, limite, numero_saques, limite_saques):
"""
Realiza saque respeitando saldo, limite por saque e limite de saques diários.
Retorna saldo, extrato e numero_saques atualizados.
"""
# Validar valor
if valor <= 0:
print("\nOperação falhou: informe um valor de saque positivo.")
return saldo, extrato, numero_saques

excedeu_saldo = valor > saldo
excedeu_limite = valor > limite
excedeu_saques = numero_saques >= limite_saques

if excedeu_saldo:
    print("\nOperação falhou: saldo insuficiente.")
elif excedeu_limite:
    print(f"\nOperação falhou: o valor excede o limite por saque (R$ {limite:.2f}).")
elif excedeu_saques:
    print("\nOperação falhou: número máximo de saques diários atingido.")
else:
    saldo -= valor
    extrato += f"Saque:\t\tR$ {valor:.2f}\n"
    numero_saques += 1
    print(f"\nSaque realizado! Novo saldo: R$ {saldo:.2f}")

return saldo, extrato, numero_saques
def exibir_extrato(saldo, /, *, extrato):
"""Exibe o extrato e o saldo atual de forma didática."""
print("\n================ EXTRATO ================")
if not extrato:
print("Nenhuma movimentação realizada.")
else:
print(extrato)
print(f"Saldo atual:\tR$ {saldo:.2f}")
print("=========================================")

def criar_usuario(usuarios):
"""Cria um novo usuário se o CPF não estiver cadastrado."""
cpf = input("Informe o CPF (somente números): ").strip()
if not cpf.isdigit():
print("\nCPF inválido: utilize apenas números.")
return

usuario = filtrar_usuario(cpf, usuarios)
if usuario:
    print("\nJá existe usuário cadastrado com esse CPF.")
    return

nome = input("Informe o nome completo: ").strip()
data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ").strip()
endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ").strip()

usuarios.append({
    "nome": nome,
    "data_nascimento": data_nascimento,
    "cpf": cpf,
    "endereco": endereco
})

print("\nUsuário criado com sucesso!")
def filtrar_usuario(cpf, usuarios):
"""Retorna o usuário com o CPF informado, ou None."""
usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
"""Cria uma conta associada a um usuário já cadastrado."""
cpf = input("Informe o CPF do titular da conta: ").strip()
usuario = filtrar_usuario(cpf, usuarios)

if usuario:
    conta = {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nConta criada com sucesso!")
    return conta

print("\nUsuário não encontrado. Cadastre o usuário antes de criar a conta.")
return None
def listar_contas(contas):
"""Mostra todas as contas cadastradas."""
if not contas:
print("\nNenhuma conta criada ainda.")
return

print()
for conta in contas:
    linha = f"""\ 
    Agência:\t{conta['agencia']}
    Conta:\t\t{conta['numero_conta']}
    Titular:\t{conta['usuario']['nome']}
    """
    print("-" * 60)
    print(textwrap.dedent(linha))
print("-" * 60)
def main():
# Configurações do Banco Escolar
LIMITE_SAQUES = 3
AGENCIA = "ESCOLA-01"
LIMITE_POR_SAQUE = 200 # limite por saque (ajustado para ambiente escolar)

# Estado inicial (simples, global para a sessão)
saldo = 0.0
extrato = ""
numero_saques = 0

usuarios = []
contas = []

print("Bem-vindo ao Banco Escolar — ambiente de aprendizagem.\n")

while True:
    opcao = menu()

    if opcao == "d":
        try:
            valor = float(input("Informe o valor do depósito: ").strip())
        except ValueError:
            print("\nValor inválido. Use apenas números.")
            continue

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":
        try:
            valor = float(input("Informe o valor do saque: ").strip())
        except ValueError:
            print("\nValor inválido. Use apenas números.")
            continue

        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=LIMITE_POR_SAQUE,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES,
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "nu":
        criar_usuario(usuarios)

    elif opcao == "nc":
        numero_conta = len(contas) + 1
        conta = criar_conta(AGENCIA, numero_conta, usuarios)
        if conta:
            contas.append(conta)

    elif opcao == "lc":
        listar_contas(contas)

    elif opcao == "q":
        print("\nEncerrando o sistema. Até logo!")
        break

    else:
        print("\nOpção inválida. Por favor selecione uma operação do menu.")
if name == "main":
main()
