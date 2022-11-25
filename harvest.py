############# Part 1   #############

class MelonType:
    """A species of melon at a melon farm."""

    def __init__(
        self, code, first_harvest, color, is_seedless, is_bestseller, name
    ):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing) # append is not making a new list it is updating the old one 
       # print(f'We are printing:{self.pairings}')


    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code=new_code
        # print(f'We are updating code value  to the new {self.code}')

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType( 
            code ="musk",
            name= "Muskmelon",
            first_harvest= 1998,
            color= "green",
            is_seedless=True,
            is_bestseller=True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)
    
    cas = MelonType(
            code ="cas",
            name= "Casaba",
            first_harvest= 2003,
            color= "2003",
            is_seedless=False,
            is_bestseller=False)
    cas.add_pairing("mint")
    cas.add_pairing("strawberries")
    all_melon_types.append(cas)
    
    yw = MelonType(
            code ="yw",
            name= "Yellow Watermelon",
            first_harvest= 2013,
            color= "yellow",
            is_seedless=False,
            is_bestseller=True)
    yw.add_pairing("ice cream")
    all_melon_types.append(yw)
    
    cren = MelonType(
            code ="cren",
            name= "Crenshow",
            first_harvest= 1996,
            color= "green",
            is_seedless=False,
            is_bestseller=False)
    cren.add_pairing("prosciutto")
    all_melon_types.append(cren)

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name}')
        for pairing in melon.pairings:
            print(f'-{pairing}')
        
def print_melon_pairing_info(melon_type): 
    ''' Helping to print a single type of melon'''

    for pairing in melon_type.pairings:
        print(f'{pairing}')    
    
def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_type_dict = {}

    for melon in melon_types:
        if melon.code  not in melon_type_dict:
            melon_type_dict[melon.code] = melon

    return melon_type_dict 

############# Part 2   #############

class Melon:
    """A melon in a melon harvest."""

    def __init__(
        self, type, shape, color, field, harvester):
        """Initialize a harvest."""

        self.type = type
        self.shape = shape
        self.color = color
        self.field = field
        self.harvester = harvester
    
    def is_sellable(self):
        '''Determine if melon can be sold or not '''

        if (self.shape > 5 and self.color > 5) and self.field != 3:
            return True
        else:
            return False    

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)

    melon_1 = Melon(melons_by_id["yw"], 8, 7, 2, "Sheila")
    melon_2 = Melon(melons_by_id["yw"], 3, 4, 2, "Sheila")
    melon_3 = Melon(melons_by_id["yw"], 9, 8, 3, "Sheila")
    melon_4 = Melon(melons_by_id["cas"], 10, 6, 35, "Sheila")
    melon_5 = Melon(melons_by_id["cren"], 8, 9, 35, "Michael")
    melon_6 = Melon(melons_by_id["cren"], 8, 2, 35, "Michael")
    melon_7 = Melon(melons_by_id["cren"], 2, 3, 4, "Michael")
    melon_8 = Melon(melons_by_id["musk"], 6, 7, 4, "Michael")
    melon_9 = Melon(melons_by_id["yw"], 7, 10, 3, "Sheila")

    melons = [
        melon_1,
        melon_2,
        melon_3,
        melon_4,
        melon_5,
        melon_6,
        melon_7,
        melon_8,
        melon_9,
    ]

    return melons

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""
    
    for melon in melons:
        harvester_name = f'Harvested by {melon.harvester}'
        field_num = f'Field #{melon.field}'
        if melon.is_sellable():
            sellable_status = "CAN BE SOLD"
        else:
            sellable_status ="NOT SELLABLE"    
        print(f'{harvester_name} from {field_num} {sellable_status}')
