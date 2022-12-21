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
        self.coolText('Du möts av en mörk korridor. Det finns en dörr rakt fram och en till vänster', 0.02, True)
        if input('Var vill du gå? (Fram/Vänster) ') != 'Fram'.lower():
            self.coolText('Du går fram till dörren och drar i handtaget', 0.02, True)
            self.coolText('Dörren är låst och du väljer att gå till den andra dörren', 0.02, True)
            pass
        self.coolText('Du öppnar dörren')

t = Tower()
t.floor4()