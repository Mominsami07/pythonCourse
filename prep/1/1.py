'''
Write a program that asks the user for three integers 0 <= a < b and k > 0.
The program prints out all integers a <= n <= b such that the sum of integers j satisfying the condition a <= j <= n is less than k.
Numbers should be written in one line separated by spaces.
'''

a = int(input("Enter a: "))
b = int(input("Enter b: "))
k = int(input("Enter k: "))

for n in range(a, b+1):
    if sum(range(a, n+1)) < k:
        print(n, end=" ")