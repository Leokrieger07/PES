medidas = []

while True:
    #    menu
    print("Menu:")
    print("1. Cadastrar")
    print("2. Excluir")
    print("3. Alterar")
    print("4. Listar")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    # Opção 1: Cadastrar
    if opcao == "1":
        nome = input("Nome: ")
        idade = input("Idade: ")
        altura = input("Altura (m): ")
        peso = input("Peso (kg): ")
        pessoa = [nome, idade, altura, peso]
        medidas.append(pessoa)
        print("Pessoa cadastrada com sucesso.")

    # Opção 2: Excluir
    elif opcao == "2":
        nome = input("Digite o nome da pessoa a ser excluída: ")
        for pessoa in medidas:
            if pessoa[0] == nome:
                medidas.remove(pessoa)
                print("Pessoa excluída com sucesso.")
                break
        else:
            print("Pessoa não encontrada.")

    # Opção 3: Alterar
    elif opcao == "3":
        nome = input("Digite o nome da pessoa a ser alterada: ")
        for pessoa in medidas:
            if pessoa[0] == nome:
                pessoa[1] = input("Nova idade: ")
                pessoa[2] = input("Nova altura (m): ")
                pessoa[3] = input("Novo peso (kg): ")
                print("Informações atualizadas com sucesso.")
                break
        else:
            print("Pessoa não encontrada.")

    # Opção 4: Listar
    elif opcao == "4":
        print("\nMedidas corpóreas cadastradas:")
        for pessoa in medidas:
            print("Nome:", pessoa[0])
            print("Idade:", pessoa[1])
            print("Altura:", pessoa[2], "m")
            print("Peso:", pessoa[3], "kg")
            print()

    # Opção 0: Sair
    elif opcao == "0":
        print("Saindo...")
        break

    # Opção inválida
    else:
        print("Opção inválida. Escolha novamente.")
