# coding: utf-8
print("PARES E IMPARES")
num1 = int("Escriba un número entero: ")
num2 = int("Escriba un número entero mayor o igual que el primero: ")

while num2 < num1:
    print "Le he pedido un número entero mayor o igual!!!!!!!!!"
else:
    for i in range(num1, num2 + 1):
        while i % 2 == 0:
            print "El número es par"
        else:
            print "El número es impar"
