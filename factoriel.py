class Weapon:
    def __init__(self, ammunition: int, range: int,):
        self._ammunition=ammunition
        self._range=range
    def fire_at(self, x: int, y: int, z= int):
        
