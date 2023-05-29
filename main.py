def primo(numero):
    if numero <= 1:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Digite um número inteiro: "))

if n <= 0:
    print("Número inválido")
else:
    primos = 0
    numero = 2
    while primos < n:
        if primo(numero):
            print(numero)
            primos += 1
        numero += 1
