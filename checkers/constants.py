import pygame

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS
RED = (225, 0, 0)
LIGHT_BROWN = (255, 191, 123)
WHITE = (255, 255, 255)
BROWN = (151, 88, 23)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)
CROWN = pygame.transform.scale(pygame.image.load('crown.png'), (44, 25))
BLACK_PIECE = pygame.transform.scale(pygame.image.load('blackPiece.png'), (70, 70))
WHITE_PIECE = pygame.transform.scale(pygame.image.load('whitePiece.png'), (70, 70))

