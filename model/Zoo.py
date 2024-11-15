class Zoo:
    '''
    This class allows the management of cages in the zoo

    Properties:
        list_cage: a list containing all cages in the zoo

    Methods:
        display_cages_nb(): displays the current number of cages in the zoo
        add_cage(cage): adds a new cage to the cage list
    '''

    def __init__(self):
        self.list_cage = []

    def display_cages_nb(self):
        '''
        Displays the current number of cages in the zoo
        '''
        print(f"There are actually {len(self.list_cage)} cages in the zoo.")

    def add_cage(self, cage):
        '''
        Adds a new cage to the cage list

        Properties:
            cage: a Cage object
        '''
        self.list_cage.append(cage)

    def get_cage_list(self):
        '''
        Getter on list_cage

        Return:
            list_cage: a list of all cages in the zoo
        '''
        return self.list_cage
