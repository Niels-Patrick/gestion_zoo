import time
import os
import sys
from model.Zoo import Zoo
from controler import controler_zoo
from controler import controler_cage

sys.path.append(os.path.abspath("../model"))

def start():
    '''
    Starts the application with a welcome message, then creates a Zoo object and displays the zoo status
    '''
    print("Welcome to your zoo!")
    time.sleep(1)
    zoo = Zoo()
    main_menu(zoo)

def main_menu(zoo):
    '''
    Displays the main menu where the user can choose to manage the zoo or to manage the cages
    '''
    print("\n### Main Menu ###")
    print("1. Manage zoo")
    print("2. Manage cages")
    print("3. Animal list per cages")
    print("4. Exit")
    choice = input("Please select an option (enter the number):")

    match choice:
        case "1":
            controler_zoo.zoo_management(zoo)
        case "2":
            cage_list = zoo.get_cage_list()
            if len(cage_list) > 0:
                controler_cage.cages_management(zoo)
            else:
                print("There is currently no cages in the zoo.")
                time.sleep(1)
                main_menu(zoo)
        case "3":
            cage_list = zoo.get_cage_list()
            if len(cage_list) > 0:
                for cage in cage_list:
                    print(f"\nCage number {(cage_list.index(cage) + 1)}")
                    cage.display_animals()
                    time.sleep(1)
                main_menu(zoo)
            else:
                print("There is currently no cages in the zoo.")
                time.sleep(1)
                main_menu(zoo)
        case "4":
            print("Goodbye")
            time.sleep(1)
            exit()
        case _:
            print("Incorrect choice")
            main_menu(zoo)