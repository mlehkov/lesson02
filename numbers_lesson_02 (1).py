import math

# Функція print() для виведення на екран.
print("Hello World!")
print("The", "quick", "brown", "fox")  # кілька аргументів
print("The", 1, True)  # кілька типів даних

# Функція input() для отримання вводу від користувача
# age = input("Введіть ваш вік: ")
age = str(34)
print("Ваш вік", age, "роки.")
print(f"Ваш вік {age} роки.") # в фігурних дужках ми візьмемо значення змінної


# Тип даних змінної
print("Type of variable", age, type(age))  # <class 'str'>
age = int(age)
print("Type of variable", age, type(age))  # <class 'int'>
age = float(age)
print("Type of variable", age, type(age))  # <class 'int'>
age = str(age)
print("Type of variable", age, type(age))  # <class 'int'>
