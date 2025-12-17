class grid :
    def __init__ (self , width , height, dimension) :
        self.width = width
        self.height = height
        self. D = dimension
        #make grid with dimensions
        self.grid = [[[0 for i in range (dimension) ] for i in range (width)]for i in range (height)]

    def reset_grid (self) :
        self.grid = [[[0 for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def reset_different (self , value) : # resets grid but different value
         self.grid = [[[value for i in range (self.dimension) ] for i in range (self.width)]for i in range (self.height)]
    def save_grid (self) :
        f= open("textfile.txt" , "w")
        f.write(str(self.grid))
    def get_gridFile (self) : #### TO DO #####
        ## input a string of a list 
        ## obtain the potential new dimensions , length and width and give it to self.D etc
        ## return the list as an actual list
        f = open("textfile.txt", "r")
        self.grid = f.read()
        return self.grid
    def set_dimension (self , num) :
        self.dimension = num
    def set_width (self , num) :
        self.width = num
    def set_height (self , num) :
        self.height = num
    def change_sqr (row , coloum , dimension , value) :
        ## used to change a specific co-ordinate
        pass
    def get_sqr () : ##### to do
        ## get a specific coord if given the row and coloum
        return ""
    def orderedPrintGrid (self) :
        for i in range (self.height) :
            print(self.grid[i])


class card () :
    pass


















g = grid(3,3,2)
g.orderedPrintGrid()

