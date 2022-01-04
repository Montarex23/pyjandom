from time import time_ns

class Random():
    def __init__(self, seed=None):
        self.multiplier = 25214903917
        self.addend = 11
        self.mask = (1 << 48) -1

        if seed != None:
            self.seed = self.initialScramble(seed)
        else:
            self.seed = (8682522807148012 * time_ns()) & self.mask

    def initialScramble(self, seed):
        return (seed ^ self.multiplier) & self.mask

    def twos_comp(self, val, bits):
        if (val & (1 << (bits - 1))) != 0:
            val = val - (1 << bits)
        return val
    
    def next(self, bits):
        seed = self.seed
        oldseed = seed
        nextseed = (oldseed * self.multiplier + self.addend) & self.mask
        while seed != oldseed:
            nextseed = (oldseed * self.multiplier + self.addend) & self.mask
        if bits % 8 == 0:
            return self.twos_comp(nextseed >> (48 - bits), bits)
        else:
            return nextseed >> (48 - bits)

    def nextInt(self, bound=None):
        if bound == None:
            return self.next(32)
        if bound <= 0:
            raise "Bound can't be zero or less"
        r = self.next(31)
        m = bound - 1
        if (bound & m) == 0:
            r = ((bound * r) >> 31)
        else:
            r = r % bound
        return r

    def nextLong(self): # HALF WORKING
        return (self.next(32) << 32) + self.next(32)

    def nextBoolean(self):
        return (self.next(1) != 0)

    def nextFloat(self): # without 2s completion / longer than java
        return self.next(24) / (1 << 24)
