class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for x in range(0,len(board),3):
            for y in range(0,len(board),3):
                seen = set()
                for rx in range(3):
                    for cy in range(3):
                        cell = board[x+rx][y+cy]
                        if cell == ".":
                            continue
                        if cell in seen:
                            return False
                        seen.add(cell)
        
        
        for x in range(len(board)):
            seen = set()
            for y in range(len(board)):
                cell = board[x][y]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        

        for y in range(len(board)):
            seen = set()
            for x in range(len(board)):
                cell = board[x][y]
                if cell == ".":
                    continue
                if cell in seen:
                    return False
                seen.add(cell)
        return True

