def square(num):
  return num**2

myList=[1,2,3,4,5]

for item in map(square, myList):    #map function applies the function (mentioned as the first argument) to the iterable (mentioned as the second argument)
  print(item)
  
#or
print(list(map(square, myList)))
