
n = int(input("Enter the number of elements: "))
sum = 0

for i in range(n):
    num = int(input(f"Enter number {i+1}: "))
    if num % 2 == 0:
        sum += num

print(f"Sum of even numbers: {sum}")