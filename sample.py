import time
import sys

def _print(string):
    sys.stdout.write(string + '\r')
    sys.stdout.flush()

_print('hello')
time.sleep(2)
_print('world')
