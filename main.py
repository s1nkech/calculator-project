# Калькулятор
import math
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
def power(a, b):
    """Возведение в степень"""
    if b < 0:
        return "Ошибка: отрицательная степень не поддерживается"
    return a ** b

def square_root(a):
    """Квадратный корень"""
    if a < 0:
        return "Ошибка: корень из отрицательного числа"
    return math.sqrt(a)

def main():
    print("Расширенный калькулятор")
    print("Операции: +, -, *, /, ^ (степень), sqrt (корень)")
    
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию: ")
        
        if op != "sqrt":
            b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка ввода")
        return
    
    if op == '+':
        print(f"Результат: {add(a, b)}")
    elif op == '-':
        print(f"Результат: {subtract(a, b)}")
    elif op == '*':
        print(f"Результат: {multiply(a, b)}")
    elif op == '/':
        print(f"Результат: {divide(a, b)}")
    elif op == '^':
        print(f"Результат: {power(a, b)}")
    elif op == 'sqrt':
        print(f"Результат: {square_root(a)}")
    else:
        print("Неизвестная операция")

if __name__ == "__main__":
    main()