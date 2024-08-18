saltos=[]
nome=0

while True:
    print("\npara sair do programa, digite SAIR")
    nome=str(input("\nescreva o nome do atleta:"))
    if nome=="sair" or nome=="SAIR":
        break

    for i in range(5):
        salto=float(input(f"escreva a distancia do seu {i+1}° salto: "))
        saltos.append(salto)

    media=sum(saltos)/len(saltos)

    print("atleta: ",nome)
    for i in range (5):
        print(f"\n{i+1}° salto: ", saltos[i],"m")
    
    print("\nresultado final:")
    print("\natleta: ",nome)

    print("saltos: ",saltos[0], "-" ,saltos[1], "-", saltos[2], "-" ,saltos[3], "-" ,saltos[4])
    print("\nmedia dos saltos: ",media)