class Solution:
  def minPathSum(self, grid: List[List[int]]) -> int:
    if len(grid) == 1 and len(grid[0]) == 1:
      return grid[0][0]
    
    # init a matrix
    mat = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # O(n)
    mat[0][0] = grid[0][0] #
    # if it is the first col
    for row in range(1, len(grid)): # O(n)
      # then the value of the cell is equal to the sum of current cell
      # and the value of the cell before it
      mat[row][0] = mat[row - 1][0] + grid[row][0]
           
    # if it is the first row
    for col in range(1, len(grid[0])): # O(n) 
      # then the value of the cell is equal to the sum of current cell
      # and the value of the cell above it
      mat[0][col] = mat[0][col - 1] + grid[0][col]
    
    # loop through the grid
    for row in range(1, len(grid)): #O(n) 
      for col in range(1, len(grid[0])): # O(n)
        # calculate value of a cell
        mat[row][col] = min(mat[row - 1][col], mat[row][col - 1]) + grid[row][col]
           
    # return the value of the last cell
    return mat[-1][-1]  
  
  # 2nd attempt
  def minPathSum(self, grid: List[List[int]]) -> int:
    # if length of grid is 0
    if len(grid) == 0:  
      # then return empty list
      return []
    
    # init a var to store the results
    results = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    
    results[0][0] = grid[0][0]
    
    # fill values in the first row
    for i in range(1, len(grid[0])):
      results[0][i] = results[0][i - 1] + grid[0][i] 
      
    # fill values in the first col
    for i in range(1, len(grid)):
      results[i][0] = results[i - 1][0] + grid[i][0]
    
    
    # loop through the matrix
    # loop through the rows
    for row in range(1, len(grid)):
      # loop through the cols
      for col in range(1, len(grid[0])):
        # calculate the value of the cell
        # min of the col before the cell and the row before the cell
        # add it to the existing value of the cell
        results[row][col] = min(results[row - 1][col], results[row][col - 1]) + grid[row][col]
        
    # return result
    return results[-1][-1]
  
  # 3rd attempt
  def minPathSum(self, grid: List[List[int]]) -> int:
    # if length of grid is 0
    if len(grid) == 0:
      # then return 0
      return 0
    
    # if length of grid is 1
    if len(grid) == 1 and len(grid[0]) == 1:
      # then return the value of that cell
      return grid[0][0]
    
    # define a matrix to store the sum of paths
    min_sum = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # O(n)
    
    # loop through the matrix
    # loop through rows
    for row in range(0, len(grid)): # O(n)
      # loop through columns
      for col in range(0, len(grid[0])): # O(n)
        if row == 0 and col == 0:
          min_sum[0][0] = grid[0][0]
        # set the value in each cell
        elif row == 0 and col >= 1:
          min_sum[0][col] = min_sum[0][col - 1] + grid[row][col]
        elif col == 0 and row >= 1:
          min_sum[row][0] = min_sum[row - 1][0] + grid[row][col]
        else:
          min_sum[row][col] = min(min_sum[row - 1][col], min_sum[row][col - 1]) + grid[row][col]
      
    # return the last cell
    return min_sum[-1][-1]
  
  # 4th attempt 
  def minPathSum(self, grid: List[List[int]]) -> int:
    if len(grid) == 0:
      return 0
    
    if len(grid) == 1 and len(grid[0]) == 1:
      return grid[0][0]
    
    min_path_grid = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # O(n)
    
    min_path_grid[0][0] = grid[0][0]
    
    for row in range(len(grid)): # O(n)
      for col in range(len(grid[0])): # O(n)
        
        if row == 0 and col == 0:
          continue
        
        if row == 0:
          min_path_grid[0][col] = min_path_grid[0][col - 1] + grid[0][col]
          
        elif col == 0:
          min_path_grid[row][0] = min_path_grid[row - 1][0] + grid[row][0]
          
        else:
          min_path_grid[row][col] = min(min_path_grid[row - 1][col], min_path_grid[row][col - 1]) + grid[row][col]
    
    return min_path_grid[-1][-1]
