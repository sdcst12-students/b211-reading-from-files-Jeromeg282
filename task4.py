#!python3
# Advanced Dungeons and Dragons

"""
the file task04.txt contains a matrix of values
The row indicates the level of fighter. Row 1 is for a level 1 fighter, row 2 is for a level 2 fighter and so on

In each row, the numers indicate the target number needed out of 20 to land a hit on a specific Armor Class, starting with
10 on the left, followed by 9, then 8, all the way to -10 on the far right.

Create a function that reads the specific value for a specific level and an armor class, and prints the target number needed.

"""



class Stats:

    def __init__(self, filename):
        self.filename = filename
        self.data = self.loaddata()

    def loaddata(self):
        with open(self.filename, 'r') as file:
            lines=file.readlines()
            data = [list(map(int, line.split()))for line in lines]
        return data



    def target(self, lvl,ac):
        levelindex = lvl - 1
        acindex = 10 - ac
        targetnumber = self.data[levelindex][acindex]
    
        return targetnumber



def tests():
    filename = "task04.txt"
    stats = Stats(filename)
    assert stats.target(3,7) == 23
    assert stats.target(9,-1) == 17
    assert stats.target(13,-10) == 20

if __name__=="__main__":
    tests()