class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimiter = 0
        for x in range(0,len(grid)):
            for y in range(0, len(grid[0])):
                if grid[x][y] == 1:
                    c = 0
                    # Edges
                    c = 0
                    if x == 0:
                        c+=1

                    if x == len(grid)-1:
                        c+=1

                    if y == 0:
                        c+=1

                    if y == len(grid[0])-1:
                        c+=1


                    # Not Edges
                    if x+1 < len(grid) and grid[x+1][y] == 0:
                        c +=1

                    if x-1 >= 0 and grid[x-1][y] == 0:
                        c +=1

                    if y+1 < len(grid[0]) and grid[x][y+1] == 0:
                        c +=1

                    if y-1 >= 0 and grid[x][y-1] == 0:
                        c +=1

                    print(x,y,c)
                    perimiter+=c
        return perimiter
