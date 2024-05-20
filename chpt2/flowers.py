class Flower: 
    '''Represent A Flower Object'''

    def __init__(self, name: str, no_of_petals: int, price: float): 
        self._name = name
        self._no_of_petals = no_of_petals
        self._price = price

    def get_name(self) -> str:
        return self._name
    
    def get_no_of_petals(self) -> int:
        return self._no_of_petals 
    
    def get_price(self) -> float: 
        return self._price
    
    def set_name(self, name: str) : 
        self._name = name

    def set_no_of_petals(self, no: int): 
        self._no_of_petals = no

    def set_price(self, price: float): 
        self._price = price
        