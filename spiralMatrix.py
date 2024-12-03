def spiralOrder(matrix):
    row_max_index = len(matrix)-1
    column_max_index= len(matrix[0])-1
    spiral_list = []

#    define boundaries
    left,right = 0, column_max_index
    top,bottom = 0, row_max_index

    while left <= right and top <= bottom:
        # left -> right movement.
        for column in range(left, right+1):
                spiral_list.append(matrix[top][column])
        top +=1 #move down a row
        
        for row in range(top,bottom+1):
            spiral_list.append(matrix[row][right])
        right -=1 # more r boundary to the l

        if top <= bottom:# l -> r movement along the bottom.
            for column in range(right,left -1,-1):
                spiral_list.append(matrix[bottom][column])
        bottom -=1 # move bottom boundary up

        if left <=right:
            for row in range(bottom,top -1, -1):
                spiral_list.append(matrix[row][left])
            left +=1
    
    print(spiral_list)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
spiralOrder(matrix)
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
spiralOrder(matrix2)