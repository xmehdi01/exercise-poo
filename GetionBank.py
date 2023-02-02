class GestionB:
    def __init__(self, ncompte, nomclient, ns):
        self.ncompte = ncompte
        self.nomclient = nomclient
        self.ns = ns
    def Versement(self,v):
        self.ns = self.ns + (v)
        return self.ns
    def Retrait(self,r):
        if r<=self.ns :
            self.ns = self.ns - (r)
            return self.ns
        else:
            self.ns = ("Solde insuffisant")
    def afficher(self):
        print("Le numero de compte est :", self.ncompte)
        print("Le nom de client est :", self.nomclient)
        print("Le solde est :", self.ns)
g1 = GestionB("5133131331","Simohamed",5000)
g1.Versement(300)
g1.Retrait(1000)
g1.afficher()