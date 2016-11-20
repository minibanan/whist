class wgame(object):
    
    def __init__(self, bid, tricksByTeam):
        self.bid = bid
        self.tricksByTeam = tricksByTeam
    
    def score(self, scorePerTrick, scoreMultiplier):
        return scorePerTrick * scoreMultiplier
    
    
    def description(self):
        print "Took %i tricks at a bid of %s for a score of %i" % (self.tricksByTeam, self.bid, self.score(110, 4))


#game = wgame("9 vip", 8)
#game.description()
