# Lista para armazenar as notas
notas = []

# Loop para solicitar ao usuário que insira as notas
for i in range(4):
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)

# Mostrando as notas na tela
print("\nNotas digitadas:")
for i, nota in enumerate(notas):
    print(f"Nota {i}: {nota}")

# Calculando a média das notas
media = sum(notas) / len(notas)

# Mostrando a média na tela
print("\nMédia das notas:", media)
