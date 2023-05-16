import time
from choices import choice
import os

print('loading...')
time.sleep(.2)

nome = input('hey, asshole, who are you?\n')
time.sleep(.2)
print(f"\n\33[34m{nome}\33[0m?! HAHAHAHAHAHA your mother hates you\n\
well, this don't care right now, take that sword\n")
time.sleep(.2)
print("you've won a \33[33mWooden Sword\33[0m\n")
time.sleep(.2)
print('Look, the super evil Villain is attacking the town')
time.sleep(.5)
if choice() == '3':
    time.sleep(.5)
    print('hey man, wake up\n')
    os.system('cls')
else:
    time.sleep(.5)
    print('hey man, wake up\n')
