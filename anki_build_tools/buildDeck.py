
def build_deck(name, cards, delimiter='|'):
		name = name + '.txt' if not name.endswith('.txt') else name
		with open(name, 'w') as f:
				for card in cards:
						f.write(f' {delimiter} '.join(card) + '\n')

def build_decks(items, delimiter='|'):
		for name, cards in items.items():
				build_deck(name, cards, delimiter)