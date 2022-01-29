"""Board class module"""

LETTERS = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

class Board:
    """The board class (player_num, size)"""
    def __init__(self, player_num, size):
        """Initialize the board"""
        self.board = []
        self.size = size
        self.player_num = player_num
        self.setup_board()

    def setup_board(self):
        """Setup an empty board"""

        for i in range(self.size): # pylint: disable=unused-variable
            board_row = []
            for j in range(self.size): # pylint: disable=unused-variable
                board_row.append(-1)
            self.board.append(board_row)

    def print_board(self, player):
        """Prints the board in a viewable format.
        Player is the player who's turn it is."""

        targetting_board = False
        player_num = self.player_num
        if player != player_num:
            targetting_board = True
        board = self.board

        # print horizontal numbers
        print()
        print("player " + str(player_num) + "'s board:")
        print()
        print("  ", end="")
        for i in range(0, 10):
            print(" " + str(i) + " ", end="")
        print()

        # print board
        for i in range(self.size):

            print(str(LETTERS[i]) + " ", end="")

            for j in range(self.size):
                if board[i][j] == -1:
                    print("[ ]", end="")
                elif board[i][j] == "*":
                    print("[*]", end="")
                elif board[i][j] == "X":
                    print("[X]", end="")
                elif board[i][j] != -1 and targetting_board:
                    print("[ ]", end="")
                else:
                    print("[" + board[i][j].strip() + "]", end="")

            print()
