class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        column_check = [[0 for _ in range(len(board))] for _ in range(len(board))]
        board_check = [[0 for _ in range(len(board))] for _ in range(len(board))]
        for i in range(len(board)):
            row_check = [0 for _ in range(len(board))]
            for j in range(len(board)):
                if board[i][j] == ".":
                    continue
                value = int(board[i][j]) - 1 
                if column_check[j][value] != 0:
                    print("col",column_check[j][value])
                    return False 
                if row_check[value] != 0:
                    print("row",row_check[value])
                    return False
                k = (i // 3) * 3 + (j//3)
                if board_check[k][value] != 0:
                    print("board",board_check[k][value])
                    return False 
                row_check[value] = 1
                column_check[j][value] = 1
                board_check[k][value] = 1

        return True
        