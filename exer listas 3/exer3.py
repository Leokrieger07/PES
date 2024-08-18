# Inicializando a lista de códigos com valores -1
codigos = [-1] * 10

# Loop principal do programa
opcao=0
while opcao!=3:

    # Exibir o menu
    print("Menu:")
    print("1. Cadastrar novo código")
    print("2. Listar códigos cadastrados")
    print("3. Sair")
    
    # Obter a opção do usuário
    opcao = input("Escolha uma opção: ")
    
    # Opção 1: Cadastrar novo código
    if opcao == "1":
        codigo = int(input("Digite o código do produto: "))
        if codigo == -1:
            print("Erro: Não é possível cadastrar um produto com código -1.")
        elif codigo in codigos:
            print("Erro: Código já cadastrado.")
        elif -1 in codigos:
            codigos[codigos.index(-1)] = codigo
            print("Código cadastrado com sucesso.")
        else:
            print("Erro: Limite de códigos cadastrados atingido.")
    
    # Opção 2: Listar códigos cadastrados
    elif opcao == "2":
        print("\nCódigos cadastrados:")
        for codigo in codigos:
            if codigo != -1:
                print(codigo)
    
    # Opção 3: Sair do programa
    elif opcao == "3":
        print("Saindo do programa...")
        break
    
    # Opção inválida
    else:
        print("Opção inválida. Escolha novamente.")
