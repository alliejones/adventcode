def get_seqs(line):
    prev_c = line[0]
    count = 0
    result = []

    for c in line:
        if c == prev_c:
            count += 1
        else:
            result += [ count, prev_c ]
            count = 1
            prev_c = c

    result += [ count, prev_c ]

    return ''.join(map(str, result))

result = '3113322113'
for i in range(50):
    result = get_seqs(result)

print len(result)
