import random

class SlotMachine:
    def __init__(self, reelNum, winDict):
        self.reels = [(i for i in range(10))] * reelNum
        self.wins = winDict
    
    def spin(self):
        spinResult = ''
        for reel in self.reels:
            spinResult += str(random.choice(reel))
        return spinResult
    
slot1 = SlotMachine(3, {'777': 50})

print(slot1.spin())

# Kinda broke, don't work