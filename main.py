amount_of_numbers = input('Vvedite kol-vo chisel: ')
max = 0
i = 1
for i in range(0, int(amount_of_numbers)):
    i + 1
    number = int(input('Vvedite chislo: '))
    if number > max and number % 5 == 0:
        max = number
print(max)
