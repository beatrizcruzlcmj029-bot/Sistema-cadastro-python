cadastro = []

def menu():
    print("\n" + "=" * 40)
    print("  SISTEMA DE CADASTRO DE PESSOAS")
    print("=" * 40)
    print("  1. Cadastrar nova pessoa")
    print("  2. Listar todas as pessoas")
    print("  3. Buscar por nome")
    print("  4. Remover cadastro")
    print("  5. Sair")
    print("=" * 40)
    opcao = input("Escolha uma opção: ")
    return opcao

def cadastrar():
    print("\n--- NOVO CADASTRO ---")
    nome = input("Nome completo: ").strip()
    if nome == "":
        print("Nome não pode ser vazio!")
        return
    idade = input("Idade: ").strip()
    if not idade.isdigit():
        print("Idade inválida!")
        return
    email = input("E-mail: ").strip()
    telefone = input("Telefone: ").strip()
    pessoa = {
        "id": len(cadastro) + 1,
        "nome": nome,
        "idade": int(idade),
        "email": email,
        "telefone": telefone
    }
    cadastro.append(pessoa)
    print(f"✅ {nome} cadastrado com sucesso!")

def listar():
    print("\n--- LISTA DE CADASTROS ---")
    if len(cadastro) == 0:
        print("Nenhuma pessoa cadastrada.")
        return
    for pessoa in cadastro:
        print(f"ID: {pessoa['id']} | Nome: {pessoa['nome']} | Idade: {pessoa['idade']} | Email: {pessoa['email']}")
    print(f"\nTotal: {len(cadastro)} pessoa(s).")

def buscar():
    print("\n--- BUSCAR POR NOME ---")
    termo = input("Nome: ").strip().lower()
    resultados = [p for p in cadastro if termo in p["nome"].lower()]
    if len(resultados) == 0:
        print("Nenhum resultado encontrado.")
    else:
        for p in resultados:
            print(f"ID: {p['id']} | {p['nome']} | {p['idade']} anos | {p['email']}")

def remover():
    print("\n--- REMOVER CADASTRO ---")
    if len(cadastro) == 0:
        print("Nenhuma pessoa cadastrada.")
        return
    listar()
    try:
        id_remover = int(input("ID para remover: "))
    except ValueError:
        print("ID inválido!")
        return
    pessoa_encontrada = None
    for p in cadastro:
        if p["id"] == id_remover:
            pessoa_encontrada = p
            break
    if pessoa_encontrada is None:
        print("ID não encontrado.")
        return
    cadastro.remove(pessoa_encontrada)
    print(f"✅ {pessoa_encontrada['nome']} removido com sucesso!")

def main():
    print("Bem-vindo ao Sistema de Cadastro!")
    print("Desenvolvido por: Beatriz Cruz")
    while True:
        opcao = menu()
        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            buscar()
        elif opcao == "4":
            remover()
        elif opcao == "5":
            print("Até logo!")
            break
        else:
            print("Opção inválida!")

main()
