"""
Main driver file.
Handling user input.
Displaying current GameStatus object.
"""
import pygame as p
import ChessEngine
from negamax import *
from Puzzels import *
import sys

BOARD_WIDTH = BOARD_HEIGHT = 512
MOVE_LOG_PANEL_WIDTH = 256
MOVE_LOG_PANEL_HEIGHT = puzzleBoardHeight = BOARD_HEIGHT
puzzleBoardWidth = 128
DIMENSION = 8
SQUARE_SIZE = BOARD_HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}


def loadImages():
    """
    Initialize a global directory of images.
    This will be called exactly once in the main.
    """
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (SQUARE_SIZE, SQUARE_SIZE))


def main():
    """
    The main driver for our code.
    This will handle user input and updating the graphics.
    """
    p.init()
    screen = p.display.set_mode((BOARD_WIDTH + MOVE_LOG_PANEL_WIDTH + puzzleBoardWidth, BOARD_HEIGHT))
    clock = p.time.Clock()
    screen.fill(p.Color("white"))
    game_state = ChessEngine.GameState([True, True, True, True], )
    valid_moves = game_state.getValidMoves()
    move_made = False  # flag variable for when a move is made
    loadImages()  # do this only once before while loop
    running = True
    square_selected = ()  # no square is selected initially, this will keep track of the last click of the user (tuple(row,col))
    player_clicks = []  # this will keep track of player clicks (two tuples)
    game_over = False
    move_undone = False
    move_log_font = p.font.SysFont("Arial", 14, False, False)
    puzzel = False
    puzzleBuilder = False
    piece = None
    puzzlePieceSelected = ()
    player_one = True  # if a human is playing white, then this will be True, else False
    player_two = True  # if a hyman is playing white, then this will be True, else False

    while running:
        human_turn = (game_state.white_to_move and player_one) or (not game_state.white_to_move and player_two)
        for e in p.event.get():
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            # mouse handler
            elif e.type == p.MOUSEBUTTONDOWN:
                if not game_over:
                    location = p.mouse.get_pos()  # (x, y) location of the mouse
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    if square_selected == (row, col) or 8 <= col:  # user clicked the same square twice
                        square_selected = ()  # deselect
                        player_clicks = []  # clear clicks
                    else:
                        square_selected = (row, col)
                        player_clicks.append(square_selected)  # append for both 1st and 2nd click
                        if puzzleBuilder and piece != None:
                            game_state.board[row][col] = piece
                    if 12 > col > 7 and row == 7 and not puzzleBuilder:
                        print('loading')
                        score = NegaMaxAlphaBeta(game_state, valid_moves, diepte, -schaakmat, schaakmat)
                        if score == schaakmat and game_state.white_to_move:
                            print('wit heeft een mat in 2')
                        elif score == schaakmat and not game_state.white_to_move:
                            print('zwart heeft een mat in 2')
                        else:
                            print('geen mat gevonden')
                    if col > 12 and row == 1 and puzzleBuilder:
                        castleCol = location[0] / SQUARE_SIZE
                        castleRow = location[1] / SQUARE_SIZE

                        if castleCol < 13.5 and castleRow < 1.5:
                            game_state.current_castling_rights.bqs = not game_state.current_castling_rights.bqs
                        if castleCol > 13.5 and castleRow < 1.5:
                            game_state.current_castling_rights.bks = not game_state.current_castling_rights.bks
                        if castleCol < 13.5 and castleRow > 1.5:
                            game_state.current_castling_rights.wqs = not game_state.current_castling_rights.wqs
                        if castleCol > 13.5 and castleRow > 1.5:
                            game_state.current_castling_rights.wks = not game_state.current_castling_rights.wks

                    if col == 13 and row == 0 and puzzleBuilder:
                        colorRow = location[1] / SQUARE_SIZE
                        if colorRow > 0.5:
                            game_state.white_to_move = not game_state.white_to_move
                        else:
                            valid_moves = game_state.getValidMoves()
                            valid_moves = game_state.getValidMoves()
                            puzzleBuilder = False
                    if col == 12 and row == 0:
                        game_state = ChessEngine.GameState(True, [False, False, False, False],
                                                           [["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                             ["--", "--", "--", "--", "--", "--", "--", "--"]])
                        puzzleBuilder = True
                    if col == 12 and row == 1:
                        game_state = ChessEngine.GameState(True, [True, True, True, True], [
                            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]])
                        valid_moves = game_state.getValidMoves()
                        square_selected = ()
                        player_clicks = []
                        move_made = False
                        game_over = False
                        move_undone = True
                        puzzel = False
                        puzzleBuilder = False
                    if col > 11 and row >= 2 and puzzleBuilder:
                        color = 'w'
                        if col > 12:
                            color = 'b'
                        pieces = {2: 'p', 3: 'R', 4: 'N', 5: 'B', 6: 'K', 7: 'Q'}
                        piece = color + pieces[row]
                        puzzlePieceSelected = (row, col)

                    if len(player_clicks) == 2 and human_turn and not puzzleBuilder:  # after 2nd click
                        move = ChessEngine.Move(player_clicks[0], player_clicks[1], game_state.board)
                        for i in range(len(valid_moves)):
                            if move == valid_moves[i]:
                                game_state.makeMove(valid_moves[i], False)
                                move_made = True
                                square_selected = ()  # reset user clicks
                                player_clicks = []
                        if not move_made:
                            player_clicks = [square_selected]

                else:
                    location = p.mouse.get_pos()  # (x, y) location of the mouse
                    col = location[0] // SQUARE_SIZE
                    row = location[1] // SQUARE_SIZE
                    if col == 12 and row == 0:
                        game_state = ChessEngine.GameState(True, [False, False, False, False],
                                                           [["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                                                            ["--", "--", "--", "--", "--", "--", "--", "--"]])
                        puzzleBuilder = True
                        game_over = False
                    if col == 12 and row == 1:
                        print('yodieyo')
                        game_state = ChessEngine.GameState(True, [True, True, True, True], [
                            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["--", "--", "--", "--", "--", "--", "--", "--"],
                            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
                            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]])
                        valid_moves = game_state.getValidMoves()
                        square_selected = ()
                        player_clicks = []
                        move_made = False
                        game_over = False
                        move_undone = True
                        puzzel = False
                        puzzleBuilder = False

            # key handler
            elif e.type == p.KEYDOWN:
                if e.key == p.K_z:  # undo when 'z' is pressed
                    game_state.undoMove()
                    move_made = True
                    game_over = False
                    move_undone = True
                if e.key == p.K_r:  # reset the game when 'r' is pressed
                    game_state = ChessEngine.GameState(True, [True, True, True, True], [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bp", "bp", "bp", "bp", "bp", "bp", "bp", "bp"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--"],
            ["wp", "wp", "wp", "wp", "wp", "wp", "wp", "wp"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]])
                    valid_moves = game_state.getValidMoves()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    game_over = False
                    move_undone = True
                    puzzel = False
                if e.key == p.K_f:
                    game_state = getRandomPuzzle()
                    square_selected = ()
                    player_clicks = []
                    move_made = False
                    game_over = False
                    move_undone = True
                    game_state.in_check, game_state.pins, game_state.checks = game_state.checkForPinsAndChecks()
                    valid_moves = game_state.getValidMoves()
                    valid_moves = game_state.getValidMoves()

                if e.key == p.K_s:
                    puzzel = True
                    if game_state.checkmate:
                        puzzel = False
                if e.key == p.K_a:
                    puzzel = False

        if not game_over and not human_turn and not move_undone or puzzel:
            negaMax = findMove(game_state, valid_moves, diepte, -schaakmat, schaakmat)
            game_state.makeMove(negaMax)

            move_made = True
            if game_state.checkmate:
                puzzel = False

        if move_made:
            valid_moves = game_state.getValidMoves()
            move_made = False
            move_undone = False

        drawGameState(screen, game_state, valid_moves, square_selected, puzzlePieceSelected, puzzleBuilder)

        if not game_over:
            drawMoveLog(screen, game_state, move_log_font)

        if game_state.checkmate and not puzzleBuilder:
            game_over = True
            puzzel = False
            if game_state.white_to_move:
                drawEndGameText(screen, "Black wins by checkmate")
            else:
                drawEndGameText(screen, "White wins by checkmate")

        elif game_state.stalemate and not puzzleBuilder:
            game_over = True
            puzzel = False
            drawEndGameText(screen, "Stalemate")

        clock.tick(MAX_FPS)
        p.display.flip()


def drawGameState(screen, game_state, valid_moves, square_selected, puzzlePieceSelected, puzzleBuilder):
    """
    Responsible for all the graphics within current game state.
    """
    drawBoard(screen)  # draw squares on the board
    highlightSquares(screen, game_state, valid_moves, square_selected, puzzlePieceSelected, puzzleBuilder)
    drawPieces(screen, game_state.board)  # draw pieces on top of those squares
    drawPuzleOptions(screen, game_state)



def drawPuzleOptions(screen, game_state):
    """
    Tekent alle puzzelopties op het scherm met tekst
    En tekent de schaakstukken opties voor de puzzelbuilder

    Parameters
    ----------
    screen: pygame.display
        scherm wat pygame laat zien
    gameState: Gamestate
        de gamestate die bekeken gaat worden

    Returns
    -------
    niet van toepassing
    """
    p.draw.rect(screen, p.Color("light blue"), p.Rect(12*SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
    p.draw.rect(screen, p.Color("purple"), p.Rect(13 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE))
    p.draw.rect(screen, p.Color("blue"), p.Rect(12 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    p.draw.rect(screen, p.Color("red"), p.Rect(13 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))



    pieces = {2: 'p', 3: 'R', 4: 'N', 5: 'B', 6: 'K', 7: 'Q'}
    for i in range(2, 8):
        screen.blit(IMAGES['w' + pieces[i]], p.Rect(12 * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        screen.blit(IMAGES['b' + pieces[i]], p.Rect(13 * SQUARE_SIZE, i * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
    if game_state.current_castling_rights.wks:
        p.draw.rect(screen, p.Color('green'), p.Rect(13.5 * SQUARE_SIZE, 1.5 *SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
    if game_state.current_castling_rights.bks:
        p.draw.rect(screen, p.Color('green'), p.Rect(13.5 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
    if game_state.current_castling_rights.wqs:
        p.draw.rect(screen, p.Color('green'), p.Rect(13 * SQUARE_SIZE, 1.5 * SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
    if game_state.current_castling_rights.bqs:
        p.draw.rect(screen, p.Color('green'), p.Rect(13 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE / 2))
    if game_state.white_to_move:
        p.draw.rect(screen, p.Color('white'), p.Rect(13 * SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE, SQUARE_SIZE / 2))
    else:
        p.draw.rect(screen, p.Color('black'), p.Rect(13 * SQUARE_SIZE, SQUARE_SIZE / 2, SQUARE_SIZE, SQUARE_SIZE / 2))

    font = p.font.SysFont("Helvetica", 20, True, False)
    text_object = font.render('builder', False, p.Color("black"))
    text_location = p.Rect(12 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE).move(
        SQUARE_SIZE / 2 - text_object.get_width() / 2,
        SQUARE_SIZE / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    font = p.font.SysFont("Helvetica", 20, True, False)
    text_object = font.render('play', False, p.Color("black"))
    text_location = p.Rect(13 * SQUARE_SIZE, 0, SQUARE_SIZE, SQUARE_SIZE).move(
        SQUARE_SIZE / 2 - text_object.get_width() / 2,
        SQUARE_SIZE / 6 - text_object.get_height() / 6)
    screen.blit(text_object, text_location)
    text_object = font.render('reset', False, p.Color("black"))
    text_location = p.Rect(12 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE).move(
        SQUARE_SIZE / 2 - text_object.get_width() / 2,
        SQUARE_SIZE / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render('castle', False, p.Color("black"))
    text_location = p.Rect(13 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE).move(
        SQUARE_SIZE / 2 - text_object.get_width() / 2,
        SQUARE_SIZE / 3 - text_object.get_height() / 3)
    screen.blit(text_object, text_location)
    text_object = font.render('rights', False, p.Color("black"))
    text_location = p.Rect(13 * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE).move(
        SQUARE_SIZE / 2 - text_object.get_width() / 2,
        SQUARE_SIZE / 3 * 2 - text_object.get_height() / 3 * 2)
    screen.blit(text_object, text_location)



def drawBoard(screen):
    """
    Draw the squares on the board.
    The top left square is always light.
    """
    global colors
    colors = [p.Color("white"), p.Color("gray")]
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            color = colors[((row + column) % 2)]
            p.draw.rect(screen, color, p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        color = colors[((row + 12) % 2)]
        p.draw.rect(screen, color, p.Rect(12 * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        color = colors[((row + 13) % 2)]
        p.draw.rect(screen, color, p.Rect(13 * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def highlightSquares(screen, game_state, valid_moves, square_selected, puzzlePieceSelected, puzzleBuilder):
    """
    Highlight square selected and moves for piece selected.
    """
    if (len(game_state.move_log)) > 0:
        last_move = game_state.move_log[-1]
        s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('green'))
        screen.blit(s, (last_move.end_col * SQUARE_SIZE, last_move.end_row * SQUARE_SIZE))
    if square_selected != () and not puzzleBuilder:
        row, col = square_selected
        if game_state.board[row][col][0] == (
                'w' if game_state.white_to_move else 'b'):  # square_selected is a piece that can be moved
            # highlight selected square
            s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
            s.set_alpha(100)  # transparency value 0 -> transparent, 255 -> opaque
            s.fill(p.Color('blue'))
            screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))
            # highlight moves from that square
            s.fill(p.Color('yellow'))
            for move in valid_moves:
                if move.start_row == row and move.start_col == col:
                    screen.blit(s, (move.end_col * SQUARE_SIZE, move.end_row * SQUARE_SIZE))
    if puzzlePieceSelected != () and puzzleBuilder:
        row, col = puzzlePieceSelected
        s = p.Surface((SQUARE_SIZE, SQUARE_SIZE))
        s.set_alpha(100)
        s.fill(p.Color('blue'))
        screen.blit(s, (col * SQUARE_SIZE, row * SQUARE_SIZE))

def drawPieces(screen, board):
    """
    Draw the pieces on the board using the current game_state.board
    """
    for row in range(DIMENSION):
        for column in range(DIMENSION):
            piece = board[row][column]
            if piece != "--":
                screen.blit(IMAGES[piece], p.Rect(column * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))


def drawMoveLog(screen, game_state, font):
    """
    Draws the move log.

    """
    move_log_rect = p.Rect(BOARD_WIDTH, 0, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT)
    p.draw.rect(screen, p.Color('black'), move_log_rect)
    move_log = game_state.move_log
    move_texts = []
    for i in range(0, len(move_log), 2):
        move_string = str(i // 2 + 1) + '. ' + str(move_log[i]) + " "
        if i + 1 < len(move_log):
            move_string += str(move_log[i + 1]) + "  "
        move_texts.append(move_string)

    moves_per_row = 3
    padding = 5
    line_spacing = 2
    text_y = padding
    for i in range(0, len(move_texts), moves_per_row):
        text = ""
        for j in range(moves_per_row):
            if i + j < len(move_texts):
                text += move_texts[i + j]

        text_object = font.render(text, True, p.Color('white'))
        text_location = move_log_rect.move(padding, text_y)
        screen.blit(text_object, text_location)
        text_y += text_object.get_height() + line_spacing
    p.draw.rect(screen, p.Color("brown"),
                p.Rect(BOARD_WIDTH, 7 * SQUARE_SIZE, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT))
    font = p.font.SysFont("Helvetica", 20, True, False)
    text_object = font.render('check for Mate', False, p.Color("black"))
    text_location = p.Rect(BOARD_WIDTH, 7 * SQUARE_SIZE, MOVE_LOG_PANEL_WIDTH, MOVE_LOG_PANEL_HEIGHT).move(
        4 * SQUARE_SIZE / 2 - text_object.get_width() / 2,
        SQUARE_SIZE / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)


def drawEndGameText(screen, text):
    font = p.font.SysFont("Helvetica", 32, True, False)
    text_object = font.render(text, False, p.Color("gray"))
    text_location = p.Rect(0, 0, BOARD_WIDTH, BOARD_HEIGHT).move(BOARD_WIDTH / 2 - text_object.get_width() / 2,
                                                                 BOARD_HEIGHT / 2 - text_object.get_height() / 2)
    screen.blit(text_object, text_location)
    text_object = font.render(text, False, p.Color('black'))
    screen.blit(text_object, text_location.move(2, 2))

if __name__ == "__main__":
    main()
