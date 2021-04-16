board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '  # returns true, an empty string

def printBoard(board):
    print('   |   |   ')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |   ')

def isBoardFull(board):
    if board.count(' ') > 1:  # count of empty strings > 1
        return  False         # Hence board is not full
    else:
        return True

def isWinner(b, l): # board and letter is passed
    return(
        (b[1] == l and b[2] == l and b[3] == l) or  # i.e. b[1] == l means letter which is present at current position whether 0 or X
        (b[4] == l and b[5] == l and b[6] == l) or
        (b[7] == l and b[8] == l and b[9] == l) or
        (b[1] == l and b[4] == l and b[7] == l) or
        (b[2] == l and b[5] == l and b[8] == l) or
        (b[3] == l and b[6] == l and b[9] == l) or
        (b[1] == l and b[5] == l and b[9] == l) or
        (b[3] == l and b[5] == l and b[7] == l))

def playerMove():
    run = True
    while run:
        move = input("Please enter the postion between 1 - 9 where you want your X to be placed.")
        # try & except are similar to if else, used for such cases as here.
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                     run = False # Our turn is over, now computer's turn
                     insertLetter('X', move)  # If the space is free it will enter X at position move
                else:
                    print("Sorry, The space is occupied")
            
            else:
                print("Type a number between 1 & 9")
        
        except:
            print("Please type a number")


def computerMove():
    possibleMoves = [x for x , letter in enumerate(board) if letter == ' ' and x != 0  ]
    move = 0

    for let in ['O' , 'X']:
        for i in possibleMoves:
            boardcopy = board[:]     # creating copy of the variable
            boardcopy[i] = let
            if isWinner(boardcopy, let):  #It's choosing a move only if it knows it'll be the winner after trying all the permutations/states.
                move = i
                return move

    cornersOpen = []          # corner moves
    for i in possibleMoves:
        if i in [1 , 3 , 7 , 9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:     # moving at center
        move = 5
        return move

    edgesOpen = []             # between moves
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def main():
    print("Welcome to the board game")
    printBoard(board)

    while not(isBoardFull(board)):

        if not(isWinner(board, '0')):
            playerMove()
            printBoard(board)
        
        else:
            print("Sorry you lose")
            break

        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == 0:  # ie computer has no move left
                print("Tie Game")
            else:
                insertLetter('0', move)
                print("Computer placed an O on postion", move, ':')
                printBoard(board)
        else:
            print("You won")
            break


    if isBoardFull(board):
        print("Tie Game")

while True:
    x = input("Do you want to play again?(y / n)")
    if x.lower() == 'y':
        board = [' ' for x in range(10)]
        print("-------------------")
        main()

    else:
        break
