import unittest
import ChessEngine
import negamax

class testcases(unittest.TestCase):
    def testEvalBoard(self):
        gameState = ChessEngine.GameState(True, [False, False, False, False],
[["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "--"],
 ["--", "--", "--", "--", "--", "--", "--", "wQ"]])
        expected = 9
        actual = negamax.evalBoard(gameState)
        self.assertEqual(actual, expected)

        gameState = ChessEngine.GameState(False, [False, False, False, False],
                                          [["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "bQ", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"]])
        expected = -9.5
        actual = negamax.evalBoard(gameState)
        self.assertEqual(actual, expected)

        gameState = ChessEngine.GameState(False, [False, False, False, False],
                                          [["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "bQ", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "wQ", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"]])
        expected = 0
        actual = negamax.evalBoard(gameState)
        self.assertEqual(actual, expected)


    def testNegaMax(self):
        gameState = ChessEngine.GameState(False, [False, False, False, False],
                                          [["--", "--", "bK", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "bQ", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "wQ", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "wp", "wp", "wp"],
                                           ["--", "--", "--", "--", "--", "--", "wK", "--"]])
        moves = gameState.getValidMoves()
        moves = gameState.getValidMoves()
        expected = negamax.schaakmat
        actual = negamax.NegaMaxAlphaBeta(gameState, moves, negamax.diepte, -negamax.schaakmat, negamax.schaakmat)
        self.assertEqual(actual, expected)

        gameState = ChessEngine.GameState(True, [False, False, False, False],
                                          [["--", "bK", "--", "--", "--", "--", "--", "--"],
                                           ["bp", "bp", "bp", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "bQ", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "wQ", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "wK", "--", "--"]])
        moves = gameState.getValidMoves()
        moves = gameState.getValidMoves()
        expected = negamax.schaakmat
        actual = negamax.NegaMaxAlphaBeta(gameState, moves, negamax.diepte, -negamax.schaakmat, negamax.schaakmat)
        self.assertEqual(actual, expected)

    def testFindMove(self):
        gameState = ChessEngine.GameState(True, [False, False, False, False],
                                          [["--", "bK", "--", "--", "--", "--", "--", "--"],
                                           ["bp", "bp", "bp", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "bQ", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "wQ", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "--", "--", "--"],
                                           ["--", "--", "--", "--", "--", "wK", "--", "--"]])
        moves = gameState.getValidMoves()
        moves = gameState.getValidMoves()
        expected = "Qh8"
        move = negamax.findMove(gameState, moves, negamax.diepte, -negamax.schaakmat, negamax.schaakmat)
        actual = move.getChessNotation()
        self.assertEqual(actual, expected)
        gameState.makeMove(move)
        moves = gameState.getValidMoves()
        expected = "Qd8"
        move = negamax.findMove(gameState, moves, negamax.diepte, -negamax.schaakmat, negamax.schaakmat)
        actual = move.getChessNotation()
        self.assertEqual(actual, expected)

        gameState.makeMove(move)
        moves = gameState.getValidMoves()
        expected = "Qxd8"
        move = negamax.findMove(gameState, moves, negamax.diepte, -negamax.schaakmat, negamax.schaakmat)
        actual = move.getChessNotation()
        self.assertEqual(actual, expected)

        gameState.makeMove(move)
        gameState.getValidMoves()
        expected = True
        actual = gameState.checkmate
        self.assertEqual(actual, expected)
        Expected = False
        actual = gameState.white_to_move
        self.assertEqual(actual, expected)

