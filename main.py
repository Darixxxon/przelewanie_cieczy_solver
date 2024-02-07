import copy
import sys
sys.setrecursionlimit(5000)

def check_completed(board):
    if len(board) == 4:
        if board[0] == board[1] == board[2] == board[3]:
            return True
    return False


def looking_for_moves(board, completed, moves):
    for i in range(len(board)):
        if check_completed(board[i]) and completed.count(i) == 0:
            completed.append(i)
    
    if len(completed) == 12:
        return
    for i in range(len(board)):
        if completed.count(i) != 0:
            continue
        for j in range(len(board)):
            board_copy = copy.deepcopy(board)
            moves_copy = moves.copy()
            completed_copy = completed.copy()
            if i is j:
                continue
            if len(board_copy[i]) == 0:
                continue
            if len(board_copy[j]) == 4:
                continue
            if i in completed_copy or j in completed_copy:
                continue
            if len(board_copy[j]) == 0 or (board_copy[i][-1] == board_copy[j][-1] and (4 - len(board_copy[j]) >= check_height(board_copy[i]))):
                board_copy_copy = copy.deepcopy(board_copy)
                for k in range(check_height(board_copy[i])):
                    board_copy_copy[j].append(board_copy_copy[i].pop(-1))
                if board_copy_copy[j] == board_copy[i]:
                    continue
                for k in range(check_height(board_copy[i])):
                    board_copy[j].append(board_copy[i].pop(-1))
                moves_copy.append(str(i+1) + " to " + str(j+1))
                looking_for_moves(board_copy, completed_copy, moves_copy)
                if len(completed_copy) == 12:
                    moves = moves_copy.copy()
                    completed = completed_copy.copy()
                    return
    if len(completed) == 12:
        moves = moves_copy.copy()
        completed = completed_copy.copy()


def check_height(board):
    count = 1
    for i in range(len(board) - 1):
        if board[-1] == board[-i-2]:
            count += 1
        else:
            return count
    return count


lg = "light green"
nv = "navy"
br = "brown"
lb = "light blue"
cm = "camo"
rd = "red"
gr = "grey"
yl = "yellow"
pk = "pink"
dg = "dark green"
mg = "magenta"
db = "dark blue"

board = [[br, br, nv, lg],
         [gr, rd, cm, lb],
         [dg, pk, lb, yl],
         [yl, pk, cm, yl],
         [lg, mg, pk, nv],
         [nv, dg, nv, mg],
         [db, pk, lb, dg],
         [db, cm, lb, db],
         [lg, br, gr, rd],
         [rd, gr, mg, dg],
         [lg, db, mg, gr],
         [yl, cm, br, rd],
         [],
         []]

completed = []
moves = []
moves_final = looking_for_moves(board, completed, moves)

for i in range(len(moves_final)):
    print(moves_final[i])
