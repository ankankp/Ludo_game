import pygame

TILE = 40


class Token:
    def __init__(self, color, grid_pos):
        self.color = color
        self.home_pos = grid_pos 
        self.grid_pos = grid_pos
        self.path_index = -1  
        self.finish_index = -1
        self.finished = False  


    def draw(self, screen):
        row, col = self.grid_pos

        x = col * TILE + TILE // 2
        y = row * TILE + TILE // 2

        # Fill
        pygame.draw.circle(screen, self.color, (x, y), 12)

        # Border
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 12, 2)


class Player:
    def __init__(self, color, home_positions):
        self.tokens = []

        for pos in home_positions:
            self.tokens.append(Token(color, pos))
        self.active_token_index = 0

    def draw(self, screen):
        for token in self.tokens:
            token.draw(screen)

