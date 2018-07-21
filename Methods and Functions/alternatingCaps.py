def altCaps(string):
  newString=''
  for item, index in enumerate(string):   #uses enumerate function to get the item and its index in the string in the form of a tuple.
    if index%2==0:
      newString+=item.upper()   #uppercases the item at even index
    else:
      newString+=item.lower()   #lowercases the item at odd index
  print(newString)
