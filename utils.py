from datetime import datetime


class DuplicateQueen(Exception):
    pass


class QueenOutOfChessboard(Exception):
    pass


class ChessboardIsEmpty(Exception):
    pass


def log(message):
    print("{} | {}".format(datetime.now(), message))
