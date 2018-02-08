# coding: utf-8
print("PARES E IMPARES")
num1 = int(input("Escriba un número entero: "))
num2 = int(input(f"Escriba un número entero mayor o igual que {numero_1}: "))

while num2 < num1:
    print(f"¡Le he pedido un número entero mayor o igual que {numero_1}!")
else:
    for i in range(num1, num2 + 1):
        while i % 2 == 0:
            print(f"El número {i} es par")
        else:
            print(f"El número {i} es impar")
