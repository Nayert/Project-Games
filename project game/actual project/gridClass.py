class grid :
    def __init__ (self , width , height, dimension) :
        self.width = width
        self.height = height
        self. D = dimension
        self.grid = [[[0 for i in range (dimension) ] for i in range (width)]for i in range (height)]
    def reset_grid (self) :
        self.grid = [[[0 for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def reset_different (self , value) :
         self.grid = [[[value for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def save_grid (self) :
        f= open("textfile.txt" , "w")
        f.write(str(self.grid))
    def strToList(self,s) :
        height = width = dimensions = checkNext = count = bcount =0
        s = s[1:-1]
        while True :
            try :
                if checkNext :
                    checkNext = False
                    if s[count] == "[" :
                          height += 1    
                if s[count] == "[" :
                   checkNext = True 
                   bcount += 1  

                if s[count]  in "[], " :
                    s = s[:count] + s[count+1:]   
                else :
                    count += 1
            except IndexError:
                break
        length  = bcount // (height + 1)
        dimensions = len(s) // (length * height)
        arr = [[[s[i+j+k] for i in range (dimensions)]for j in range (length)]for k in range (height)]
        return height , length , dimensions , arr
    def getFileSave (self):
        f = open("textfile.txt","r")
        self.height , self.length , self.dimensions, self.grid = self.strToList(f.read())
        f.close()
    def set_dimension (self , num) :
        self.dimension = num
        self.grid = [[[0 for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def set_width (self , num) :
        self.width = num
        self.grid = [[[0 for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def set_height (self , num) :
        self.height = num
        self.grid = [[[0 for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def change_sqr (row , coloum , dimension , value) :
        ## used to change a specific co-ordinate
        pass
    def get_sqr () : ##### to do
        ## get a specific coord if given the row and coloum
        return ""
    def orderedPrintGrid (self) :
        for i in range (self.height) :
            print(self.grid[i])


exam = grid(width = 3 , height = 3 , dimension = 2)
exam.set_height(4)
print(exam.grid)




