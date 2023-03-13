board = [
    [0,9,0, 0,0,3, 6,0,0],
    [0,0,0, 1,0,0, 2,0,0],
    [3,0,2, 0,0,6, 0,9,8],
    [0,0,0, 0,0,0, 1,2,5],
    [0,0,4, 0,0,0, 8,0,0],
    [5,2,9, 0,0,0, 0,0,0],
    [2,4,0, 7,0,0, 5,0,3],
    [0,0,3, 0,0,2, 0,0,0],
    [0,0,8, 3,0,0, 0,1,0]
]

def solve(f):
    # print(f) # Printing each step
    find = find_empty_box(f)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(f, i, (row, col)):
            f[row][col] = i

            if solve(f):
                return True

            f[row][col] = 0

    return False
    


def valid(f, num, ps): # board, number, position
    # checking the row
    for i in range(len(f[0])):
        if f[ps[0]][i] == num and ps[1] != i:
            return False
        
    # Checking the column
    for i in range(len(f)):
        if f[i][ps[1]] == num and ps[0] != i:
            return False
        
    # Checkking the box
    box_x = ps[1] // 3
    box_y = ps[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if f[i][j] == num and (i, j) != ps:
                return False
            
    return True


def p_board(f):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - ")

        for j in range(len(f[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(f[i][j])
            else:
                print(str(f[i][j]) + " ", end="")


def find_empty_box(f):
    for i in range(len(f)):
        for j in range(len(f[0])):
            if f[i][j] == 0:
                return (i,j) # row, coloumn
            
    return None

p_board(board)
print("\n")
solve(board)
p_board(board)