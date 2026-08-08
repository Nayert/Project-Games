import random
from copy import deepcopy
from cell import Cell


class Grid:
    def __init__(self, width, height, dimension):
        self.width = width
        self.height = height
        self.dimension = dimension

    def makeGrid(self, contents):
        self.gridArray = [[deepcopy(contents) for _ in range(self.width)]
                          for _ in range(self.height)]
        return self.gridArray

    # def saveGrid(self):
    #     with open("textfile.txt", "w") as file:
    #         file.write(str(self.gridArray))

    def strToList(self, text):
        if text == "":
            return 0, 0, 0, []

        gridHeight = gridWidth = gridDimension = checkNext = count = bombCount = 0
        text = text[1:-1]

        while True:
            try:
                if checkNext:
                    checkNext = False
                    if text[count] == "[":
                        gridHeight += 1

                if text[count] == "[":
                    checkNext = True
                    bombCount += 1

                if text[count] in "[], ":
                    text = text[:count] + text[count + 1:]
                else:
                    count += 1
            except IndexError:
                break

        gridWidth = bombCount // (gridHeight + 1)
        gridDimension = len(text) // (gridWidth * gridHeight)

        parsedArray = [[[text[index + row + depth] for index in range(gridDimension)]
                        for row in range(gridWidth)]
                        for depth in range(gridHeight)]

        return gridHeight, gridWidth, gridDimension, parsedArray

    def getFileSave(self):
        with open("textfile.txt", "r") as file:
            self.height, self.width, self.dimension, self.gridArray = self.strToList(file.read())

    def setDimension(self, values):
        self.dimension = len(values)
        self.gridArray = [[Cell(False, 0, False) for _ in range(self.width)] for _ in range(self.height)]

    def setWidth(self, num):
        self.width = num
        self.gridArray = [[[0 for _ in range(self.dimension)]
                           for _ in range(self.width)]
                          for _ in range(self.height)]

    def setHeight(self, num):
        self.height = num
        self.gridArray = [[[0 for _ in range(self.dimension)]
                           for _ in range(self.width)]
                          for _ in range(self.height)]

    def getSurroundingSqrs(self, x, y):
        surroundingSqrs = [[x + offsetX, y + offsetY] for offsetY in range(-1, 2) for offsetX in range(-1, 2)]
        surroundingSqrs = [[newX, newY] for newX, newY in surroundingSqrs if 0 <= newX < self.width and 0 <= newY < self.height]
        surroundingSqrs.remove([x, y])
        return surroundingSqrs

    def orderedPrintGrid(self):
        for row in range(self.height):
            print(self.gridArray[row])


class MinesweeperGrid(Grid):
    def __init__(self, width, height, bombPercentage):
        super().__init__(width, height, 3)
        self.bombPercentage = bombPercentage
        self.createCells()
        self.placeBombs()
        self.calculateNumbers()

    def createCells(self):
        self.gridArray = self.makeGrid(Cell(False, 0, False))

    def placeBombs(self):
        totalBombs = (self.width * self.height * self.bombPercentage) // 100
        bombCoords = set()

        while len(bombCoords) < totalBombs:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            bombCoords.add((x, y))

        for x, y in bombCoords:
            self.gridArray[y][x].value = "BOMB"

    def calculateNumbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.gridArray[y][x].value == "BOMB":
                    continue

                count = 0
                for neighborX, neighborY in self.getSurroundingSqrs(x, y):
                    if self.gridArray[neighborY][neighborX].value == "BOMB":
                        count += 1

                self.gridArray[y][x].value = count

    def revealCell(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return

        if self.gridArray[y][x].revealed:
            return

        self.gridArray[y][x].reveal()

        if self.gridArray[y][x].value == 0:
            for neighborX, neighborY in self.getSurroundingSqrs(x, y):
                self.revealCell(neighborX, neighborY)

    def flagCell(self, x, y):
        if not (0 <= x < self.width and 0 <= y < self.height):
            return

        self.gridArray[y][x].toggleFlag()

    def checkWin(self):
        for row in self.gridArray:
            for cell in row:
                if cell.value != "BOMB" and not cell.revealed:
                    return False
        return True

    def checkLoss(self):
        for row in self.gridArray:
            for cell in row:
                if cell.revealed and cell.value == "BOMB":
                    return True
        return False
