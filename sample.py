import time
from multiplexer import Multiplexer

with Multiplexer() as mp:
    for i in range(7):
        print(i)
        mp.SelectChannel(i)
        time.sleep(2)

