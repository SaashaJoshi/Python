def rList(text):
  newList=text.split()      #converts string to list
  newList.reverse()         #reverses the items in list
  print(''.join(newList))   #concatenates the items in list to form a string
