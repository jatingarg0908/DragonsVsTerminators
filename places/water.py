from . import Place


class Water(Place):
    """Water is a place that can only hold watersafe fighters."""

    def add_fighter(self, fighter):
        """Add a Fighter to this place. If the fighter is not watersafe, reduce
        its armor to 0."""
        # BEGIN 4.1
        super().add_fighter(fighter)
        if fighter.is_watersafe is False:
               fighter.reduce_armor(fighter.armor)
        "*** YOUR CODE HERE ***"
