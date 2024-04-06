ev_numbers = []
with open("numbers.txt", "r") as src:
    even_numbers = [ev_numbers.append(line.strip()) for line in src if int(line.strip()) % 2 == 0]
    ev_numbers.sort()
    with open("even_numbers.txt", 'w') as dsn:
        for number in ev_numbers:
            dsn.write(str(number) + '\n')

print("List of even numbers created!")