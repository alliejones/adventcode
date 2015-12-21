literal_total = 0
mem_total = 0

with open('ex08-input.txt') as file:
    for line in file:
        line = line.strip('\n')
        literal_total += len(line)
        mem_total += len(eval(line))

print literal_total - mem_total
