"""
This is the lab1 classes
"""
class Battery:

    def __init__(self) -> None:
        print("Kiva Robot Components")
"""
This will provide power to the bot
"""
def SupplyPower(self, watts):
        print("Supply Power to robot")

"""
This will make the screw go up and down
"""
class LiftingMechanism:
    def __init__(self,ScrewHeight, ScrewMaterial) -> None:
        self._screwheight = ScrewHeight #Should be private
        self._screwmaterial = ScrewMaterial #Should be private
        
    def Unscrew(self):
        print("Go Up")
    
    def Screw(self):
        print("Go Down")
"""
Subclass of liftinning mechanism
"""
class HeightControl(LiftingMechanism):
    def __init__(self, ScrewHeight, ScrewMaterial) -> None:
         super().__init__(ScrewHeight, ScrewMaterial)
         self._Height = 5

    def SetHeight(self, Centimiters):
        print("Set Height to {Centimiters} centimiters")
        self._Height = Centimiters
