

import sys
dct_1 = {'рука': 'hand'}
dct_2 = {k: v for i in sys.stdin.readlines() for k, v in [i.split()]}

dct_1.update(dct_2)

print(dct_1)

