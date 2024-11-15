from model.Animal import Animal

class Axolotl(Animal):
    '''
    This class represent an Axolotl and its attributes

    Properties:
        name: the name of the animal
        families: the families of the animal
        gender: the animal gender
        gills_nb: the number of gills of the animal
    '''

    def __init__(self, name, families, gender, gills_nb):
        super().__init__(name, families, gender)
        self.gills_nb = gills_nb
    
    def animal_information(self):
        '''
        Displays all information of the current animal
        '''
        print(f"name: {self.name}, species: {self.species}, gender: {self.gender}, number of gills: {self.gills_nb}")