sum = 0
amount = int(input('Vvedite kol-vo chisel: '))
for i in range(0,amount):
    number = int(input('Vvedite chislo: '))
    if number % 6 == 0:
        sum = sum + number
print(sum)

#Напишите программу, которая в последовательности натуральных чисел определяет сумму чисел, кратных 6. Программа
#получает на вход количество чисел в последовательности, а затем сами числа. В последовательности всегда имеется число,
#кратное 6. Количество чисел не превышает 100. Введенные числа не превышают 300. Программа должна вывести одно число
#сумму чисел, кратных 6.
