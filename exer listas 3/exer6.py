medidas = []
while True:
    print("Menu:")
    print("1. Cadastrar")
    print("2. Excluir")
    print("3. Alterar")
    print("4. Listar")
    print("0. Sair")

    opcao= input("escolha uma opção valida ")

#opçaõ 1:Cadastrar
    if opcao == "1":
        nome=input("nome: ")
        idade=input("idade: ")
        altura=input("altura: ")
        peso=input("peso: ")
        codigo=input("codigo: ")

        pessoa=[nome, idade, altura, peso, codigo]
        medidas.append(pessoa)

        print("pessoa cadastrada com sucesso!")

#opcao 2 :excluir
    elif opcao=="2":
        x=input("escreva 1 para excluir por nome e 2 para excluir por codigo")
        if x=="1":
            nome = input("escreva o nome da pessoa que deseja excluir")
            for pessoa in medidas:
                if pessoa[0] == nome:
                    medidas.remove(pessoa)
                    print("pessoa excluida com sucesso!")
        
        elif x=="2":
            codigo=input("escreva o codigo da pessoa que deseja excluir")
            for pessoa in medidas:
                if pessoa[4] == codigo:
                    medidas.remove(pessoa)
                    print("pessoa excluida com sucesso!")
                    break
                else: 
                    print("pessoa não encontrada")
    
            

#opcao 3 :alterar
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

#opcao 4:listar
    elif opcao=="4":
        y=input("digite 1 caso queira listar um pessoa especifica e 2 caso queira listar todos")
        if y=="1":
            nome=input("escreva o nome da pessoa que deseja listar: ")
            for pessoa in medidas:
                if pessoa[0]==nome:
                    print("Nome:", pessoa[0])
                    print("Idade:", pessoa[1])
                    print("Altura:", pessoa[2], "m")
                    print("Peso:", pessoa[3], "kg")
                    break
        
        elif y=="2":
            print("\nMedidas corpóreas cadastradas:")
        for pessoa in medidas:
            print("Nome:", pessoa[0])
            print("Idade:", pessoa[1])
            print("Altura:", pessoa[2], "m")
            print("Peso:", pessoa[3], "kg")
            print( )
            break
#sair
    elif opcao=="0":
        print("saindo...")
        break
    else:
        print("opção invalida. Por favor rescolha uma opção valida")

