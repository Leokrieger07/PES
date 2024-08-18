cadastro=[]

while True:
    print("\n1 - Cadastrar")
    print("2 - Excluir")
    print("3 - Alterar")
    print("4 - Listar")
    print("0 - Sair")

    opcao=int(input("\nescolha uma opção valida: "))

    if opcao==1:
        nome=str(input("escreva o seu nome: "))
        idade=(input("escreva a sua idade: "))
        altura=float(input("escreva a sua altura: "))
        peso=float(input("escreva o seu peso: "))
        pessoa=[nome, idade, altura, peso]
        cadastro.append(pessoa)

    if opcao==2:
        nome=input("escreva o nome da pessoa que deseja excluir: ")
        for pessoa in cadastro:
            if pessoa[0]==nome:
                cadastro.remove(pessoa)
                print("pessoa excluida com sucesso!")
            else:
                print("pessoa não encontrada.")
        
    if opcao==3:
        nome=input("escreva o nome da pessoa que deseja excluir: ")
        for pessoa in cadastro:
            if pessoa[0] == nome:
                pessoa[1]= input("escreva a sua nova idade: ")
                pessoa[2] = float(input("escreva a sua nova altura: "))
                pessoa[3] = float(input("escreva o seu novo peso: "))
                print("\nmedidas alteradas com sucesso!")
    
    if opcao==4:
        x=int(input("digite 1 se deseja listar todos os cadastros e 2 para litar apenas um cadastro especifico."))
        if x==1:
            print("medidas cadastradas: ")
            for pessoa in cadastro:
                print("nome: ", pessoa[0])
                print("idade: ", pessoa[1])
                print("altura: ",pessoa[2])
                print("peso: ",pessoa[3])
        
        elif x==2:
            nome=input("escreva o nome da pessoa que deseja listar: ")
            for pessoa in cadastro: 
                if nome== pessoa[0]:
                    print("nome: ", pessoa[0])
                    print("idade: ", pessoa[1])
                    print("altura: ",pessoa[2])
                    print("peso: ",pessoa[3])
    
    if opcao==0:
        print("saindo...")
        break
