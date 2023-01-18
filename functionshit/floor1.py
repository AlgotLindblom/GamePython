import time

class Tower:
    def coolText(self, text, speed, nl):
        for i in text:
            print(i, end='')
            time.sleep(speed)
        if nl:
            print('') #Den här funktionen används på alla plan. Gör att texten långsamt och snyggare kommer fram i terminalen.
    
    def floor1(self):
            self.coolText('''De uråldriga stendörrarna gnäller dovt när du forcerar dig in i TORNETS dunkel.''', 0.02, True)
            self.coolText('Innanför möts du av ett cirkulärt rum dekorerat av statyer av olika omänskliga varelser. Rummet verkar större på insidan än utsidan.', 0.02, True)
            input('>')
            self.coolText('Rakt framför dig är en bred trappa som smalnar till en brant spiral upp mot nästa våning', 0.02, True)
            if input('Gå mot trappan? Ja/Nej ').lower() != 'ja':
                self.coolText('Synd för dig...', 0.5, True)
            print('Du närmar dig ', end='')
            self.coolText('långsamt', 0.1, False)
            self.coolText(' trappans blanka steg.', 0.02, True)
            self.coolText('När du närmar dig trappans fot formas en märklig varelse från dimma.', 0.02, True)
            self.coolText('Varelsen verkar bestå helt av olika bägare och kokkärl. Du tittar dig kring och ser några liknande kärl här och där i rummet.', 0.02, True)
            self.coolText('"Vill du fortsätta måste du svara på min gåta." yttrar en skrovlig röst som verkar komma från den spökliknande högen disk.', 0.02, True)
            match input('Vill du höra gåtan?').lower():
                case 'ja':
            self.coolText('You see dark room at the top of the stairway. To your right is a sign that is unclear. ', 0.02, True)
            if input('You can look closer at the sign. What do you do? look/stay ').lower() != 'look':
                self.coolText(' You do not have any other choices. Looking at plack.... ')
            # Här kallar på gåt funktion.
    
T = Tower()
T.floor1()
        
