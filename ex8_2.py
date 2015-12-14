literal_length = 0
escaped_length = 0

with open('8-input.txt') as file:
    for line in file:
        literal_length += len(line)
        escaped_length += \
            2 + len(line.replace('\\', "\\\\").replace('"', '\\\"'))


print escaped_length - literal_length
