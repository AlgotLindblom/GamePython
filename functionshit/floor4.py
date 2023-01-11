import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='', flush=True)
            time.sleep(speed)
        if nl:
            print('')

    def floor4(self):
        self.coolText('Du går upp för ännu en trappa', 0.02, True)
        self.coolText('Du kollar ut genom en springa i väggen och märker att du är väldigt högt upp', 0.02, True)
        self.coolText('Du möts av en mörk korridor. Det finns en dörr rakt fram och en till höger', 0.02, True)
        if input('Var vill du gå? (Fram/Höger) ').lower() != 'fram':
            self.coolText('Du går fram till dörren och drar i handtaget', 0.02, True)
            self.coolText('Dörren är låst och du väljer att gå till den andra dörren', 0.02, True)
            pass
        self.coolText('Du öppnar dörren', 0.02, True)
        #Fight

        self.coolText('Efter att du besegrat besten går du tillbaka ut i korridoren. Dörren som nu är till vänster om dig verkar stå på glänt.', 0.02, True)
        self.coolText('Du öppnar den och känner en bris av varm luft komma mot dig.', 0.02, True)
        self.coolText('Du börjar gå upp för trappan.', 0.02, True)
        # Kalla på våning 5 (bossfight)

t = Tower()
t.floor4()