from model.Animal import Animal

class Platypus(Animal):
    '''
    This class represent a Platypus and its attributes

    Properties:
        name: the name of the animal
        families: the families of the animal
        gender: the animal gender
        beak_length: the length of the animal's beak
    '''

    def __init__(self, name, families, gender, beak_length):
        super().__init__(name, families, gender)
        self.beak_length = beak_length
    
    def animal_information(self):
        '''
        Displays all information of the current animal
        '''
        print(f"name: {self.name}, species: {self.species}, gender: {self.gender}, beak length: {self.beak_length} mm")
