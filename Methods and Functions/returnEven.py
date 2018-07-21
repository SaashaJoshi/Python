def rEven(*args):     #function takes arbitrary number of arguments
  list=[]
  for item in args:
    if item%2==0:   
      list.append(item)   #append even items to the empty list
  print(list)
  
  
