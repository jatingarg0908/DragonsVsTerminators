from .thrower_dragon import ThrowerDragon


class LaserDragon(ThrowerDragon):
    # This class is optional. Only one test is provided for this class.

    name = 'Laser'
    # OVERRIDE CLASS ATTRIBUTES HERE
    # BEGIN 4.5
    implemented = True  # Change to True to view in the GUI
    food_cost=10
    damage=2
    fighters_shot=0
    # END 4.5

    def __init__(self, armor=1):
        ThrowerDragon.__init__(self, armor)
        self.fighters_shot = 0

    def fighters_in_front(self, skynet):
        # BEGIN 4.5
        dic={}
        current_place=self.place
        dist=0
        while current_place !="skynet" and current_place!=None:
            if current_place.dragon!=None :
                x=current_place.dragon
                y=dist
                if x!=self:
                    dic.update({x:y})
            if len(current_place.terminators)!=0:
                for j in current_place.terminators:
                    dic.update({j:dist})
            current_place=current_place.entrance
            dist+=1
            
        return dic
        # END 4.5

    def calculate_damage(self, distance):
        # BEGIN 4.5
        x=distance*0.2+self.fighters_shot*0.05
        return self.damage-x
        # END 4.5

    def action(self, colony):
        fighters_and_distances = self.fighters_in_front(colony.skynet)
        for fighter, distance in fighters_and_distances.items():
            damage = self.calculate_damage(distance)
            fighter.reduce_armor(damage)
            if damage:
                self.fighters_shot += 1
