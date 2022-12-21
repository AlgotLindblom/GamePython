import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='')
            time.sleep(speed)
        if nl:
            print('')

    def floor2(self):
        self.coolText('Du går upp för den mörka trappan. Dina steg ekar i det tomma tornet.', 0.02, True)
        self.coolText('Framför dig ser du en korridor med två vägar', 0.02, True)
        if input('Vill du gå åt höger eller vänster? ').lower() != "Höger":
            self.coolText('Du rycker i dörren men den är låst. Du testar dörren åt vänster istället. ', 0.05, True)
        self.coolText('Handtaget är löst. Du öppnar dörren och ett rum lyses upp av din fackla.', 0.02, True)
        # Kalla på pusselfunktion
 
        self.coolText('Med ditt svärd i hand går du ut i korridoren igen. Du försöker öppna dörren till höger.', 0.02, True)
        self.coolText('Dörren öppnar sig den här gången.', 0.02, True)
        # Kalla på våning 3

T = Tower()
T.floor2()
