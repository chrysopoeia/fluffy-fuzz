db = [{
    'name': 'counterspell',
    'mana_cost': 'uu',
    'sets': [('limited edition alpha', 'uncommon'),('limited edition beta', 'uncommon')],
    'types': ['instant'],
}]


class Urza(object):
    def identify(self, card_image):
        # AI wizard thingo
        card_details = card_image
        
        return card_details


class InputTray(object):
    def __init__(self):
        self.physical_pile = []
    
    def physical_load(self, *card):
        self.physical_pile.extend(card)
        
    def next(self):
        return self.physical_pile.pop(0)


class Scanner(object):
    def scan(self, physical_card):
        # scan the card face for an image
        image = physical_card
        
        return image


class Filter(object):
    pass


class MTGO(object):
    def lookup(self, card_details):
        # online lookup
        current_card = card_details
        
        return current_card


urza = Urza()
mtgo = MTGO()

input_tray = InputTray()

input_tray.physical_load(241,24,21,5,4,3,46,57,45)
input_tray.physical_load(223,23421,213465,2346,43,623)

scanner = Scanner()


while input_tray.physical_pile:
    next_card = input_tray.next()
    
    image = scanner.scan(next_card)
    card_details = urza.identify(image)
    current_card = mtgo.lookup(card_details)
    
    # apply filters
    
    print current_card
