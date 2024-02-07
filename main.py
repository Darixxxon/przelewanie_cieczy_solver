import copy
import os

def check_completed(board):
    if len(board) == 4:
        if board[0] == board[1] == board[2] == board[3]:
            return True
    return False

def looking_for_moves(board, completed, moves):
    for i in range(len(board)):
        if check_completed(board[i]) and completed.count(i) == 0:
            completed.append(i)
    completed_copy = []
    for i in range(len(board)):
        if completed.count(i) != 0:
            continue
        for j in range(len(board)):
            if len(completed_copy) == 12:
                return board_copy, completed_copy, moves_copy
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
                board_copy, completed_copy, moves_copy = looking_for_moves(board_copy, completed_copy, moves_copy)
                if len(completed_copy) == 12:
                    return board_copy, completed_copy, moves_copy
    return board, completed, moves

def check_height(board):
    count = 1
    for i in range(len(board) - 1):
        if board[-1] == board[-i-2]:
            count += 1
        else:
            return count
    return count

def print_colours():
    print("lg = 'light green'")
    print("nv = 'navy'")
    print("br = 'brown'")
    print("lb = 'light blue'")
    print("cm = 'camo'")
    print("rd = 'red'")
    print("gr = 'grey'")
    print("yl = 'yellow'")
    print("pk = 'pink'")
    print("dg = 'dark green'")
    print("mg = 'magenta'")
    print("db = 'dark blue'")
    print("' ' = 'empty'")

def swap_to_colours(tmp):
    match tmp:
        case "lg":
            return "light green"
        case "nv":
            return "navy"
        case "br":
            return "brown"
        case "lb":
            return "light blue"
        case "cm":
            return "camo"
        case "rd":
            return "red"
        case "gr":
            return "grey"
        case "yl":
            return"yellow"
        case "pk":
            return "pink"
        case "dg":
            return "dark green"
        case "mg":
            return "magenta"
        case "db":
            return "dark blue"
        case " ":
            return "empty"
        case _:
            return "error"
            
os.system('cls')
number_of_vials = int(input("Hello, write number of total vials: "))
board = [[] for _ in range(number_of_vials)]
for i in range(number_of_vials):
    for j in range(4):
        os.system('cls')
        print("Use only these acronyms: ")
        print_colours()
        tmp = input("Write colour from the " + str(i+1) + " column and from the " + str(j+1) + " place starting from the bottom")
        tmp = swap_to_colours(tmp)
        if tmp == "error":
            print("Incorrect input please retry")
            j=-1
            continue
        if tmp != "empty":
            board[i].append(tmp)
completed = []
moves = []
board, completed, moves = looking_for_moves(board, completed, moves)

os.system('cls')
for i in range(len(moves)):
    print(moves[i])
