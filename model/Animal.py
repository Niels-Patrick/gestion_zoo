class Animal:
    '''
    This class represents an animal and its attributes

    Properties:
        name: the name of the animal
        families: the families of the animal
        gender: the animal gender
    '''

    def __init__(self, name, families, gender):
        self.name = name
        self.species = families
        self.gender = gender

    def animal_information(self):
        '''
        Displays all basic information of the current animal
        '''
        print(f"name: {self.name}, species: {self.species}, gender: {self.gender}")
