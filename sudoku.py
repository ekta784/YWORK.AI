def sudokuboard(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    for r in range(9):
        for c in range(9):
            if board[r][c]== ".":
                empty.append((r,c))
            else:
                val= board[r][c]
                rows[r].add(val)
                cols[c].add(val)
                boxes[(r // 3) * 3 + c // 3].add(val)
    def backtrack(i=0):
        if i == len(empty):
            return True

        r, c = empty[i]
        b = (r // 3) * 3 + c // 3 
        for ch in map(str, range(1, 10)):
            if ch not in rows[r] and ch not in cols[c] and ch not in boxes[b]:
                
                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

            
                if backtrack(i + 1):
                    return True

                board[r][c] = '.'
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[b].remove(ch)

        return False

    backtrack()
    
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

sudokuboard(board)

for row in board:
    print(row)

