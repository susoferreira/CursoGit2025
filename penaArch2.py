print("Hello Suso from penaArch2")

def resta(a, b):
    return a - b

print(resta(10, 5))

def multiplica(a, b):
    return a * b

print(multiplica(10, 5))

def divide(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

print(divide(10, 2))

print(divide(10, 0))

def saludo(nombre):
    return "Hola " + nombre

print(saludo("Suso"))

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))
print(factorial(0))
print(factorial(1))

def fibonacci(n):
    if n <= 0:
        return "Input should be a positive integer"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
print(fibonacci(10))
print(fibonacci(1))