import check_input.py

class pokemon:
    def __init__(self, name, p_type):
        self._name = name
        self._poke_type = p_type
        self._battle_table = [[1, .5, 2], [2, 1, .5],[.5, 2, 1]]
        self._hp = 25
    
    @property
    def get_hp(self):
        return self._hp

    #returns str 
    def get_normal_menu(self):
        return f""
    
    #returns str
    def _normal_move(self, opponent, move):
        result = ""
        choice = check_input.get_int_range(1,2)
        if(c= 1):

        else:

    #return str
    def _slam(self, opponent):

    #return str
    def _tackle():
        return result

    #return str
    @abstractmethod
    def get_special_menu():
        return result
        
    #returns str
    @abstractmethod
    def get_special_move(self, opponent, move):
        return result

    #return str
    def attack(self, opponent, type, move):
        return result


    #return void
    def _take_damage(self, dmg):

    #return str
    def __str__(self):
        return " "
