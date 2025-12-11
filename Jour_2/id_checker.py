class Id:
    def __init__(self, id_string=None):
        self.identifier = id_string if id_string is not None else ""
        self.validation = None
    
    def set_id(self, id_string):
        self.identifier = id_string
    
    def get_id(self):
        return self.identifier
    
    def to_int(self):
        return int(self.get_id())
    
    def print_id(self):
        print(self.get_id())

    def get_validation(self):
        return self.validation
    
    def is_valid(self): #méthode de la partie 1 de l’énigme
        if len(self.identifier)%2 != 0:
            self.validation = True
        else:
            if self.identifier[0: len(self.identifier)//2] == self.identifier[len(self.identifier)//2: len(self.identifier)]:
                self.validation = False
            else:
                self.validation = True
        return self.validation

class Id2(Id): # solution par chatgpt
    def is_valid(self):
        def is_periodic_string(s: str) -> bool:
            """Test optimal de périodicité."""
            return s in (s + s)[1:-1]
        s = self.identifier
        self.validation = not is_periodic_string(s)
        return self.validation

class Id_Sequence:
    def __init__(self, seq=None):
        self.id_tab = [] if seq is None else Id_Sequence.expand_id_sequence(seq)

    @staticmethod
    def expand_id_sequence(seq):
        first_id = seq.split('-')[0]
        last_id = seq.split('-')[1]
        id_tab = []
        for i in range(int(first_id),int(last_id)+1):
            id_tab.append(Id2(str(i)))
        return id_tab

    def id_validator(self):
        for id in self.id_tab:
            id.is_valid()

class Solver:
    def __init__(self, acc=None):
        self.acc = acc if acc is not None else 0
        self.line = ""
        self.sequences_t = []

    def input_importer(self):
        with open("input.txt", "r") as f:
            self.line = f.read()
            
    def sequences_expander(self):
        seqs_str_t = self.line.split(',')
        for seq in seqs_str_t:
            self.sequences_t.append(Id_Sequence(seq))
    
    def id_validator(self):
        for seq in self.sequences_t :
            seq.id_validator()

    def code_calculator(self):
        for seq in self.sequences_t:
            for id in seq.id_tab:
                if id.get_validation() == False:
                    self.acc = self.acc + id.to_int()
        return self.acc
