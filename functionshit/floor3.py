import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='', flush=True)
            time.sleep(speed)
        if nl:
            print('')
    
    def floor3(self):
        self.coolText('Du känner en kall bris över din rygg när du går upp för trappan', 0.02, True)
        self.coolText('Månens ljus slinkras igenom i den trasig torn väggen och lyser upp rummet framför dig', 0.02, True)
        self.coolText('Till vänster ser du en dörr med texten *VARNING* och till höger är en tillsynes vanlig dörr', 0.02, True)
        self.coolText("Du kan gå till höger till den vanliga dörren eller till vänster till dörren med varnings skylten?", 0.02, True)
        if input('> ') != "höger":
            self.coolText('Dörren knakar och långsamt uppenbarar sig rummet därbakom framför dina ögon', 0.02, True)
            self.coolText("Framför dig ser du ett ganska mörkt rum ", 0.02, True)
            pass
        self.coolText('Dörren öppnas och du ser ett tomt rum framför dig', 0.02, True)
        self.coolText('Längst in syns ännu en dörr, du försöker öppna den men den är låst', 0.02, True)
        self.coolText('Du återvänder till korridoren och försöker öppna den andra dörren', 0.02, True)
        # Kalla på slå slå funktion

        self.coolText('Du besegrade besten och har nu fått en nyckel. Du återvänder ut i korridoren.', 0.02, True)
        self.coolText('Du återvänder in i rummet med den låsta dörren. Dina steg ekar mot marken....', 0.02, True)
        if input('Vill du öppna dörren? ') != "Ja".lower():
            self.coolText('Du går tillbaka ut i korridoren', 0.02, True)
            self.coolText('Efter att ha sökt igenom våningen märker du att det inte finns något mer att göra.', 0.02, True)
            self.coolText('Du återvänder till dörren och stoppar nyckeln i dörren.', 0.02, True)
            pass

        # Kalla på våning 4
        
t = Tower()
t.floor3()

