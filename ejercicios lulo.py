# pasar un int a un float

num1 = 20
num2 = 30.5

num1 = num1 + num2

print(type(num1))
print(type(num2))

# ahora de manera explicita

num1 = 5.8
print(num1)
print (type(num1))

num2 = int(num1)
print(num2)
print(type(num2))
#ejemplo

edad = input("dime tu edad:")
print(type(edad))
edad = int(edad)
nueva_edad = 1 + edad

#ejemplo de sumar dos numeros uno float y un int convirtiendo uno en float

num1 = 7.5
num2 = 10
print(float(num1) + float(num2 ))