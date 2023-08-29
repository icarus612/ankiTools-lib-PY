with open('./all-terms.txt', 'w') as t, open('./raw.txt', 'r') as u:	
  n = []
  f = []
  for i, line in enumerate(u.readlines()):
    match i % 3:
      case 2:
        n.append(f)
        f = []
        continue
    f.append(line.replace(':', ' ').strip())
	  
  t.writelines([' | '.join(i) + '\n' for i in n])