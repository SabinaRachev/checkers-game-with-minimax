import pygame
import pygame_menu
from checkers.constants import WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK
from checkers.game import Game
from minimax.algorithm import minimax

pygame.init()
clock = pygame.time.Clock()
HOVER_COLOR = (50, 70, 90)
FPS = 60
font = pygame.font.SysFont("Times New Norman", 100)
FONT = pygame.font.SysFont("Times New Norman", 60)


def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col


def end_game(win, winner, single):
    end = True
    if winner == WHITE:
        winner = "WHITE"
    else:
        winner = "BLACK"
    end_title = font.render("Winner is " + winner, True, BLACK)
    re_play = FONT.render("play again", True, WHITE)
    menu = FONT.render("menu", True, WHITE)
    play_rect = pygame.Rect(275, 350, 225, 80)
    menu_rect = pygame.Rect(275, 450, 225, 80)
    end_buttons = [
        [re_play, play_rect, BLACK],
        [menu, menu_rect, BLACK]
    ]
    while end:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end = False
            if event.type == pygame.MOUSEMOTION:
                for button in end_buttons:
                    if button[1].collidepoint(event.pos):
                        button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK

            win.blit(end_title, (90, 150))
            start = 350
            for text, rect, color in end_buttons:
                pygame.draw.rect(win, color, rect)
                win.blit(text, (285, start))
                start += 100
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if 275 <= x <= 500 and 350 <= y <= 430:
                            start_the_game(single)
                            end = False
                        elif 275 <= x <= 500 and 450 <= y <= 530:
                            game_intro()
                            end = False
        pygame.display.update()


def start_the_game(single):
    WIN = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('checkers')

    run = True
    game = Game(WIN)
    while run:
        clock.tick(FPS)
        if single and game.turn == WHITE:
            game.check_end_eval()
            value, new_board = minimax(game.get_board(), 4, WHITE, game, float('-inf'), float('inf'))
            game.ai_move(new_board)
        if game.winner() is not None:
            end_game(WIN, game.winner(), single)
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()

    pygame.quit()


def game_intro():
    screen = pygame.display.set_mode((800, 550))
    pygame.display.set_caption('checkers')
    # Background
    bg = pygame.image.load("checkers.png")

    title = font.render("Checkers Game", True, WHITE)
    text1 = FONT.render("1 player", True, WHITE)
    text2 = FONT.render("2 players", True, WHITE)
    text3 = FONT.render("Quit", True, WHITE)

    # Buttons
    rect1 = pygame.Rect(275, 200, 205, 80)
    rect2 = pygame.Rect(275, 300, 205, 80)
    rect3 = pygame.Rect(275, 400, 205, 80)

    buttons = [
        [text1, rect1, BLACK],
        [text2, rect2, BLACK],
        [text3, rect3, BLACK],
    ]

    running = False
    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEMOTION:
                for button in buttons:
                    if button[1].collidepoint(event.pos):
                        button[2] = HOVER_COLOR
                    else:
                        button[2] = BLACK

                        screen.blit(bg, (0, 0))
            screen.blit(title, (100, 80))
            start = 210
            for text, rect, color in buttons:
                pygame.draw.rect(screen, color, rect)
                screen.blit(text, (285, start))
                start += 100
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        x, y = pygame.mouse.get_pos()
                        if 275 <= x <= 480 and 300 <= y <= 380:
                            start_the_game(False)
                            running = False
                        elif 275 <= x <= 480 and 200 <= y <= 280:
                            start_the_game(True)
                            running = False
                        elif rect3.collidepoint(event.pos):
                            return
        pygame.display.update()
        clock.tick(60)


game_intro()
pygame.quit()
