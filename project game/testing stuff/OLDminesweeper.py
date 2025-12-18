import random
#lets make a customisable grid and a custom amount of bombs
class Grid () :
    def __init__(self , gridSize , bomb):
        # set grid size capped at 26
        self.gridSize = gridSize
        self.maxGridSize = 26
        if gridSize > 26 :
            self.gridSize = gridSize

        # set number of bombs
        bombP = bomb/ 100
        self.bombT = (gridSize**2) * bombP
        # make dictionary of grid
        gridLetter = [chr(x) for x in range(97 , gridSize+97)]
        gridNumber = [x for x in range(1 , gridSize+1)]
        self.coords = {str(letter)+str(num): 0 for letter in gridLetter for num in gridNumber} 
        #make bombs in the grid
        arr = []
        while len(arr) < self.bombT :
            randLetter = random.choice(gridLetter)
            randNumber = random.choice(gridNumber)
            if [randLetter , randNumber] not in arr :
                arr.append(str(randLetter)+str(randNumber))
        self.arrB = arr # !!!!
        for value in arr :
            self.coords[value] = "BOMB"

        ## adding 1 to squares that have a bomb next to it
        for cord, value in self.coords.items() :
            if value == "BOMB" :
                if  1< cord[1] and cord[1] < gridSize :
                    if self.coord[cord[0]+ [int(cord[0])-1]] != "BOMB" :
                        self.coords += 1
                    






g = Grid (5, 20) 
print(g.coords)

