with open("numbers.txt", 'r') as file:
    numbers = [int(line.strip()) for line in file]

numbers.sort(reverse=True)

for number in numbers[:3]:
    print(number)
