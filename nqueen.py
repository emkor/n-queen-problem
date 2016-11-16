from collections import Counter

from utils import DuplicateQueen, QueenOutOfChessboard, ChessboardIsEmpty




# def csp(chessboard, iter_limit, queen_n):
#     """
#     :type chessboard: nqueen.Chessboard
#     :type iter_limit: int
#     :type queen_n: int
#     :rtype: nqueen.Chessboard
#     """
#     if chessboard.count_conflicts() <= 0:
#         if chessboard.queen_count() >= queen_n:
#             log("Found solution! Returning chessboard...")
#             return chessboard
#         new_queen = _keep_iterating_until_not_duplicated(chessboard, iter_limit)
#         try:
#             log("Adding new {} ...".format(new_queen))
#             chessboard.add_queen(new_queen)
#             return csp(chessboard, iter_limit, queen_n)
#         except DuplicateQueen as e:
#             log(e)
#             return chessboard
#     else:
#         removed_queen = chessboard.remove_last_queen()
#         log("Could not add {} due to conflicts".format(removed_queen))
#         return csp(chessboard, iter_limit, queen_n)
#
#
# def _keep_iterating_until_not_duplicated(chessboard, iter_limit):
#     new_queen = get_random_queen(chessboard.n)
#     iteration = 0
#     while iteration <= iter_limit and new_queen in chessboard.queens:
#         new_queen = get_random_queen(chessboard.n)
#         iteration += 1
#     return new_queen
#
#
# chessboard_size = 8
# queen_count = 4
# iterations_limit = 100
# csp(Chessboard(chessboard_size), iterations_limit, queen_count)
