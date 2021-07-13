from .dragon import Dragon


class FireDragon(Dragon):
    """FireDragon cooks any Terminator in its Place when it expires."""

    name = 'Fire'
    food_cost=5
    damage = 3
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 2.2
    implemented = True  # Change to True to view in the GUI

    # END 2.2

    def __init__(self, armor=3):
        """Create a Dragon with a ARMOR quantity."""
        Dragon.__init__(self, armor)

    def reduce_armor(self, amount):
        """Reduce armor by AMOUNT, and remove the FireDragon from its place if it
        has no armor remaining.

        Make sure to damage each terminator in the current place, and apply the bonus
        if the fire dragon dies.
        """
    def reduce_armor(self,amount):
        self.armor=self.armor-amount
        x=self.place.terminators.copy()
        for j in x:
             j.reduce_armor(amount)
        xx=self.place.terminators.copy()
        if self.armor<=0:
               for k in xx:
                  k.reduce_armor(self.damage)
               y=self.place
               y.remove_fighter(self)
               self.death_callback()
        # BEGIN 2.2
        
        "*** YOUR CODE HERE ***"
