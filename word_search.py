class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(board,x,y,word,i):
            if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or i >= len(word):
                return False

            if board[x][y] == word[i]:
                temp = board[x][y]
                board[x][y] = ""

                if i == len(word)-1:
                    return True
                b = dfs(board,x+1,y,word,i+1) or dfs(board,x-1,y,word,i+1) or dfs(board,x,y+1,word,i+1) or dfs(board,x,y-1,word,i+1)
                board[x][y] = temp
                return b

        for x in range(len(board)):
            for y in range(len(board[0])):
                z = board
                if board[x][y] == word[0] and dfs(board,x,y,word,0):
                    return True
        return False
