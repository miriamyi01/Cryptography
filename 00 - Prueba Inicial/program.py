import fileinput

lines = []
for line in fileinput.input():
    lines.append(line)

total = 0.0
for line in lines:
    number = float(line)
    if number.is_integer():
        number = int(number)
    total += number

if total.is_integer():
    total = int(total)

print(total)