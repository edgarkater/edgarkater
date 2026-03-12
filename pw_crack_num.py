from check_pw import *
reset_zahl()
for zahl in range(10000):
    if check(zahl):
        if zahl<10:
            print("000",zahl)
        elif zahl<100:
            print("00",zahl)
        elif zahl<1000:
            print("0",zahl)
        else:
            print(zahl)
        break