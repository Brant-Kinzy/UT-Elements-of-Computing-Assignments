# Brant Kinzy
# Elements of Computing HW1
# 9/14/2025
# Professor: Amrita Kaur

# Excercise 1
name = input('What is your name? ')
print(f'Hello {name}! You have just delved into Python.')
print()

# Excercise 2
temp_C = input('Enter a tempature in degrees Celsius: ')
print(f'{temp_C} Celsius is {round((float(temp_C) * (9/5) + 32), 2)} Fahrenheit.')
print()

# Excercise 3
user_input = input('Enter the bill and the gratuity rate: ')
bill, gratuity = user_input.split(',')
bill = float(bill)
gratuity = (float(gratuity))/100
grat_dol_amt = round((bill * gratuity), 2)
total = (bill + grat_dol_amt)
print(f'The gratuity is ${grat_dol_amt} and the total is ${total}.')
print()

# Excercise 4
num = input('Enter a number between 0 and 999: ')
num = int(num)
num1s = num % 10 # find the 1's place
num = num // 10
num10s = num % 10 # find 10's place
num = num // 10
num100s = num % 10
total = (num1s + num10s + num100s)
print(f'The sum of the digits is {total}.')
print()

# Excercise 4
p = float(input('Enter your investment amount ($): '))
r = 0.07
n = input('Enter your investment length (years): ')
n = int(n)
a = p * (1 + r) ** n
print(f'After {n} years, you will have ${round(a, 2)}.')
print()

# Excercise 5
age = int(input('Enter your age: '))
max_HR = 220 - age
ideal_HR_A = 0.5 * max_HR
ideal_HR_B = 0.85 * max_HR
print(f'Your target heart rate is {round(ideal_HR_A)} - {round(ideal_HR_B)} bpm.')
