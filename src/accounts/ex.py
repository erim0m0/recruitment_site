import random
import sys
print(random.randint(111111, 999999))

b = ['a', 'b']
print(sys.getsizeof(b))
if (a := len(b)) < 10:
    print(f'len of b is {a}')
