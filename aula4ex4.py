def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# Exemplo de uso:
lista = [1, 5, 10, 3, 8]
maior_numero = find_largest(lista)
print("O maior número na lista é:", maior_numero)
