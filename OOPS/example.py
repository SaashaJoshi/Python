class Line():
    def __init__(self, coord1, coord2):
        self.coord1=coord1
        self.coord2=coord2

    def distance(self):
        x1,y1=self.coord1
        x2,y2=self.coord2
        return ((x2-x1)**2+(y2-y1)**2)**0.5

    def slope(self):
        x1, y1 = self.coord1
        x2, y2 = self.coord2
        return (y2-y1)/(x2-x1)
