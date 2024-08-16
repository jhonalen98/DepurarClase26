# def es_primo(n):

#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# numero = 29
# print(f"¿El número {numero} es primo? {es_primo(numero)}")

def es_primo(n):

    if n <= 1:
        return False
    maximo=int(n**0.5)
    for i in range(2, maximo+1):
        if n % i == 0:
            return False
    return True

numero = int(input("Introduzca el numero a verificar: "))
print(f"¿El número {numero} es primo? {es_primo(numero)}")