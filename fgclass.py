import random
class GamePlayer:

    population = []
    Casual_Population = []
    fgc_players = []
    graveyard = []

    def __init__(self):
        self.like = False
        self.played = False
        self.Casual_Population.append(self)
        self.population.append(self)
        self.recommend = False # recommending to people
    def local_tourney(self):
        self.Casual_Population.remove(self)
        self.fgc_players.append(self)
#    def injustice (self):
#        self.Casual_Population.remove(self)
#        self.graveyard.append(self)
    def tick(self):
        if self.played:
            if self in self.Casual_Population:
                self.local_tourney()
            self.like = True
            if self.like==True:
                self.recommend=True
        if self.recommend:
            nfriends = 1
            if len(self.Casual_Population) > nfriends:
                friends=random.sample(self.Casual_Population,nfriends)
            else:
                friends = self.Casual_Population[:]
            for f in friends:
                f.played=True
#       You can add this line when you want to add the random. As of now 3:44, thursday, it is set to auto like the game: toss=random.randint(1,2)
#if toss==1:
#self.like=True
#if toss==2: self.like=False

# I dont need this(?)   def create_FGC_Players (self):        
# I don't need this(?)  self.played=True

def make_players (n):
    fgc=GamePlayer()
    fgc.played=True
    for q in range (n-1):
        GamePlayer()
    
def run_simulation (fgc_players,ticks):
    make_players(fgc_players)
    for t in range(ticks):
        print len (GamePlayer.Casual_Population)
        for p in GamePlayer.population:
            p.tick()
            

run_simulation(50,10)


print len (GamePlayer.fgc_players),"is the number of people advancing the meta."
print len (GamePlayer.Casual_Population), "is the number of total players."
