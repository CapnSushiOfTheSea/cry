from time import sleep
from random import randint

def cryAbout(thing):
    thingYelled = thing.upper()
    tears = 1
    print(f'WAAHHHH WAHHHH!! {thingYelled}!!!!! (1 tear)')
    try:
        crying = True
        while crying:
            sniffles = randint(0,5)
            if sniffles == 3:
                print('*sniff*')
                sleep(.2)
            else:
                tears += 1
                print(f'WAAHHHH WAHHHH ({tears} tears)')
                sleep(.2)
    except KeyboardInterrupt:
        print('No')

cryAbout('something')
