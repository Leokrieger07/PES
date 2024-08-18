medidas=[]

while True:
    print("menu")
    print("----")
    print("1.cadastrar")
    print("2.excluir")
    print("3.alterar")
    print("4.listar")
    print("0. sair")

    op=int(input("digite uma opção valida: "))

    if op == 0:
        print("saindo...")
        break

    if op == 1: 
        nome=str(input("escreva o seu nome: "))
        for pessoa in medidas:
            if pessoa[0] == nome:
                print('pessoa ja cadastrada.')
                break
            idade=int(input("escreva a sua idade: "))
            altura=float(input("escreva a sua altura: "))
            peso=float(input("escreva o seu peso: "))

        pessoa=[nome, idade, altura, peso]
        medidas.append(pessoa)
        print("pessoa cadastrada com sucesso!")

    
    if op == 2:
        nome=input("escreva o nome da pessoa que deseja excluir: ")
        for pessoa in medidas:
            if pessoa[0] == nome:
                medidas.remove(pessoa)
                print("pessoa excluida com sucesso!")
                break
            else:
                print("pessoa não encontrada.") 
    
    if op == 3:
        nome=input("escreva o nome da pessoa que deseja alterar os dados: ")
        for pessoa in medidas:
            if pessoa[0] == nome:
                pessoa[1]=int(input("escreva a nova idade: "))
                pessoa[2] = input("Nova altura (m): ")
                pessoa[3] = input("Novo peso (kg): ")
                print("Informações atualizadas com sucesso.")
                break
        else:
            print("Pessoa não encontrada.")

    if op == 4:
        print("\nmedidas corporeas cadastradas: ")
        for pessoa in medidas:
            print(pessoa[0])
            print(pessoa[1])
            print(pessoa[2])
            print(pessoa[3])
            print()

