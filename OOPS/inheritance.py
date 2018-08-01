class Rainbow():
    def __init__(self):
        print('Colours of Rainbow!')

    def colors(self, color):
        print(f'{color} is a color in the rainbow!')

class MyColor(Rainbow):     # class Mycolor inherits class Rainbow
    def __init__(self):
        Rainbow.__init__(self)    #__init__ methos is also inherited.
        print('MyColor created')

    def colors(self, color):    #overriding the colors method of the Rainbow class
        print(f'{color} is not a color in the rainbow!')
