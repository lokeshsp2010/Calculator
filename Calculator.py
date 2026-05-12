class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def display_board(self):
        for i, row in enumerate(self.board):
            print('|'.join(row))
            if i < 2:
                print('-' * 5)

    def make_move(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        # Rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return self.board[i][0]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return self.board[0][i]
        
        # Diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Draw
        if all(cell != ' ' for row in self.board for cell in row):
            return 'Draw'
        
        return None

if __name__ == "__main__":
    game = TicTacToe()
    game.make_move(0, 0)
    game.make_move(1, 1)
    game.make_move(0, 1)
    game.make_move(1, 0)
    game.make_move(0, 2)
    game.display_board()
    print("Winner:", game.check_winner())












