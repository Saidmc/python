import string as s
from random import *


ch1 = s.ascii_letters
ch2 = s.digits
ch3 = s.punctuation

ch = ch1 + ch2 + ch3

password = ''.join(choice(ch) for j in range(randint(8,16)))

print('\n')
print(password, end = '\n\n')


