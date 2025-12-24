import random
import pygame


class Grid:
    def __init__(self, width, height, dimension):
        self.width = width
        self.height = height
        self.dimension = dimension
        self.arr = [[[0 for i in range(dimension)]
                     for i in range(width)]
                     for i in range(height)]

    def reset_grid(self):
        self.arr = [[[0 for i in range(self.dimension)]
                     for i in range(self.width)]
                     for i in range(self.height)]

    def reset_different(self, value):
        self.arr = [[[value for i in range(self.dimension)]
                     for i in range(self.width)]
                     for i in range(self.height)]

    def save_grid(self):
        with open("textfile.txt", "w") as f:
            f.write(str(self.arr))

    def strToList(self, s):
        if s == "":
            return 0, 0, 0, []

        height = width = dimension = checkNext = count = bcount = 0
        s = s[1:-1]

        while True:
            try:
                if checkNext:
                    checkNext = False
                    if s[count] == "[":
                        height += 1

                if s[count] == "[":
                    checkNext = True
                    bcount += 1

                if s[count] in "[], ":
                    s = s[:count] + s[count + 1:]
                else:
                    count += 1
            except IndexError:
                break

        width = bcount // (height + 1)
        dimension = len(s) // (width * height)

        arr = [[[s[i + j + k] for i in range(dimension)]
                for j in range(width)]
                for k in range(height)]

        return height, width, dimension, arr

    def getFileSave(self):
        with open("textfile.txt", "r") as f:
            self.height, self.width, self.dimension, self.arr = self.strToList(f.read())

    def set_dimension(self, list: list):
        self.dimension = len(list)
        self.arr = [[list.copy() for i in range(self.width)] for j in range(self.height) ]

    def set_width(self, num):
        self.width = num
        self.arr = [[[0 for i in range(self.dimension)]
                     for i in range(self.width)]
                     for i in range(self.height)]

    def set_height(self, num):
        self.height = num
        self.arr = [[[0 for i in range(self.dimension)]
                     for i in range(self.width)]
                     for i in range(self.height)]


    def get_surrounding_sqrs(self, x, y):
        surrounding_sqrB = [ [x + i, y + j] for j in range(-1, 2) for i in range(-1, 2)]
        surrounding_sqr = [ [nx, ny] for nx, ny in surrounding_sqrB if 0 <= nx < self.width and 0 <= ny < self.height ]
        surrounding_sqr.remove([x,y])
        return surrounding_sqr

    def orderedPrintGrid(self):
        for i in range(self.height):
            print(self.arr[i])






