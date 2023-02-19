
def merge(current, new, override=True, current_field=0, new_field=0):
  new_deck = []
  for card in current:
    if new_field is not False:
      item = card[current_field] in [x[new_field] for x in new]
      new_deck.push()
    else:
       item = filter(lambda x: card[current_field] in x, new)
       if len(item) > 0: new_deck.push(item[0])