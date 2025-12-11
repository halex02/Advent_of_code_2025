class Dial:
    cursor = 50
    cpt = 0
    def __init__(self, cpt=None, cursor=None):
        if cursor is None:
            self.cursor = Dial.cursor
        else:
            self.cursor = cursor
        if cpt is None:
            self.cpt = Dial.cpt
        else:
            self.cpt = cpt
    
    def count_zero(self, verbose=False):
        if self.cursor == 0:
            self.cpt = self.cpt+1
            if verbose == True:
                self.print_counter()
        else:
            if verbose == True:
                self.print_counter()
    
    def get_counter(self):
        return self.cpt
    
    def print_counter(self):
        print("Valeur du compteur: "+str(self.get_counter()))
        
    def get_cursor(self):
        return self.cursor
        
    def print_cursor(self):
        print("Position du curseur: "+str(self.get_cursor()))
    
    def to_the_right(self, verbose=False, part_two = True):
        self.cursor = (self.cursor+1)%100
        if part_two == True:
            self.count_zero()
        if verbose == True:
            self.print_cursor()
    
    def to_the_left(self, verbose=False, part_two = True):
        self.cursor = (self.cursor-1)%100
        if part_two == True:
            self.count_zero()
        if verbose == True:
            self.print_cursor()
        
    def apply_rotation(self, rotation, part_two = True):
        rotation_value = int(rotation[1:])
        for i in range(rotation_value):
            if rotation[0] == 'L':
                self.to_the_left()
            else:
                self.to_the_right()
        if part_two == False:
            self.count_zero()
    
    def parse_rotations(self):
        with open("input.txt", "r") as f:
            for line in f:
                self.apply_rotation(line.strip())
