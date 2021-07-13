from .scuba_thrower import ScubaThrower
from utils import terminators_win
from.dragon import Dragon

class DragonKing(ScubaThrower):  # You should change this line
    # END 4.3
    """The King of the colony. The game is over if a terminator enters his place."""

    name = 'King'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.3
    implemented = True  # Change to True to view in the GUI
    food_cost=7
    # END 4.3
    def __init__(self, armor=1):
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        super().__init__(armor)
        self.real_one=False
        if DragonKing.instantiated is False:
                self.real_one=True
                DragonKing.instantiated=True
        # END 4.3

    def action(self, colony):
        """A dragon king throws a stone, but also doubles the damage of dragons
        in his tunnel.
         
        Impostor kings do only one thing: reduce their own armor to 0.
        """
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
        if self.real_one is False:
            self.reduce_armor(self.armor)
        else:
            super().action(colony)
            x=self.place.exit
            while x is not None:
                if x.dragon is not None:
                   if x.dragon.is_doubled is False:
                      x.dragon.damage=2*x.dragon.damage
                      x.dragon.is_doubled=True
                   if x.dragon.is_container:
                        if x.dragon.contained_dragon is not None and x.dragon.contained_dragon.is_doubled is False:
                           x.dragon.contained_dragon.damage=2*x.dragon.contained_dragon.damage
                           x.dragon.contained_dragon.is_doubled=True
                x=x.exit
            
       
        # END 4.3

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and if the True DragonKing has no armor
        remaining, signal the end of the game. 
        """
        self.armor-=amount
        if self.armor<=0:
             self.place.remove_fighter(self)
             self.death_callback()
             if self.real_one is True:
                terminators_win()
        # BEGIN 4.3
        "*** YOUR CODE HERE ***"
