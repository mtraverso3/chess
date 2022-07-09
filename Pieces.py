from abc import ABC, abstractmethod
from typing import List

import pygame as pygame

from main import Board
from main import Tile


class Piece(ABC):
    def __init__(self, white):
        self.white = white

    def isWhite(self):
        return self.white

    @abstractmethod
    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        pass

    @abstractmethod
    def getImg(self):
        pass


# class Cannon(Piece):
#     def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
#         return []
#
#     def getImg(self):
#         return pygame.image.load('resources/BoatW.png')
#
#     def __init__(self, white):
#         super().__init__(white)


class Pawn(Piece):
    def getImg(self):
        return pygame.image.load('resources/PawnW.png') if self.isWhite() else pygame.image.load('resources/PawnB.png')

    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:  # TODO: add diagonal captures / en passant
        validTiles = []

        if self.isWhite():
            up1 = board.board[pos.getX()][pos.getY() - 1]
            up2 = board.board[pos.getX()][pos.getY() - 2]

            if up1.getPiece() is None:
                validTiles.append(up1)
                if pos.getY() == 6 and up2.getPiece() is None:
                    validTiles.append(up2)
        else:
            down1 = board.board[pos.getX()][pos.getY() + 1]
            down2 = board.board[pos.getX()][pos.getY() + 2]

            if down1.getPiece() is None:
                validTiles.append(down1)
                if pos.getY() == 1 and down2.getPiece() is None:
                    validTiles.append(down2)
        return validTiles


class Rook(Piece):

    def getImg(self):
        return pygame.image.load('resources/RookW.png') if self.isWhite() else pygame.image.load('resources/RookB.png')

    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        validTiles = []

        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            while (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles.append(board.board[x][y])
                if board.board[x][y].getPiece() is not None and board.board[x][
                    y].getPiece().isWhite() != self.isWhite():
                    break
                x += direction[0]
                y += direction[1]

        return validTiles


class Knight(Piece):

    def getImg(self):
        return pygame.image.load('resources/KnightW.png') if self.isWhite() else pygame.image.load(
            'resources/KnightB.png')

    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        validTiles = []
        for direction in [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            if (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles.append(board.board[x][y])
        return validTiles


class Bishop(Piece):

    def getImg(self):
        return pygame.image.load('resources/BishopW.png') if self.isWhite() else pygame.image.load(
            'resources/BishopB.png')

    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        validTiles = []

        for direction in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            while (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles.append(board.board[x][y])
                if board.board[x][y].getPiece() is not None and board.board[x][
                    y].getPiece().isWhite() != self.isWhite():
                    break
                x += direction[0]
                y += direction[1]

        return validTiles


class Queen(Piece):

    def getImg(self):
        return pygame.image.load('resources/QueenW.png') if self.isWhite() else pygame.image.load(
            'resources/QueenB.png')

    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        validTiles = []

        # diagonals
        for direction in [(1, 1), (-1, -1), (1, -1), (-1, 1)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            while (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles.append(board.board[x][y])
                if board.board[x][y].getPiece() is not None and board.board[x][
                    y].getPiece().isWhite() != self.isWhite():
                    break
                x += direction[0]
                y += direction[1]

        # vertical/horizontal
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            while (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles.append(board.board[x][y])
                if board.board[x][y].getPiece() is not None and board.board[x][
                    y].getPiece().isWhite() != self.isWhite():
                    break
                x += direction[0]
                y += direction[1]
        return validTiles


class King(Piece):

    def getImg(self):
        return pygame.image.load('resources/KingW.png') if self.isWhite() else pygame.image.load('resources/KingB.png')

    def __init__(self, white):
        super().__init__(white)

    def getValidMoves(self, board: Board, pos: Tile) -> List[Tile]:
        validTiles = []
        for direction in [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)]:
            x = pos.getX() + direction[0]
            y = pos.getY() + direction[1]
            if (0 <= x < 8 and 0 <= y < 8) and (
                    board.board[x][y].getPiece() is None or board.board[x][y].getPiece().isWhite() != self.isWhite()):
                validTiles.append(board.board[x][y])
        return validTiles
