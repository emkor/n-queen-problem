import unittest

from constraint import SameColumnConstraint, SameRowConstraint, SameDiagonalConstraint
from model import Chessboard, Queen


class ConstraintTest(unittest.TestCase):
    def setUp(self):
        self.same_column_constraint = SameColumnConstraint()
        self.same_row_constraint = SameRowConstraint()
        self.same_diagonal_constraint = SameDiagonalConstraint()

    def test_should_same_column_constraint_fail(self):
        chessboard = Chessboard(n=4)

        chessboard.add_queen(Queen(0, 0))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

        chessboard.add_queen(Queen(0, 2))
        self.assertTrue(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

    def test_should_same_row_constraint_fail(self):
        chessboard = Chessboard(n=4)

        chessboard.add_queen(Queen(1, 3))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

        chessboard.add_queen(Queen(0, 3))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertTrue(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

    def test_should_same_diagonal_constraint_fail(self):
        chessboard = Chessboard(n=4)

        chessboard.add_queen(Queen(1, 1))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

        chessboard.add_queen(Queen(3, 3))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertTrue(self.same_diagonal_constraint.is_broken(chessboard))

    def test_should_secondary_diagonal_constraint_fail(self):
        chessboard = Chessboard(n=4)

        chessboard.add_queen(Queen(2, 0))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

        chessboard.add_queen(Queen(3, 1))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertTrue(self.same_diagonal_constraint.is_broken(chessboard))

    def test_should_none_of_constraints_fail(self):
        chessboard = Chessboard(n=4)
        chessboard.add_queen(Queen(1, 0))
        chessboard.add_queen(Queen(0, 2))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))

        chessboard.add_queen(Queen(3, 1))
        self.assertFalse(self.same_column_constraint.is_broken(chessboard))
        self.assertFalse(self.same_row_constraint.is_broken(chessboard))
        self.assertFalse(self.same_diagonal_constraint.is_broken(chessboard))
