'''
Write a program that asks the user for three integers 0 <= a < b and k > 0.
The program prints out all integers a <= n <= b such that the sum of integers j satisfying the condition a <= j <= n is less than k.
Numbers should be written in one line separated by spaces.
'''

initial_value = input("Initial value: ")
cumulative_value = int(initial_value)

while True:
    operations = input().split()
    if not operations:
        break

    for op in operations:
        symbol = op[0]
        number = int(op[1:])
        if symbol == "+":
            cumulative_value += number
        elif symbol == "*":
            cumulative_value *= number

print("Value:", cumulative_value)

