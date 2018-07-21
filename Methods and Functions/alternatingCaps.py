def altCaps(string):
  newString=''
  for item, index in enumerate(string):
    if index%2==0:
      newString+=item.upper()
    else:
      newString+=item.lower()
  print(newString)
