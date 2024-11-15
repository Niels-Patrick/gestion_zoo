from controler import controler
from controler import controler_animal
import time

def cages_management(zoo):
    '''
    Displays the cages management menu, where the user can see the current number of cages, select
    the cage they want to manage and choose to add a new animal in the chosen cage
    '''
    print("\n### Cages Management ###")
    zoo.display_cages_nb()
    cage_index = int(input('Please enter the number of the cage you want to manage:'))
    cage_list = zoo.get_cage_list()

    if (cage_index - 1) < 0 or (cage_index) > len(cage_list):
        print(f"The cage number {cage_index} does not exist.")
        time.sleep(1)
        cages_management(zoo)
        
    cage = cage_list[cage_index-1]
    cage.display_animals()

    time.sleep(1)
    add_animal(zoo, cage)

def add_animal(zoo, cage):
    response = input('\nDo you want to add another animal in the cage? (y/n)')
    if response == "y":
        cage.add_animal(controler_animal.create_animal())
        print("Animal successfully added to the cage.")
        time.sleep(1)
        add_animal(zoo, cage)
    elif response == "n":
        controler.main_menu(zoo)
    else:
        print("Incorrect answer")
        time.sleep(1)
        add_animal(zoo, cage)
