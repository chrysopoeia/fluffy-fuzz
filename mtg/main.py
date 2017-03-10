cards = [
    {
        'name': 'counterspell',
        'mana_cost': 'uu',
        'sets': [('limited edition alpha', 'uncommon'),('limited edition beta', 'uncommon')],
        'types': ['instant'],
    },
]


class Module(object):
    pass

class Filter(Module):
    pass

class Sleever(Module):
    pass

class Cleaner(Module):
    pass


base_filter = []
pile = [None]*10


while pile:
    print pile.pop()
