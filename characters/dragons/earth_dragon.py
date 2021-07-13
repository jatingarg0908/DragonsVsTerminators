from .dragon import Dragon

class EarthDragon(Dragon):
    # ADD/OVERRIDE CLASS ATTRIBUTES HERE
    name='Earth'
    food_cost=4
    implemented=True
    def __init__(self,armor=4):
           super().__init__(armor)
    
