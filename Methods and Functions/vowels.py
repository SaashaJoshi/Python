def vowels(text):
  order=['a','e', 'i', 'o', 'u', 'x']     #checks if aeiou occur in the given order in the string
  for char in text:
    if char==order[0]:
      order.pop(0)      #or use order.remove(char)
  if len(order)==1:   #is true when all the vowels are found in the given order in the string
    print('Yes, vowels occur in the given order!')
