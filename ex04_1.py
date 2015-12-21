import hashlib

key = 'iwrupvqb'
n = 0

found = False
while not found:
    n += 1
    hash = hashlib.md5()
    hash.update(key+str(n))
    if hash.hexdigest().startswith('00000'):
        found = True

print n
