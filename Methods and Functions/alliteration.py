def allit(text):
  list=text.split()     #converts string to a list  #can even use text.lower().split()
  if list[0][0].lower()==list[1][0].lower():      #compares the first letter of the different items in the list created
    return True
  else:
    return False
  
