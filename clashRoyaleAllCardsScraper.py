from bs4 import BeautifulSoup
import requests

cardNames = ['Three Musketeers', 'Golem', 'Royal Recruits', 'Lava Hound', 'P.E.K.K.A', 'Mega Knight', 'Electro Giant', 'Sparky', 'Giant Skeleton', 'Goblin Giant', 'Royal Giant', 'Elite Barbarians', 'Archer Queen', 'Ram Rider', 'Balloon', 'Witch', 'Prince', 'Bowler', 'Executioner', 'Cannon Cart', 'Electro Dragon', 'Giant', 'Royal Hogs', 'Wizard', 'Barbarians', 'Minion Horde', 'Rascals', 'Skeleton King', 'Golden Knight', 'Mighty Miner', 'Lumberjack', 'Inferno Dragon', 'Electro Giant', 'Night Witch', 'Magic Archer', 'Mother Witch', 'Baby Dragon', 'Dark Prince', 'Hunter', 'Valkyrie', 'Musketeer', 'Mini P.E.K.K.A', 'Hog Rider', 'Battle Ram', 'Zappies', 'Flying Machine', 'Battle Healer', 'Skeleton Dragons', 'Ice Wizard', 'Princess', 'Miner', 'Bandit', 'Royal Ghost', 'Fisherman', 'Skeleton Army', 'Guards', 'Mega Minion', 'Dart Goblin', 'Elixir Golem', 'Knight', 'Archers', 'Minions', 'Goblin Gang', 'Skeleton Barrel', 'Firecracker', 'Wall Breakers', 'Ice Golem', 'Goblins', 'Bomber', 'Spear Goblins', 'Bats', 'Skeletons', 'Ice Spirit', 'Fire Spirit', 'Electro Spirit', 'Barbarian Hut', 'X-Bow', 'Elixir Collector', 'Goblin Hut', 'Inferno Tower', 'Goblin Drill', 'Bomb Tower', 'Furnace', 'Goblin Cage', 'Mortar', 'Tesla', 'Tombstone', 'Cannon', 'Lightning', 'Rocket', 'Graveyard', 'Freeze', 'Poison', 'Fireball', 'Goblin Barrel', 'Tornado', 'Clone', 'Earthquake', 'Arrows', 'Royal Delivery', 'The Log', 'Rage', 'Barbarian Barrel', 'Zap', 'Giant Snowball', 'Mirror', 'Heal Spirit']
allCards = {'Three Musketeers': {}, 'Golem': {'Golemite (On Death)': {}}, 'Royal Recruits': {}, 'Lava Hound': {'Lava Pups (On Death)': {}}, 'P.E.K.K.A': {}, 'Mega Knight': {}, 'Electro Giant': {}, 'Sparky': {}, 'Giant Skeleton': {'Bomb (On Death)':{}}, 'Goblin Giant': {'Giant': {}, 'Spear Goblin': {}}, 'Royal Giant': {}, 'Elite Barbarians': {}, 'Archer Queen': {}, 'Ram Rider': {'Hog Rider': {}, 'Rider': {}}, 'Balloon': {'Bomb (On Death)': {}}, 'Witch': {'Skeleton': {}}, 'Prince': {}, 'Bowler': {}, 'Executioner': {}, 'Cannon Cart': {'Cannon Cart (On Death)': {}}, 'Electro Dragon': {}, 'Giant': {}, 'Royal Hogs': {}, 'Wizard': {}, 'Barbarians': {}, 'Minion Horde': {}, 'Rascals': {'Rascal Boy': {}, 'Rascal Girl': {}}, 'Skeleton King': {}, 'Golden Knight': {}, 'Mighty Miner': {}, 'Lumberjack': {'Rage Barbarian': {}}, 'Inferno Dragon': {}, 'Electro Giant': {}, 'Night Witch': {'Bat': {}}, 'Magic Archer': {}, 'Mother Witch': {}, 'Baby Dragon': {}, 'Dark Prince': {}, 'Hunter': {}, 'Valkyrie': {}, 'Musketeer': {}, 'Mini P.E.K.K.A': {}, 'Hog Rider': {}, 'Battle Ram': {'Barbarian (On Death)': {}}, 'Zappies': {}, 'Flying Machine': {}, 'Battle Healer': {}, 'Skeleton Dragons': {}, 'Ice Wizard': {'Spawn IceWizardCold': {}}, 'Princess': {}, 'Miner': {}, 'Bandit': {}, 'Royal Ghost': {}, 'Fisherman': {}, 'Skeleton Army': {}, 'Guards': {}, 'Mega Minion': {}, 'Dart Goblin': {}, 'Elixir Golem': {'Elixir Golemite (On Death)': {}}, 'Knight': {}, 'Archers': {}, 'Minions': {}, 'Goblin Gang': {'Goblin': {}, 'Spear Goblin': {}}, 'Skeleton Barrel': {'Balloon': {}, 'Skeleton Barrel (On Death)': {}}, 'Firecracker': {}, 'Wall Breakers': {}, 'Ice Golem': {}, 'Goblins': {}, 'Bomber': {}, 'Spear Goblins': {}, 'Bats': {}, 'Skeletons': {}, 'Ice Spirit': {}, 'Fire Spirit': {}, 'Electro Spirit': {}, 'Barbarian Hut': {'Barbarian': {}, 'Barbarian (On Death)': {}}, 'X-Bow': {}, 'Elixir Collector': {}, 'Goblin Hut': {'Spear Goblin': {}, 'Spear Goblin (On Death)': {}}, 'Inferno Tower': {}, 'Goblin Drill': {}, 'Bomb Tower': {'Bomb (On Death)': {}}, 'Furnace': {'Fire Spirit': {}, 'Fire Spirit (On Death)': {}}, 'Goblin Cage': {'Goblin Brawler (On Death)': {}}, 'Mortar': {}, 'Tesla': {}, 'Tombstone': {'Skeleton': {}, 'Skeleton (On Death)': {}}, 'Cannon': {}, 'Lightning': {}, 'Rocket': {}, 'Graveyard': {'Skeleton': {}}, 'Freeze': {}, 'Poison': {}, 'Fireball': {}, 'Goblin Barrel': {}, 'Tornado': {}, 'Clone': {}, 'Earthquake': {}, 'Arrows': {}, 'Royal Delivery': {}, 'The Log': {}, 'Rage': {}, 'Barbarian Barrel': {}, 'Zap': {}, 'Giant Snowball': {}, 'Mirror': {}, 'Heal Spirit': {}}



for card in cardNames:
    print(card)
    cardURL = card.replace(' ', '+')
    url = 'https://statsroyale.com/card/' + cardURL

    response = requests.get(url, timeout=120)
    soup = BeautifulSoup(response.content, "html.parser")

    group = soup.find(attrs={'class': 'card__headerContentWrapper'}) # box containing description and table(s) of info
    for square in group.findAll(attrs={'class': 'card__metrics'}): # each seperate table has class name card__metrics
        header = square.find(attrs={'class': 'ui__mediumText card__metricsHeader'})
        if header == None:
            for div in square.findAll('div', recursive=False): # finds all divs which have keys and values, recursive so it only looks on parent div
                content = div.find('div')
                pairs = []
                for thing in content.findAll('div'):
                    pairs.append(thing.text.strip())
                pairs = list(filter(None, pairs)) # filters blanks
                allCards[card][pairs[0]] = pairs[1]  # add to dictionary 
        elif header.text.strip() == card: 
            divBox = square.findAll('div', recursive=False) # finds all divs which have keys and values, recursive so it only looks on parent div
            divIter = iter(divBox) # turn to iterable
            next(divIter) # skip first div since it is just the header
            for div in divIter:
                content = div.find('div')
                pairs = []
                for thing in content.findAll('div'):
                    pairs.append(thing.text.strip())
                pairs = list(filter(None, pairs)) # filters blanks
                allCards[card][pairs[0]] = pairs[1]  # add to dictionary 
        else:
            divBox = square.findAll('div', recursive=False) # finds all divs which have keys and values, recursive so it only looks on parent div
            divIter = iter(divBox) # turn to iterable
            next(divIter) # skip first div since it is just the header
            sub = square.find(attrs={'class': 'ui__mediumText card__metricsHeader'}).text.strip() # finds header to use in dictionary assignment
            for div in divIter:
                content = div.find('div')
                pairs = []
                for thing in content.findAll('div'):
                    pairs.append(thing.text.strip())
                pairs = list(filter(None, pairs)) # filters blanks
                allCards[card][sub][pairs[0]] = pairs[1]  # add to dictionary
    
print(allCards)
