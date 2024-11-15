from model.Axolotl import Axolotl
from model.Owl import Owl
from model.Platypus import Platypus
from model.Animal import Animal
import os
import sys
import time

sys.path.append(os.path.abspath("../model"))

def create_animal():
    '''
    Displays the animal creation menu, where the user can choose to create an Axolotl, an Owl, a
    Platypus or another animal

    Return: an Axolotl, an Owl, a Platypus or another animal object
    '''
    print("\n### Animal Adoption ###")
    print("1. Axolotl")
    print("2. Owl")
    print("3. Platypus")
    print("4. Other")
    choice = input("Please choose an animal to adopt:")

    match choice:
        case "1":
            return create_axolotl()
        case "2":
            return create_owl()
        case "3":
            return create_platypus()
        case "4":
            return create_other_animal()
        case _:
            print("Incorrect choice")
            time.sleep(1)
            return create_animal()
        
def create_axolotl():
    '''
    Runs the Axolotl creation process

    Return:
        an Axolotl object with the properties specified during the creation process
    '''
    name = input("Please enter a name for your newly adopted Axolotl:")
    families = "Ambystomatidae"
    gender_choice = ""

    while gender_choice != "m" or gender_choice != "f":
        gender_choice = input("Please choose the Axolotl gender (m/f):")
        if gender_choice == "m":
            gender = "male"
            break
        elif gender_choice == "f":
            gender = "female"
            break
        else:
            print("Incorrect answer")
            time.sleep(1)
            
    gills_nb = input("Please enter the number of gills of your newly adopted Axolotl:")

    return Axolotl(name, families, gender, gills_nb)

def create_owl():
    '''
    Runs the Owl creation process

    Return:
        an Owl object with the properties specified during the creation process
    '''
    name = input("Please enter a name for your newly adopted Owl:")
    families = "Strigidae"
    gender_choice = ""

    while gender_choice != "m" or gender_choice != "f":
        gender_choice = input("Please choose the Axolotl gender (m/f):")
        if gender_choice == "m":
            gender = "male"
            break
        elif gender_choice == "f":
            gender = "female"
            break
        else:
            print("Incorrect answer")
            time.sleep(1)
            
    plumage_colour = input("Please enter the plumage colour of your newly adopted Owl:")

    return Owl(name, families, gender, plumage_colour)

def create_platypus():
    '''
    Runs the Platypus creation process

    Return:
        a Platypus object with the properties specified during the creation process
    '''
    name = input("Please enter a name for your newly adopted Platypus:")
    families = "Ornithorhynchidae"
    gender_choice = ""

    while gender_choice != "m" or gender_choice != "f":
        gender_choice = input("Please choose the Axolotl gender (m/f):")
        if gender_choice == "m":
            gender = "male"
            break
        elif gender_choice == "f":
            gender = "female"
            break
        else:
            print("Incorrect answer")
            time.sleep(1)
            
    beak_length = input("Please enter the beak length of your newly adopted Platypus (in mm):")

    return Platypus(name, families, gender, beak_length)

def create_other_animal():
    '''
    Runs the animal creation process

    Return:
        an Animal object with the properties specified during the creation process
    '''
    name = input("Please enter a name for your newly adopted animal:")
    families = input("Please enter the animal families:")
    gender_choice = ""

    while gender_choice != "m" or gender_choice != "f":
        gender_choice = input("Please choose the Axolotl gender (m/f):")
        if gender_choice == "m":
            gender = "male"
            break
        elif gender_choice == "f":
            gender = "female"
            break
        else:
            print("Incorrect answer")
            time.sleep(1)

    return Animal(name, families, gender)
