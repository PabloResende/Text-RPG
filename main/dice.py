import random



def D20_dice():
    for i in range(20):
        random_number = random.randint(1, 20)
        return random_number
    print(random_number)

def D6_dice():
    for i in range(6):
        random_number = random.randint(1, 6)
        return random_number