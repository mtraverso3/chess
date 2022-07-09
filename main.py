from Pieces import *
from constants import *


class Board:
    def toString(self):
        text = [""] * 8
        for col in range(8):
            for row in range(8):
                if self.board[col][row].getPiece() is not None:
                    text[
                        row] += f"{type(self.board[col][row].getPiece()).__name__[:4]}({'W' if self.board[col][row].getPiece().isWhite() else 'B'}) "
                    # print piece types
                else:
                    text[row] += "[     ] "

                # text[row] += f"({self.board[col][row].getX()},{self.board[col][row].getY()}) "  # print tile coords
        return "\n".join(text)

    def __init__(self):
        self.board = [[Tile(col, row) for row in range(8)] for col in range(8)]
        self.newBoard()

    def newBoard(self):
        # white pieces:
        for col in range(8):
            self.board[col][6].setPiece(Pawn(True))
        self.board[0][7].setPiece(Rook(True))
        self.board[1][7].setPiece(Knight(True))
        self.board[2][7].setPiece(Bishop(True))
        self.board[3][7].setPiece(Queen(True))
        self.board[4][7].setPiece(King(True))
        self.board[5][7].setPiece(Bishop(True))
        self.board[6][7].setPiece(Knight(True))
        self.board[7][7].setPiece(Rook(True))

        # black pieces
        for col in range(8):
            self.board[col][1].setPiece(Pawn(False))
        self.board[0][0].setPiece(Rook(False))
        self.board[1][0].setPiece(Knight(False))
        self.board[2][0].setPiece(Bishop(False))
        self.board[3][0].setPiece(Queen(False))
        self.board[4][0].setPiece(King(False))
        self.board[5][0].setPiece(Bishop(False))
        self.board[6][0].setPiece(Knight(False))
        self.board[7][0].setPiece(Rook(False))


class Tile:

    def __init__(self, x, y, piece=None):
        self.piece = piece
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.getX()},{self.getY()})"

    def __repr__(self):
        return f"<Tile.({self.getX()},{self.getY()})>"

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getPiece(self):
        return self.piece

    def setPiece(self, piece):
        self.piece = piece

    def getValidMoves(self, board: Board):
        return [] if self.piece is None else self.piece.getValidMoves(board, self)

    def drawPiece(self, win):
        piece = self.getPiece()
        if piece is not None:
            img = piece.getImg()
            if img is not None:
                img = pygame.transform.smoothscale(img, (100, 100))
                win.blit(img, (self.getX() * SQUARE_SIZE, self.getY() * SQUARE_SIZE))


def printCoordBoard():
    text = [""] * 8
    for row in range(8):
        for col in range(8):
            text[row] += f"({col},{row}) "  # print tile coords
    return "\n".join(text)


class Game:
    def __init__(self):
        self.board = Board()
        self.WIN = None

    def start(self):
        surface = None
        selected = False
        validTiles = []

        self.WIN = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")

        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    x, y = x // SQUARE_SIZE, y // SQUARE_SIZE

                    if not selected:
                        validTiles = self.board.board[x][y].getValidMoves(self.board)
                        print(validTiles)
                        surface = self.getValidTileOverlay(validTiles)
                        selected = self.board.board[x][y]
                    else:
                        if (x, y) in [(tile.getX(), tile.getY()) for tile in validTiles]:
                            self.applyMove(selected, self.board.board[x][y])
                        else:
                            pass
                        selected = None
                        surface = None

            self.update(surface)

        pygame.quit()

    def applyMove(self, start: Tile, end: Tile, moveType="DEFAULT"):
        if moveType == "DEFAULT":
            end.setPiece(start.getPiece())
            start.setPiece(None)
        elif moveType == "EN_PASSANT":
            pass  # TODO en-passant capture logic
        elif moveType == "CASTLE":
            pass  # TODO castling logic

    def getValidTileOverlay(self, validTiles):
        surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

        for tile in validTiles:
            pygame.draw.circle(surface, (0, 0, 0, 50),
                               (tile.getX() * SQUARE_SIZE + SQUARE_SIZE / 2,
                                tile.getY() * SQUARE_SIZE + SQUARE_SIZE / 2),
                               SQUARE_SIZE / 4)
        return surface

    def update(self, overlay=None):
        self.draw_squares(self.WIN)
        self.draw_pieces(self.WIN, self.board)
        if overlay is not None:
            self.WIN.blit(overlay, (0, 0))
        pygame.display.update()

    def draw_pieces(self, win, board):
        for row in range(ROWS):
            for col in range(COLS):
                tile = board.board[row][col]
                tile.drawPiece(win)

    def draw_squares(self, win):
        win.fill(DARK_TILE)

        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(win, LIGHT_TILE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


if __name__ == '__main__':
    game = Game()
    game.start()
    # board.board[2][6].setPiece(None)
    # board.board[3][6].setPiece(None)
    # board.board[4][6].setPiece(None)
    # board.board[3][3].setPiece(Pawn(True))
    # board.board[2][5].setPiece(Cannon(True))
    # print(board.toString())
    # print(printCoordBoard())
    # print(str(board.board[1][7].getValidMoves(board)))
