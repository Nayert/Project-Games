def get_sqr (length, height) : ##### to do
        ## get a specific coord if given the row and coloum
    return arr[height][length]

def change_sqr (height , length , dimension , value) :
        ## used to change a specific co-ordinate
    if type(value) is list :
        arr[height][length] = value
        
    else :
        arr[height][length][dimension] = value 

a


arr = [[[1, 2], [3, 4], [5, 6]], [[7, 8], [9, 10], [11, 12]], [[13, 14], [15, 16], [17, 18]]]
change_sqr(1,0,0,[3,4])
print(arr)