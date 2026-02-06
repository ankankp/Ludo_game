# board/board.py

import pygame
from settings import *

TILE = 40   # Tile size
GRID = 15   # 15x15 Ludo board


class Board:
    def __init__(self):
        self.tile = TILE

    def draw_grid(self, screen):
        """Draw base grid"""
        for row in range(GRID):
            for col in range(GRID):
                pygame.draw.rect(
                    screen,
                    GRAY,
                    (col*TILE, row*TILE, TILE, TILE),
                    1
                )

    def draw_home_bases(self, screen):
        """Draw player home areas"""

        # Red
        pygame.draw.rect(screen, RED, (0, 0, 6*TILE, 6*TILE))

        # Green
        pygame.draw.rect(screen, GREEN,
                         (9*TILE, 0, 6*TILE, 6*TILE))

        # Blue
        pygame.draw.rect(screen, BLUE,
                         (0, 9*TILE, 6*TILE, 6*TILE))

        # Yellow
        pygame.draw.rect(screen, YELLOW,
                         (9*TILE, 9*TILE, 6*TILE, 6*TILE))

    def draw_center(self, screen):
        """Center finish triangle"""
        center = 6*TILE

        pygame.draw.polygon(
            screen, RED,
            [(center, center),
             (center+3*TILE, center),
             (center+1.5*TILE, center+1.5*TILE)]
        )

        pygame.draw.polygon(
            screen, GREEN,
            [(center+3*TILE, center),
             (center+3*TILE, center+3*TILE),
             (center+1.5*TILE, center+1.5*TILE)]
        )

        pygame.draw.polygon(
            screen, BLUE,
            [(center, center+3*TILE),
             (center, center),
             (center+1.5*TILE, center+1.5*TILE)]
        )

        pygame.draw.polygon(
            screen, YELLOW,
            [(center+3*TILE, center+3*TILE),
             (center, center+3*TILE),
             (center+1.5*TILE, center+1.5*TILE)]
        )

    def draw(self, screen):
        screen.fill(WHITE)

        self.draw_grid(screen)
        self.draw_home_bases(screen)
        self.draw_center(screen)
