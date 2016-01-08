from __future__ import division                       #Thanks to bgusach from Stackexchange for a better division alternative
import random
import time
class GamePlayer:

    population = []
    casual_population = []
    fgc_players = []
    graveyard = []

    def __init__(self):
        self.like = False
        self.played = False
        self.casual_population.append(self)
        self.population.append(self)
        self.recommend = False
    def local_tourney(self):
        self.casual_population.remove(self)
        self.fgc_players.append(self)

    def tick(self):
        if self.played:
            if self in self.casual_population:
                liketoss=random.randint(1,2)
                loctoss=random.randint(1,5)
                if loctoss>3:
                    self.local_tourney()
                if liketoss==1:
                    self.like = True
                else:
                        if self in self.casual_population:
                            self.casual_population.remove(self)
                            self.graveyard.append(self)

            if self.like==True:
                rectoss=random.randint(1,10)
                if rectoss>7:
                    self.recommend=True

        if self.recommend:
            nfriends = 1
            if len(self.casual_population) > nfriends:
                friends=random.sample(self.casual_population,nfriends)
            else:
                friends = self.casual_population[:]
            for f in friends:
                f.played=True


def make_players (n):
    fgc=GamePlayer()
    fgc.played=True
    for q in range (n-1):
        GamePlayer()
    
def run_simulation (fgc_players,ticks):
    make_players(fgc_players)
    for t in range(ticks):
        print len (GamePlayer.casual_population)
        for p in GamePlayer.population:
            p.tick()
def mr_wizard ():
    Melee="This game is going places; it will be featured at a future major tournament!"
    Injustice="This game isn't going to make it, the community just can't keep it alive long enough."
    Soul_Calibur="It's a fun game and all, but no one is going to any tournaments for it; It has nowhere else to go."
    if len(GamePlayer.fgc_players)/ len(GamePlayer.casual_population) >1:
        print Melee
    elif len(GamePlayer.casual_population)/ len(GamePlayer.population) >0.4:
        print Soul_Calibur
    else:
        print Injustice

run_simulation(50,10)
def results():
    time.sleep(4)
    if len (GamePlayer.graveyard)==1:
        print "player went back to playing Street Fighter"
    else:
        print len (GamePlayer.graveyard), "players went back to playing Street Fighter."
    time.sleep(4)
    if len (GamePlayer.casual_population)==1:
        print "player didn't really contribute much to the community."
    else:
        print len (GamePlayer.casual_population), "players didn't really contribute much."
    time.sleep(4)
    if len (GamePlayer.fgc_players)==1:
        print len (GamePlayer.fgc_players),"player is growing the game's meta and expanding its community."
    else:
        print len (GamePlayer.fgc_players),"players are growing the game's meta and expanding its community."
    time.sleep(3)
results()
mr_wizard()
