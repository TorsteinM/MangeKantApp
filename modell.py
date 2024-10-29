class Mangekant:
    """Baseklasse for mangekanter: 
        Bruk trekant, rektangel eller kvadrat for å lage objekter
        Alle klassene skal implementere:
        .areal():   regner ut arealet
        .omkrets(): regner ut omkretsen
        """
    def __init__(self):
        pass
class Kvadrat(Mangekant):
    def __init__(self, side):
        self.side = side
class Rektangel(Mangekant):
    def __init__(self, lengde, bredde):
        self.lengde = lengde
        self.bredde = bredde


        
