class goblin:
    def __init__(self,maxhealth,maxmana,stats=[]):
        self.maxhealth = maxhealth
        self.maxmana = maxmana
        self.STR = stats[0]
        self.DEX = stats[1]
        self.INT = stats[2]
        self.VIT = stats[3]
        self.currenthealth = self.maxhealth
   
    def reduceHP(self,damage):
        self.currenthealth = self.currenthealth - damage
        if self.currenthealth <= 0:
            die()

    def getPercentHP(self):
        return(self.currenthealth / self.maxhealth)
   
    def raiseHP(self,heal):
        self.currenthealth = self.currenthealth + heal
        if self.currenthealth + heal > self.maxhealth:
            self.currenthealth = self.maxhealth
        
    def die(self):
        print("ya died, kid")
        # drop loot to room
