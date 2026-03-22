# Калькулятор
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

def main():
    print("Простой калькулятор")
    print("Операции: +, -, *, /")
    
    try:
        a = float(input("Введите первое число: "))
        op = input("Введите операцию (+, -, *, /): ")
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
    else:
        print("Неизвестная операция")

if __name__ == "__main__":
    main()