class GameState:  # class that tracks board state
    def __init__(self):
        # First, lowercase, letter indicates color, second, uppercase, indicates type, and -- indicates an empty file
        # The board is a 8x8 2d list
        self.board = [["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                      ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["--", "--", "--", "--", "--", "--", "--", "--"],
                      ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                      ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]]
        self.white_to_move = True
        self.move_log = []

    def make_move(self, move):  # updates board when a piece moves
        self.board[move.start_row][move.start_col] = '--'
        self.board[move.end_row][move.end_col] = move.piece_moved
        self.move_log.append(move)
        self.white_to_move = not self.white_to_move

    def undo_move(self):  # returns board to state of a move before the current one
        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_col] = move.piece_moved
            self.board[move.end_row][move.end_col] = move.piece_captured
            self.white_to_move = not self.white_to_move

    def get_valid_moves(self):  # checks which moves out of all possible won't lead to check and returns them in a list
        return self.get_all_moves()

    def get_all_moves(self):  # checks all  existing moves, and returns a list
        moves = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                turn = self.board[i][j][0]
                if (turn == 'w' and self.white_to_move) or (turn == 'b' and not self.white_to_move):  # implements turns and checks if selected piece is of the player who is playing
                    piece = self.board[i][j][1]
                    if piece == 'p':  # checks each piece's move
                        self.get_pawn_moves(i, j, moves)
                    elif piece == 'R':
                        self.get_rook_moves(i, j, moves)
                    elif piece == 'N':
                        self.get_knight_moves(i, j, moves)
                    elif piece == 'B':
                        self.get_bishop_moves(i, j, moves)
                    elif piece == 'Q':
                        self.get_queen_moves(i, j, moves)
                    elif piece == 'K':
                        self.get_king_moves(i, j, moves)
        return moves

    def get_pawn_moves(self, row, col, moves):
        pass

    def get_rook_moves(self, row, col, moves):
        pass

    def get_knight_moves(self, row, col, moves):
        pass

    def get_bishop_moves(self, row, col, moves):
        pass

    def get_queen_moves(self, row, col, moves):
        pass

    def get_king_moves(self, row, col, moves):
        pass


class Move:  # class that categorizes each move and allows to check if a move is equal to another
    def __init__(self, start_sq, end_sq, board):
        self.start_row = start_sq[0]
        self.start_col = start_sq[1]
        self.end_row = end_sq[0]
        self.end_col = end_sq[1]
        self.piece_moved = board[self.start_row][self.start_col]
        self.piece_captured = board[self.end_row][self.end_col]
        self.move_id = self.start_row * 1000 + self.start_col * 100 + self.end_row * 10 + self.end_col  # creates an ID number for each move

    def __eq__(self, other):  # overrides the == method for Move objects so it checks their ID's
        if isinstance(other, Move):
            return self.move_id == other.move_id
        return False
