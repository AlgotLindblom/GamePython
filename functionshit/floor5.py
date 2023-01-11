import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='', flush=True)
            time.sleep(speed)
        if nl:
            print('')

    def floor5(self):
        self.coolText('Du känner en skum lukt ju högre upp i trappan du kommer.', 0.02, True)
        self.coolText('Ett högt flåsande hörs och du börjar känna dig nervös.', 0.02, True)
        self.coolText('Ur skuggorna kommer en grovt överviktig, illaluktande Goblin.', 0.02, True)
        #Battle
