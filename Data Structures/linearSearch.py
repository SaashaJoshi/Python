numlist=input('Enter the list: ')
numlist=numlist.split(',')
target=input('Enter the element to be searched: ')

for position, element in enumerate(numlist):
    if element==target:
        print(f'Element found at position : {position}')
        break
else:
    print('Element not found!')
