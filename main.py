from utilities import generate_piece, print_board

DEV_MODE = True


def main(game_board: [[int, ], ]) -> [[int, ], ]:
    """
    2048 main function, runs a game of 2048 in the console.

    Uses the following keys:
    w - shift up
    a - shift left
    s - shift down
    d - shift right
    q - ends the game and returns control of the console
    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: returns the ending game board
    """
    # Initialize board's first cell
    # TODO: generate a random piece and location using the generate_piece function
    # TODO: place the piece at the specified location
    piece = generate_piece(game_board)
    game_board[piece['row']][piece['column']] = piece['value']
    
    # Initialize game state trackers
    win = False
    lose = False
    # Returns True if game lost
    def check_lose(game_board): 
        filled = False
        empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
        if not empty_cells:
            filled = True
        valid_move = False
        for row in range(3):
            for col in range(2):
                if game_board[row][col] == game_board[row][col+1]:
                    valid_move = True
        for col in range(3):
            for row in range(2):
                if game_board[row][col] == game_board[row+1][col]:
                    valid_move = True
        if filled and not valid_move:
            return True
        else:
            print('Invalid Move')
            return False
        
    # Returns True if Game is Won
    def check_win(game_board):
        for row in game_board:
            for col in row:
                if col == 2048:
                    return True
        return False
        
    # Return True if Input is Not Valid
    def input_not_valid(user_input):
        valid_inputs = ['a','s','w','d']
        if len(user_input) > 1:
            return True
        elif user_input not in valid_inputs:
            return True
        else:
            return False
            
    # Returns True if board is the same
    def same_board(u_input, game_board):
        original_board = game_board[:]
        changed_board = []
        for row in original_board:
            new_row = []
            for col in row:
                new_row.append(col)
            changed_board.append(new_row)
        if u_input == 'a':
            for i, row in enumerate(changed_board):
                nums = []
                for j, col in enumerate(row):
                    if col > 0:
                        nums.append(col)
                    changed_board[i][j] = 0 #set each spot in row to 0
                #print(nums)
                index = 0
                while index < len(nums)-1:
                    if nums[index] == nums[index+1]:
                        nums[index] = 2 * nums[index]
                        del nums[index+1]
                    index += 1
                #print(nums)
                for index, num in enumerate(nums):
                    changed_board[i][index] = num
        if user_input == 'd':
            for i, row in enumerate(changed_board):
                nums = []
                for j, col in enumerate(row):
                    if col > 0:
                        nums.append(col)
                    changed_board[i][j] = 0 #set each spot in row to 0
                #print(nums)
                index = len(nums) - 1
                while index >= 1:
                    if nums[index] == nums[index-1]:
                        nums[index] = 2 * nums[index]
                        del nums[index-1]
                        index -= 2
                    else:
                        index -= 1
                #print(nums)
                for index, num in enumerate(nums):
                    changed_board[i][index+ (4-len(nums))] = num
                    
        if user_input == 'w':
            for col in range(4):
                nums = []
                for row in range(4):
                    if changed_board[row][col] > 0:
                        nums.append(changed_board[row][col])
                    changed_board[row][col] = 0
                index = 0
                while index < len(nums) - 1:
                    if nums[index] == nums[index+1]:
                        nums[index] = 2 * nums[index]
                        del nums[index+1]
                    index += 1
                for index, num in enumerate(nums):
                    changed_board[index][col] = num
        
        if user_input == 's':
            for col in range(4):
                nums = []
                for row in range(4):
                    if changed_board[row][col] > 0:
                        nums.append(game_board[row][col])
                    changed_board[row][col] = 0
                index = len(nums) - 1
                while index >= 1:
                    if nums[index] == nums[index-1]:
                        nums[index] = 2 * nums[index]
                        del nums[index-1]
                        index -= 2
                    else:
                        index -= 1
                for index, num in enumerate(nums):
                    changed_board[index+ (4-len(nums))][col] = num
        print(original_board)
        print(changed_board)
        if changed_board == original_board:
            return True
        else:
            return False
                   
        
            
    # Game Loop
    while not win and not lose:
        # TODO: Reset user input variable
        user_input = -1
        ''' while input_not_valid(user_input) and user_input != 'q':
            print('Invalid move')
            user_input = input('Enter move: \n')
        if user_input == 'q':
            print('Goodbye')
            break'''
        
        # TODO: Take computer's turn
        piece = generate_piece(game_board)
        
        # place a random piece on the board
        game_board[piece['row']][piece['column']] = piece['value']
        
        # check to see if the game is over using the game_over function
        if game_over(game_board):
            lose = True
            break
        #print('game_over is ran')
        
        # TODO: Show updated board using the print_board function
        print_board(game_board)
        
        # TODO: Take user's turn
        user_input = input('Enter move: \n')
        
        # Take input until the user's move is a valid key
        while (input_not_valid(user_input) and user_input != 'q') or same_board(user_input, game_board):
            print('Invalid move')
            user_input = input('Enter move: \n')
        #print_board(game_board)
            
        # if the user quits the game, print Goodbye and stop the Game Loop
        if user_input == 'q':
            print('Goodbye')
            break
        
        # Execute the user's move
        
        copy_board = game_board[:]
        if user_input == 'a':
            #append numbers that aren't zero into a list
            #print('a is being ran')
            for i, row in enumerate(game_board):
                nums = []
                for j, col in enumerate(row):
                    if col > 0:
                        nums.append(col)
                    game_board[i][j] = 0 #set each spot in row to 0
                #print(nums)
                index = 0
                while index < len(nums)-1:
                    if nums[index] == nums[index+1]:
                        nums[index] = 2 * nums[index]
                        del nums[index+1]
                    index += 1
                #print(nums)
                for index, num in enumerate(nums):
                    game_board[i][index] = num
                    
        if user_input == 'd':
            for i, row in enumerate(game_board):
                nums = []
                for j, col in enumerate(row):
                    if col > 0:
                        nums.append(col)
                    game_board[i][j] = 0 #set each spot in row to 0
                #print(nums)
                index = len(nums) - 1
                while index >= 1:
                    if nums[index] == nums[index-1]:
                        nums[index] = 2 * nums[index]
                        del nums[index-1]
                        index -= 2
                    else:
                        index -= 1
                #print(nums)
                for index, num in enumerate(nums):
                    game_board[i][index+ (4-len(nums))] = num
                    
        if user_input == 'w':
            for col in range(4):
                nums = []
                for row in range(4):
                    if game_board[row][col] > 0:
                        nums.append(game_board[row][col])
                    game_board[row][col] = 0
                index = 0
                while index < len(nums) - 1:
                    if nums[index] == nums[index+1]:
                        nums[index] = 2 * nums[index]
                        del nums[index+1]
                    index += 1
                for index, num in enumerate(nums):
                    game_board[index][col] = num
        
        if user_input == 's':
            for col in range(4):
                nums = []
                for row in range(4):
                    if game_board[row][col] > 0:
                        nums.append(game_board[row][col])
                    game_board[row][col] = 0
                index = len(nums) - 1
                while index >= 1:
                    if nums[index] == nums[index-1]:
                        nums[index] = 2 * nums[index]
                        del nums[index-1]
                        index -= 2
                    else:
                        index -= 1
                for index, num in enumerate(nums):
                    game_board[index+ (4-len(nums))][col] = num
                
        # Check if the user wins
        for row in game_board:
            for col in row:
                if col == 2048:
                    win = True
                    break
        
        
    return game_board


def game_over(game_board: [[int, ], ]) -> bool:
    """
    Query the provided board's game state.

    :param game_board: a 4x4 2D list of integers representing a game of 2048
    :return: Boolean indicating if the game is over (True) or not (False)
    """
    # TODO: Loop over the board and determine if the game is over
    filled = False
    empty_cells = [(y, x) for y, row in enumerate(game_board) for x, cell in enumerate(row) if not cell]
    if not empty_cells:
        filled = True
    valid_move = False
    for row in range(3):
        for col in range(2):
            if game_board[row][col] == game_board[row][col+1]:
                valid_move = True
    for col in range(3):
        for row in range(2):
            if game_board[row][col] == game_board[row+1][col]:
                valid_move = True
    if filled and not valid_move:
        print('True')
        return True
    else:
        return False

if __name__ == "__main__":
    main([[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]])
