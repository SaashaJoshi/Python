numlist=input('Enter the list: ')
numlist=numlist.split(',')
index=int(input('enter the index position: '))

def delete(list, index):
    del list[index]
    print(list)

delete(numlist, index)
