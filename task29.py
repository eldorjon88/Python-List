numbers = []

print("10 ta son kiriting:")

for _ in range(10):
    num = int(input())
    numbers.append(num)

unique_numbers = []

for n in numbers:
    if numbers.count(n) == 1:
        unique_numbers.append(n)

print("Noyob elementlar.", unique_numbers)
