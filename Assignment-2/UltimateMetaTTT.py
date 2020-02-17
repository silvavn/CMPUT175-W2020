#----------------------------------------------------
# Assignment 2: Tic Tac Toe classes
# 
# Author: Victor Silva
# Collaborators:
# References:
#----------------------------------------------------

class TicTacToe:
    '''
    Abstract Class TicTacToe
    Implements the general methods for the TicTacToe Game
    '''
    def __init__(self):
        raise Exception('Each Class must implement their own __init__')

    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        for i in self.board:
            print (i)


    def isValidPosition(self, row, col):
        if 0 > row > len(self.board):
            return False
        elif 0 > col > len(self.board):
            return False
        return True


    def update(self, row, col, mark):
        '''
        Assigns <mark>, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           mark <str or int> - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row, col): return False
        try:
            self.board[row][col] = mark
        except:
            return False
        return True

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is "empty", or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == 0 or self.board[row][col] == '':
            return True
        return False

    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares.
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        for i in range(len(self.board)):
            for j in range(len(i)):
                if self.squareIsEmpty(self.board[i][j]):
                    return False
        return True

    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        for i in board:
            for j in i:
                if not type(j) is int:
                    return False
        return True

    def __getLines(self):
        lines = []

        #HORIZONTAL
        for i in self.board:
            lines.append(i)

        #VERTICAL
        lines.extend([[i[x] for i in self.board] for x in range(len(self.board))])

        #DIAGONAL
        lines.append([self.board[i][i] for i in range(len(self.board))])
        lines.append([self.board[len(self.board) - 1 - i][i] for i in range(len(self.board))])

        return lines

    def isWinner(self):
        raise Exception('Must be implemented!!!')

class NumTicTacToe(TicTacToe):
    def __init__(self):
        self.board = [[0] * 3] * 3

    def update(self, row, col, mark):
        if not type(mark) is int:
            return False

        super().update(row, col, mark)


    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for i in self.__getLines():
            if sum(i) == 15:
                return True
        return False

    
class ClassicTicTacToe:
    def __init__(self):
        '''
        Initializes an empty Classic Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [['']*3]*3
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) with 
        matching marks (i.e. 3 Xs  or 3 Os). That line can be horizontal, vertical,
        or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        for i in self.__getLines():
            if ''.join(i) == 'xxx' or ''.join(i) == 'ooo':
                return True
        return False 


class MetaTicTacToe(TicTacToe):
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''      
        self.board = []
        with open(configFile) as f:
            self.board = [i.lower().strip().split() for i in f]
                
    
    def getLocalBoard(self, row, col):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        val = self.board[row][col].lower()
        if val in ['x', 'o', 'd']:
            return None
        elif val == 'n':
            self.board[row][col] = NumTicTacToe()
        elif val == 'c':
            self.board[row][col] = ClassicTicTacToe()


        raise Exception('File has error')


def game():
    meta_game = MetaTicTacToe('MetaTTTconfig.txt')
    print('Welcome to Ultimate TicTacToe')
    print('This is the current board:')
    meta_game.drawBoard()

    row = int(input('Player 1, please insert your play row: '))
    col = int(input('Player 1, please insert your play column: '))

    






if __name__ == "__main__":
    game()
    # TEST EACH CLASS THOROUGHLY HERE
