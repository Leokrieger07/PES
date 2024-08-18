letras = [0]*10
vogais = ["a", "e", "i", "o", "u"]
cont=0

for i in range (10):
    letra = str(input(f"escreva a sua letra numero {i+1}: "))
    if letra not in vogais:
        cont+=1
    letras[i] = letra

print("consoantes digitadas: ")

for letra in letras:
    if letra not in vogais:
        print(letra)

print("O numero de consoeantes lidas foi: ", cont)

