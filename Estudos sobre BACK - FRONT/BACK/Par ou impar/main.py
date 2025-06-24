x = input("digite um numero: ")

while not x.isdigit():
    print("Entrada inválida. Por favor, digite um número inteiro.")
    x = input("digite um numero: ")
    
x = int(x)
if x % 2 == 0:
    print("\n O número inserido é par")
else:
    print("\n O número inserido é impar")