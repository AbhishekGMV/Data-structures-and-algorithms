def setMatrixToZero(matrix):
    # 0(NM) TIME, O(N+M) SPACE

    rowSet = set()
    colSet = set()
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 0:
                rowSet.add(row)
                colSet.add(col)

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if row in rowSet or col in colSet:
                matrix[row][col] = 0
    print(matrix)

def setMatrixZeroOptimal(matrix):
   # O(1) - space, O(NM) - time
   ROWS, COLS = len(matrix), len(matrix[0])
   rowZero = False

   for r in range(ROWS):
       for c in range(COLS):
           if matrix[r][c] == 0:
               matrix[0][c] = 0
               if r == 0:
                   rowZero = True
               else:
                   matrix[r][0] = 0

   for r in range(1, ROWS):
      for c in range(1, COLS):
          if matrix[0][c] == 0 or matrix[r][0] == 0:
              matrix[r][c] = 0

   # Check if first col is zero
   if matrix[0][0] == 0:
       for r in range(ROWS):
           matrix[r][0] = 0

   if rowZero:
      for c in range(COLS):
         matrix[0][c] = 0
   print(matrix)




matrix = [
    [1,2,0],
    [4,5,6],
    [0,8,9],
    ]
setMatrixZeroOptimal(matrix)
