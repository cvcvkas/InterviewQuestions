def rotate90acw(matrix):
    outMatrix = []
    for x in range(len(matrix)):
        outArray = []
        for y in range(len(matrix)):
            outArray.append(matrix[len(matrix)-1-y][len(matrix)-1-x])
        
        outMatrix.append(outArray[::-1])
    
    return outMatrix

def rotate90cw(matrix):
    outMatrix = []
    for x in range(len(matrix)):
        outArray = []
        for y in range(len(matrix)):
            outArray.append(matrix[y][x])
        
        outMatrix.append(outArray[::-1])
    
    return outMatrix

        
Matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print(rotate90cw(Matrix))