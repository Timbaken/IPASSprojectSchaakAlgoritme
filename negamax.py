import numpy as np

diepte = 4

schaakmat = 10000
gelijkspel = 0

pawnValue = 1
rookValue = 5
knightValue = 3
bishopValue = 3
queenValue = 9

pawnScores = np.asarray([[0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9, 0.9],
                         [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7],
                         [0.4, 0.4, 0.4, 0.5, 0.5, 0.4, 0.4, 0.4],
                         [0.3, 0.3, 0.3, 0.5, 0.5, 0.3, 0.3, 0.3],
                         [0.2, 0.2, 0.2, 0.4, 0.4, 0.2, 0.2, 0.2],
                         [0.1, 0.2, 0.1, 0.2, 0.2, 0.1, 0.2, 0.1],
                         [0.2, 0.3, 0.3, 0.0, 0.0, 0.3, 0.3, 0.1],
                         [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]])

rookScores = np.asarray([[0.3, 0.3, 0.3, 0.4, 0.4, 0.3, 0.3, 0.3],
                         [0.3, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.3],
                         [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                         [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                         [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                         [0.0, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.0],
                         [0.0, 0.2, 0.2, 0.3, 0.3, 0.2, 0.2, 0.0],
                         [0.3, 0.3, 0.4, 0.5, 0.5, 0.4, 0.3, 0.3]])

knightScores = np.asarray([[0.0, 0.0, 0.0, 0.1, 0.1, 0.0, 0.0, 0.0],
                           [0.0, 0.3, 0.4, 0.6, 0.6, 0.4, 0.3, 0.0],
                           [0.0, 0.4, 0.8, 0.5, 0.5, 0.8, 0.4, 0.0],
                           [0.1, 0.4, 0.5, 0.8, 0.8, 0.5, 0.4, 0.1],
                           [0.1, 0.4, 0.5, 0.8, 0.8, 0.5, 0.4, 0.1],
                           [0.0, 0.4, 0.8, 0.5, 0.5, 0.8, 0.4, 0.0],
                           [0.0, 0.3, 0.4, 0.6, 0.6, 0.4, 0.3, 0.0],
                           [0.0, 0.1, 0.2, 0.2, 0.2, 0.2, 0.1, 0.0]])

bishopScores = np.asarray([[0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2],
                           [0.1, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.1],
                           [0.1, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.1],
                           [0.1, 0.5, 0.5, 0.6, 0.6, 0.5, 0.5, 0.1],
                           [0.1, 0.5, 0.6, 0.6, 0.6, 0.6, 0.5, 0.1],
                           [0.1, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.1],
                           [0.1, 0.4, 0.4, 0.4, 0.4, 0.4, 0.4, 0.1],
                           [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.2]])

queenScores = np.asarray([[0.0, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.0],
                          [0.2, 0.5, 0.4, 0.4, 0.4, 0.4, 0.5, 0.2],
                          [0.2, 0.4, 0.6, 0.6, 0.6, 0.6, 0.4, 0.2],
                          [0.3, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                          [0.4, 0.4, 0.5, 0.5, 0.5, 0.5, 0.4, 0.3],
                          [0.2, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.2],
                          [0.0, 0.4, 0.6, 0.6, 0.6, 0.6, 0.0, 0.0],
                          [0.0, 0.0, 0.2, 0.3, 0.3, 0.2, 0.0, 0.0]])

kingScores = np.asarray([[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                         [0.0, 0.0, 0.5, 0.0, 0.0, 0.0, 1, 0.0]])

def findMove(bord, moves, depth, alpha, beta):
    global NMmove
    NMmove = None
    NegaMaxAlphaBeta(bord, moves, depth, alpha, beta)
    return NMmove

def NegaMaxAlphaBeta(gameState, moves, depth, alpha, beta):
    global NMmove
    if depth == 0:
        return evalBoard(gameState)
    maxScore = alpha
    for move in moves:
        gameState.makeMove(move)
        nieuweMoves = gameState.getValidMoves()
        score = -NegaMaxAlphaBeta(gameState, nieuweMoves, depth - 1, -beta, -maxScore)
        if score >= maxScore:
            maxScore = score
            if depth == diepte:
                NMmove = move
        gameState.undoMove()
        if maxScore >= beta:
            return maxScore
    return maxScore


def evalBoard(gameState):
    nieuweMoves = gameState.getValidMoves()
    if gameState.checkmate:
        return -schaakmat if gameState.white_to_move else schaakmat
    elif gameState.stalemate:
        return gelijkspel

    score = 0
    for i in range(len(gameState.board)):
        for j in range(len(gameState.board[i])):
            schaakStuk = gameState.board[i][j]
            if schaakStuk != "--":
                if schaakStuk[0] == "w":
                    multiplier = 1
                    if schaakStuk[1] == "p":
                        score += pawnScores[i][j] * multiplier
                    elif schaakStuk[1] == "R":
                        score += rookScores[i][j] * multiplier
                    elif schaakStuk[1] == "N":
                        score += knightScores[i][j] * multiplier
                    elif schaakStuk[1] == "B":
                        score += bishopScores[i][j] * multiplier
                    elif schaakStuk[1] == "Q":
                        score += queenScores[i][j] * multiplier
                    elif schaakStuk[1] == "K":
                        score += kingScores[i][j] * multiplier
                if schaakStuk[0] == "b":
                    multiplier = -1
                    if schaakStuk[1] == "p":
                        score += pawnScores[::-1][i][j] * multiplier
                    elif schaakStuk[1] == "R":
                        score += rookScores[i][j] * multiplier
                    elif schaakStuk[1] == "N":
                        score += knightScores[::-1][i][j] * multiplier
                    elif schaakStuk[1] == "B":
                        score += bishopScores[::-1][i][j] * multiplier
                    elif schaakStuk[1] == "Q":
                        score += queenScores[::-1][i][j] * multiplier
                    elif schaakStuk[1] == "K":
                        score += kingScores[::-1][i][j] * multiplier
    return score
