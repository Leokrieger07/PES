perguntas=["Telefonou para a vítima?", "Esteve no local do crime?", "Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?" ]

cont=0

for i in range(len(perguntas)):
    print("")
    print(perguntas[i])
    resp=int(input("\nrespoda com 1- para sim e 0 para não: "))
    cont=cont+resp

if cont==2:
    print("v\nocê é suspeito!")

elif cont == 3 or cont == 4:
    print( "\nvocê é cumplice! ")

elif cont==5:
    print("\nvocê é um assassino! ")

else:
    print("\nvocê é inocente! ")
