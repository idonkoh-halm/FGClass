import random
class GamePlayer:

    population = []
    fgc_players = []
    graveyard = []

    def __init__(self):
        self.played = False
        self.population.append(self)
        self.reccomend = False # recommending to people
    def local_tourney(self):
        self.population.remove(self)
        self.fgc_players.append(self)
#    def injustice (self):
#        self.population.remove(self)
#        self.graveyard.append(self)
    def tick(self):
        if self.played:
            self.reccomend = True
        if self.played:  #Now add the infection methods
            self.local_tourney()
            #toss=random.randint(1,2)
            #if toss==1:
            #   self.sax()
            #if toss==2:
            #    self.played=False
            #    self.reccomend=False

            #friends=self.population[:]
            #for friend in friends:
            #    if friend.reccomend:
            #        self.sax=True
        #if self.played:
        #    self.local()
    def create_FGC_Players (self):        
        self.played=True

def make_players (n):
    fgc=GamePlayer()
    fgc.played=True
    for q in range (n-1):
        GamePlayer()
    
def run_simulation (population,ticks):
    make_players(population)
    for t in range(ticks):
        print len (GamePlayer.population)
        for p in GamePlayer.population:
            p.tick()
            

run_simulation(50,10)

for i in range (10):
    GamePlayer()
print len (GamePlayer.fgc_players),"is the number of people advancing the meta."
print len (GamePlayer.population), "is the number of total players."
