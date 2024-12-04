def findDiagonalOrder(matrix):
    '''
    Input:matrix (list of length m, with n elements per m element.)
    Output: array of elements in diagonal order.
    PSEUDOCODE
    size of the grid is len(matrix) * len(matrix[0])
        1. m,n -> 0,0
            m0, n1
            m1,n0
            m2, n0
            ------
            m1,n1
            m0,n2
            m1,n2
            m2,n1
            m2,n2
        1. Obtain number of rows ( max(m))
        2. get number of columns ( max(n))

#     '''
    row =len(matrix)
    column = len(matrix[0])
    diagonal_list=[]
    going_up = True
    m=0
    n=0

    while len(diagonal_list) < (row*column):
        diagonal_list.append(matrix[m][n])
        if going_up:
            if n== column-1: 
                m+=1 # move down, into the next row, start moving down
                going_up = False
            elif m == 0: # on the top row
                n+=1 # move to the right
                going_up= False # startMovingDown
            else: # if within bounds, move up and right
                m-=1
                n+=1
        else: # if going down
            if m == row-1: # reaches the max index on the columns
                n +=1
                going_up = True
            elif n == 0:
                m+=1
                going_up=True
            else:
                n-=1
                m+=1
    print(diagonal_list)

findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
