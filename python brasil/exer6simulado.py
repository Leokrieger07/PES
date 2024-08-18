produtos=[""]*10

while True:
    print("\nMenu:\n------\n1. Cadastrar\n2. Listar todos\n0. Sair")
    opcao=int(input("escoha uma opção valida: "))

    if opcao==1:
        nome=str(input("escreva o nome do produto que deseja cadastrar: "))
        if nome == '""':
            print("nome invalido.")
        else:
            if nome in produtos:
                print("produto ja cadastrado")
            else:
                if "" in produtos:
                    produtos[produtos.index("")]=nome
                    print("produto cadastrado com sucesso!")

    elif opcao==2:
        print("produtos cadastrados: ")
        for nome in produtos:
            if nome!="":
                print("\n",nome)

    elif opcao==0:
        print("saindo...")
        break

    else:
        print("opção invalida.Por favor escolçha um opção valida")
        