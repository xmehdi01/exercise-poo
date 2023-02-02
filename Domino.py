class Domino():
    def __init__(self,co1,co2):
        self.cote1 = co1
        self.cote2 = co2
    def affichePoint(self):
        print("Les points de cotes 1 est ",self.cote1)
        print("Les points de cotes 1 est ",self.cote2)
    def somePoint(self):
        m = self.cote1+self.cote2
        print(m)
ca1 = Domino(4,5)
(ca1.affichePoint())
(ca1.somePoint())