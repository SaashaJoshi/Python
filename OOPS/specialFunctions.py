class Book():
  def __init__(self, name, author, pages):
    self.name=name
    self.author=author
    self.pages=pages
    
  def __str__(self):      # special method string     # str returns the string representations of objects
    return f'The author of {self.name} is {self.author}'
  
  def __len__(self):      # special method length     # len returns the length of the object
    return self.pages
  
  def __del__(self):    # special method delete
    print('A book has been deleted!')
