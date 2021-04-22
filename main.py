import random  
import sys

j = int(sys.argv[2])

file = open(r'H:\projects\py\tokensys\hashes.fm', sys.argv[3])
if str(sys.argv[3]) == 'a':
    file.write('\n')
for i in range(0, j):
    hash = hex(random.getrandbits(int(sys.argv[1])))[2:]
    while (len(hash)/3).is_integer() is False:
       hash = hex(random.getrandbits(int(sys.argv[1])))[2:]
    spaced = '-'.join([hash[i:i+3] for i in range(0, len(hash), 3)])
    if j-i == 1:
        file.write(spaced)
    else:
        file.write(spaced + '\n')
    print(i+1)
file.close()
