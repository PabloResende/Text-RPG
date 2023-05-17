from enemy import slime_life
import pandas as pd

#rpg class
#[1][1] for defense
#[1][0] for damage
barbarian = [
['barbarian_damage', 'barbarian_defense'],
[4, 3]]

mage = [
['mage_damage', 'mage_defense'],
[5, 2]]

knight = [
['knight_damage', 'knight_defense'],
[3, 4]]

bag =[
    ['wooden_sword_damage', 2],[ 'wooden_sword_price', 10],
    [],[]
]


#Character sheet:

base_player_life = '100'
player_class = "Mage"
player_damage = mage[1][0] + bag[0][1]


def player_attack():
    sum_damage =  slime_life - player_damage
    print(sum_damage)
    # return player_damage

#bag:

def show_bag():
    bag= [
        {'name':'wooden_sword','price': 10, 'quantidade':1},
        {'name':'iron_sword','price': 10, 'quantidade':0},
        {'name':'healing potion','price': 10, 'quantidade':1},
        ]
    table = pd.DataFrame(bag)
    return print(table)