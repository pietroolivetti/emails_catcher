while True:
  txt = str(input('Incolla il testo >>> '))
  wtxt = txt.split()
  emails = ''
  l = []
  for i in wtxt:
    if len(i) > 6 and '@' in i:
      l.append(i)

  for i in l:
    if i != l[-1]:
      emails += f'{i} ; '
    else:
      emails += f'{i}'
  print(emails)
  cont = str(input('Vuoi continuare ["n" per uscire]: ')).strip().lower()
  if cont == 'n':
    break  