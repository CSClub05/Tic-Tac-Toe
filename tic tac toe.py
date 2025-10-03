board = [1,2,3,4,5,6,7,8,9]
message_storage = ""
value_to_show = ""

x_turn = False
o_turn = False

start = input("X or O starts? ")
if start == "X":
    x_turn = True
else: 
    o_turn = True

win = False

def check_win_x():
    if board[0] == board[1] == board[2] == "X":
        print("X wins.")
        return True
    if board[3] == board[4] == board[5] == "X":
        print("X wins.")
        return True
    if board[6] == board[7] == board[8] == "X":
        print("X wins.")
        return True
    if board[0] == board[3] == board[6] == "X":
        print("X wins.")
        return True
    if board[1] == board[4] == board[7] == "X":
        print("X wins.")
        return True
    if board[2] == board[5] == board[8] == "X":
        print("X wins.")
        return True
    
    if board[0] == board[4] == board[8] == "X":
        print("X wins.")
        return True

    if board[2] == board[4] == board[6] == "X":
        print("X wins.")
        return True

def check_win_o():
    if board[0] == board[1] == board[2] == "O":
        print("O wins.")
        return True
        
    if board[3] == board[4] == board[5] == "O":
        print("O wins.")
        return True
        
    if board[6] == board[7] == board[8] == "O":
        print("O wins.")
        return True

    if board[0] == board[3] == board[6] == "O":
        print("O wins.")
        return True

    if board[1] == board[4] == board[7] == "O":
        print("O wins.")
        return True

    if board[2] == board[5] == board[8] == "O":
        print("O wins.")
        return True
    
    if board[0] == board[4] == board[8] == "O":
        print("O wins.")
        return True

    if board[2] == board[4] == board[6] == "O":
        print("O wins.")
        return True

while win == False:

    if x_turn == True:

        slot = int(input("X slot: ")) 

        while type(board[slot-1]) == str:
            print("Slot taken.")
            slot = int(input("X slot: ")) 
        
        board[slot-1] = "X"

        for i in range(0,3):
            if type(board[i]) != str:
                value_to_show = "[]"
            else:
                value_to_show = board[i]
            message_storage = message_storage + value_to_show + " "

        print(message_storage)
        message_storage = ""

        for i in range(3,6):
            if type(board[i]) != str:
                value_to_show = "[]"
            else:
                value_to_show = board[i]
            message_storage = message_storage + value_to_show + " "
        
        print(message_storage)
        message_storage = ""

        for i in range(6,9):
            if type(board[i]) != str:
                value_to_show = "[]"
            else:
                value_to_show = board[i]
            message_storage = message_storage + value_to_show + " "
                
        print(message_storage)
        message_storage = ""

        x_turn = False
        o_turn = True

    if check_win_o() == True:
        win = True
        break
    if check_win_x() == True:
        win = True
        break

    if type(board[0]) == type(board[1]) == type(board[2]) == type(board[3]) == type(board[4]) == type(board[5]) == type(board[6]) == type(board[7]) == type(board[8]) == str:
        print ("Draw.")
        win = True
        break

    if o_turn == True:

        slot = int(input("O slot: ")) 

        while type(board[slot-1]) == str:
            print("Slot taken.")
            slot = int(input("O slot: ")) 
        
        board[slot-1] = "O"
        
        for i in range(0,3):
            if type(board[i]) != str:
                value_to_show = "[]"
            else:
                value_to_show = board[i]
            message_storage = message_storage + value_to_show + " "

        print(message_storage)
        message_storage = ""

        for i in range(3,6):
            if type(board[i]) != str:
                value_to_show = "[]"
            else:
                value_to_show = board[i]
            message_storage = message_storage + value_to_show + " "
        
        print(message_storage)
        message_storage = ""

        for i in range(6,9):
            if type(board[i]) != str:
                value_to_show = "[]"
            else:
                value_to_show = board[i]
            message_storage = message_storage + value_to_show + " "
                
        print(message_storage)
        message_storage = ""

        x_turn = True
        o_turn = False
    
    if check_win_o() == True:
        win = True
        break
    if check_win_x() == True:
        win = True
        break

    if type(board[0]) == type(board[1]) == type(board[2]) == type(board[3]) == type(board[4]) == type(board[5]) == type(board[6]) == type(board[7]) == type(board[8]) == str:
        print ("Draw.")
        win = True
        break