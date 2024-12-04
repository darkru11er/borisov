def slo(a, b):
    return a + b

def vich(a, b):
    return a - b

def umn(a, b):
    return a * b

def delen(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def cifra(prompt):
    while True:
        value = input(prompt)
        if value.strip() == "":
            print("Ошибка: введена пустая строка пожалуйста введите число.")
        else:
            try:
                return float(value)
            except ValueError:
                print("Ошибка: введено некорректное значение пожалуйста введите число")

def main():
    a = cifra("Введите первое число: ")
    b = cifra("Введите второе число: ")

    print("Сложение:", slo(a, b))
    print("Вычитание:", vich(a, b))
    print("Умножение:", umn(a, b))

    res = delen(a, b)
    if res == "Ошибка: деление на ноль":
        print(res)
    else:
        print("Деление:", res)

main()



