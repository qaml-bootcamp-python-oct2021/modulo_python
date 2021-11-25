
from enum import Enum

class PlayerRace(Enum):
    TERRAN = 1
    ZERG = 2
    PROTOSS = 3

    def get_info(self):
        return f'{self.value} - for {self.name}'



  

