from dice import D20_dice, D6_dice
from enemy import slime_life, slime_attack
from player import player_damage
import os

def choice_1():
    enemy_life =  slime_life
    player_life = 100
    player_defense = 2

    while enemy_life > 0:
        player_choice = input('what you do? \n\
        [1]Fight [2]Bag [3]Run')

        if player_choice == '3':
            print('HAHAHA gay?')
            break

        if player_choice == '1':

            if D20_dice() in range(1,2):
                print('\33[33mMISS\33[0m')

            if D6_dice() in range(1):
                print('\33[33mMISS\33[0m')

            if D20_dice() in range(3,15):
                print('BOOM')
                enemy_life -= player_damage
                print(f'the life of the enemy is {enemy_life}')

            if D6_dice() in range(2,5):
                print('POW')
                player_life -= slime_attack + player_defense
                print(f"player life is {player_life}")

            if D20_dice() in range(16,20):
                print('\33[31mCRITICAL\33[0m' )
                enemy_life -= 5 - player_damage
                print(f'the life of the enemy is {enemy_life}')

            if D6_dice() in range(5):
                print('\33[31mCRITICAL\33[0m' )
                player_life -= slime_attack + player_defense - 5
                print(f"player life is {player_life}")


        if player_life == 0:
            # os.system('cls')
            print('\33[31mYOU DIE\33')
            break

        if enemy_life >= 0:
            # os.system('cls')
            print('\33[33mEnemy is defeated!\33[0m')
            print(f'players life is {player_life}')
            break
