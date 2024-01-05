import time
import sys

'60 sec timer'
v= time.time()+60

while v > time.time():
    sys.set_int_max_str_digits(0)
    f=9999
    print(f**f)
    f+=9999

