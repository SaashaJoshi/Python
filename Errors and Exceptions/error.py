def func():
  while True:
    try:
      numb=int(input('Please enter a number: '))
    except:
      print('An error occured!')
      continue
    else:
      break
    
  print(f'The square of number is: {numb**2}')
  
