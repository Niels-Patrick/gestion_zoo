from model.Cage import Cage
import os
import sys
from controler import controler
import time

sys.path.append(os.path.abspath("../model"))

def zoo_management(zoo):
    '''
    Displays the zoo management menu, where the user can see the current number of cages and can
    choose to add a new cage
    '''
    print("\n### Zoo Management ###")
    zoo.display_cages_nb()
    response = input('Do you want to add another cage? (y/n)')

    if response == "y":
        cage = Cage()
        zoo.add_cage(cage)
        print("A new cage has been added to your zoo.")
        time.sleep(1)
        zoo_management(zoo)
    elif response == "n":
        controler.main_menu(zoo)
    else:
        print("Incorrect answer")
        time.sleep(1)
        zoo_management(zoo)