def start():
    welcome = input("Välkommen till tornet. Ditt mål är att ta dig till toppen. Är du ny till spelet? (Ja/Nej) ")
    if welcome == ("Ja").lower():
        print("För att gå kan du välja att gå Framåt ('F'), Bakåt ('B'), Höger ('H') eller Vänster ('V')")
        print("Det kommer stå i varje prompt vad du har för alternativ, så du behöver inte oroa dig vart du kan gå!")
    elif welcome == ("Nej").lower():
        pass

    print(f'''

    888
    888
    888                                           888
    888888 .d88b.  888 8888  888 88888    .d88b.  888 
    888   d88""88b 88888  88 88888   888 d8P  Y8b 888888
    888   888  888 888       888     888 88888888 888
    Y88b. Y88..88P 888       888     888 PY8b.    Y88b.
     "Y888 "Y88P   888       888     888   "Y8888  "Y888

               uuuuu
               |_#-|
               | _#|
               |_ -|
___.$$.________| - |____
  .#$$$. __    |-  |
  $$$$$$    ` -[__N]
  $$$$$$    -.
   `:/'    _.))
    ||  .'.-'
    '" /  (
      .    `.
      .      `--..
''')

start()