particles = []

def get_el(el, idx=0):
  return el.split('|')[idx].strip()

for i in range(1, 11):
  with open(f'./created-decks/jp101-core-{i}00.txt') as deck:
    particles.append(set(el for el in deck.readlines()))

for idx, deck in enumerate(particles):
  r = []
  for i, x in enumerate(particles):
    if i != idx:
      r.extend([get_el(e) for e in x])
  itr = set(get_el(card) for card in deck).intersection(r)
  print([(get_el(card, 1), get_el(card, 2)) for card in deck if get_el(card) in r])

