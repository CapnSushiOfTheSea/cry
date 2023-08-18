from time import sleep
from random import randint, choice

userInput = input('What to cry about? (Leaving it blank will pick a random choice) ')

thingsToCryAbout = [
    'taxes',
    'debt',
    'i made the npc sad',
    'idk what im crying about but wahhh'
]

def cryAbout(thing):
    if thing == '':
        thing = choice(thingsToCryAbout)
    thingYelled = thing.upper()
    tears = 1
    print(f'WAAHHHH WAHHHH!! {thingYelled}!!!!! (1 tear)')
    sleep(.5)
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

cryAbout(userInput)
