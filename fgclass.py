import random
class Game:

    population = []
    fgc_players = []
    graveyard = []

    def __init__(self):
        self.played = False
        self.population.append(self)
        self.reccomend = False
    def local(self):
        if self.played==True:
            self.population.remove(self)
            self.fgc_players.append(self)
    def sax(self):
        self.population.remove(self)
        self.fgc_players.append(self)
            
    def injustice (self):
        self.population.remove(self)
        self.graveyard.append(self)
    def death_tick(self):
        warner=0
        if warner==0:
            for i in range (300):
                self.injustice()
                print graveyard
    def tick(self):
        if self.played:
            self.reccomend = True
        if self.played:
           toss=random.randint(1,2)
           if toss==1:
               self.sax()
           if toss==2:
                self.played=False
                self.reccomend=False
        if len(self,population)>5:
            friends=random.sample(self.population,5)
        else:
            friends=self.population[:]
        for friend in friends:
            if friend.reccomend:
                self.sax=True
def create_FGC_Players (self):
    GIMR = Game()
    GIMR.played=True

def run_simulation (population,ticks):
    create_players(population)
    for t in range(ticks):
        for p in Game.population:
            p.tick()

run_simulation(500,3)
