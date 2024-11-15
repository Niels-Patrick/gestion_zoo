class Cage:
    '''
    This class represents a cage containing several animals

    Properties:
        list_animals: a list containing all animals in the current cage

    Methods:
        
    '''

    def __init__(self):
        self.list_animals = []

    def add_animal(self, animal):
        '''
        Adds a new animal in the current cage

        Properties:
            animal: an Animal object
        '''
        self.list_animals.append(animal)

    def display_animals(self):
        '''
        Displays the name of all animals present in the current cage
        '''
        print("List of animals in the current cage:")
        for animal in self.list_animals:
            animal.animal_information()
