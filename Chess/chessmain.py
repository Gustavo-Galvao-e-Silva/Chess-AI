import pygame as pg
from Chess import chessengine

width = height = 400
dimension = 8
sq_size = height // dimension
max_fps = 15
images = {}


def load_images():  # function that load all images with a for loop
    pieces = ['wp', 'wR', 'wN', 'wB', 'wK', 'wQ', 'bp', 'bR', 'bN', 'bB', 'bK', 'bQ']
    for i in pieces:
        images[i] = pg.transform.scale(pg.image.load('images/'+i+'.png'), (sq_size, sq_size))


def main():
    pg.init()
    screen = pg.display.set_mode((width, height))
    clock = pg.time.Clock()
    screen.fill(pg.Color("white"))
    gs = chessengine.GameState()
    valid_moves = gs.get_valid_moves()
    move_made = False
    load_images()
    running = True
    sq_selected = ()
    player_clicks = []
    while running:
        for e in pg.event.get():
            if e.type == pg.QUIT:
                running = False
            elif e.type == pg.MOUSEBUTTONDOWN:  # this code executes a move when the player click on a piece and a file
                loc = pg.mouse.get_pos()
                col = loc[0]//sq_size
                row = loc[1]//sq_size
                if sq_selected == (row, col):  # when a player clicks twice on a piece, it deselects it
                    sq_selected = ()
                    player_clicks = []
                else:  # clicking on a square different from the current one, appends the list of clicks
                    sq_selected = (row, col)
                    player_clicks.append(sq_selected)
                if len(player_clicks) == 2:  # whenever the list has two clicks, it executes the move if it is valid and then resets the list of clicks
                    move = chessengine.Move(player_clicks[0], player_clicks[1], gs.board)
                    if move in valid_moves:
                        gs.make_move(move)
                        move_made = True
                    sq_selected = ()
                    player_clicks = []
            elif e.type == pg.KEYDOWN:  # calls function that undoes move
                if e.key == pg.K_z:
                    gs.undo_move()
                    move_made = True
        if move_made:  # updates the list of valid moves after a move is made
            valid_moves = gs.get_valid_moves()
            move_made = False
        clock.tick(max_fps)
        pg.display.flip()
        draw_game_state(screen, gs)


def draw_game_state(screen, gs):  # calls function that draws the board (might exclude as pieces aren't being drawn)
    draw_board(screen, gs.board)


def draw_board(screen, board):  # creates the image for the board
    colors = [pg.Color("white"), pg.Color("gray")]
    for i in range(dimension):
        for j in range(dimension):
            color = colors[(i + j) % 2]
            pg.draw.rect(screen, color, pg.Rect(j * sq_size, i * sq_size, sq_size, sq_size))
            piece = board[i][j]
            if piece != "--":
                screen.blit(images[piece], pg.Rect(j * sq_size, i * sq_size, sq_size, sq_size))


if __name__ == '__main__':
    main()
