amount = input('Vvedite kol-vo chisel: ')
max = 0
i = 1
for i in range(0, int(amount)):
    i + 1
    number = int(input('Vvedite chislo: '))
    if number > max and number % 5 == 0:
        max = number
print(max)

# Напишите программу, которая в последовательности натуральных чисел определяет максимальное число, кратное 5. Программа
# получает на вход количество чисел в последовательности, а затем сами числа. В последовательности всегда имеется число,
# кратное 5. Количество чисел не превышает 1000. Введенные числа не превышают 30 000. Программа должна вывести одно
# числo максимальное число, кратное 5.
