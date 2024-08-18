def lista_vazia(lista):
    """Retorna True se a lista estiver vazia, caso contrário, retorna False."""
    return len(lista) == 0

def maior_valor(lista):
    """Retorna o maior valor da lista. Retorna -1 se a lista estiver vazia."""
    if lista_vazia(lista):
        return -1
    return max(lista)

def menor_valor(lista):
    """Retorna o menor valor da lista. Retorna -1 se a lista estiver vazia."""
    if lista_vazia(lista):
        return -1
    return min(lista)

def valor_medio(lista):
    """Retorna o valor médio da lista. Retorna -1 se a lista estiver vazia."""
    if lista_vazia(lista):
        return -1
    return sum(lista) / len(lista)

# Testa as funções com uma lista vazia e uma lista com alguns elementos

# Lista vazia
lista_vazia_test = []

# Lista com alguns elementos
lista_com_elementos = [10, 20, 5, 15, 30]

# Teste com lista vazia
print("Testando lista vazia:")
print("A lista está vazia:", lista_vazia(lista_vazia_test))  # Esperado: True
print("Maior valor na lista vazia:", maior_valor(lista_vazia_test))  # Esperado: -1
print("Menor valor na lista vazia:", menor_valor(lista_vazia_test))  # Esperado: -1
print("Valor médio da lista vazia:", valor_medio(lista_vazia_test))  # Esperado: -1

# Teste com lista com elementos
print("\nTestando lista com elementos:")
print("A lista está vazia:", lista_vazia(lista_com_elementos))  # Esperado: False
print("Maior valor na lista com elementos:", maior_valor(lista_com_elementos))  # Esperado: 30
print("Menor valor na lista com elementos:", menor_valor(lista_com_elementos))  # Esperado: 5
print("Valor médio da lista com elementos:", valor_medio(lista_com_elementos))  # Esperado: 16.0
