from model.Animal import Animal

class Owl(Animal):
    '''
    This class represent an Owl and its attributes

    Properties:
        name: the name of the animal
        families: the families of the animal
        gender: the animal gender
        plumage_colour: the colour of the animal plumage
    '''

    def __init__(self, name, families, gender, plumage_colour):
        super().__init__(name, families, gender)
        self.plumage_colour = plumage_colour
    
    def animal_information(self):
        '''
        Displays all information of the current animal
        '''
        print(f"name: {self.name}, species: {self.species}, gender: {self.gender}, plumage colour: {self.plumage_colour}")