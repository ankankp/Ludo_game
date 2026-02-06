# main.py

import pygame
import sys

from settings import *
from board.board import Board
from dice.dice import Dice
from player.player import Player
from board.path import PATH


SAFE_TILES = [
    PATH[1],   # Red gate
    PATH[9],
    PATH[14],
    PATH[22],  # Green gate
    PATH[27], 
    PATH[35], # Yellow gate
    PATH[40],# Blue gate
    PATH[48]
]
FINISH_PATHS = {

    0: [  # Red
        (7,1),(7,2),(7,3),(7,4),(7,5),(7,6)
    ],

    1: [  # Green
        (1,7),(2,7),(3,7),(4,7),(5,7),(6,7)
    ],

    2: [  # Blue
        (7,13),(7,12),(7,11),(7,10),(7,9),(7,8)
    ],

    3: [  # Yellow
        (13,7),(12,7),(11,7),(10,7),(9,7),(8,7)
    ]
}


#.....................ADD CAPTURE................
def check_capture(players, current_player):

    attacker = players[current_player]

    for token in attacker.tokens:

        # Skip tokens in base
        if token.path_index == -1:
            continue

        for i, opponent in enumerate(players):

            if i == current_player:
                continue

            for opp_token in opponent.tokens:

                if opp_token.path_index == -1:
                    continue

                # ===== COLLISION CHECK =====
                if token.grid_pos == opp_token.grid_pos:

                    # ---- SAFE TILE ----
                    if token.grid_pos in SAFE_TILES:
                        continue

                    # ---- FINISH LANE IMMUNITY ----
                    if token.finish_index != -1:
                        continue

                    if opp_token.finish_index != -1:
                        continue

                    # ---- CAPTURE ----
                    opp_token.path_index = -1
                    opp_token.grid_pos = opp_token.home_pos

#...................MAIN..............................

def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Ludo Game")

    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    board = Board()
    dice = Dice()

    players = [

        Player((255, 0, 0), [
            (1, 1), (1, 3),
            (3, 1), (3, 3)
        ]),

        Player((0, 255, 0), [
            (1, 11), (1, 13),
            (3, 11), (3, 13)
        ]),

        Player((0, 0, 255), [
            (11, 1), (11, 3),
            (13, 1), (13, 3)
        ]),

        Player((255, 255, 0), [
            (11, 11), (11, 13),
            (13, 11), (13, 13)
        ]),
    ]
    start_index = [1, 14, 40, 27]
   


    current_player = 0
    running = True

    while running:
        clock.tick(FPS)

        # Events
        # -------- EVENTS --------
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:

                    dice_value = dice.roll()

                    player = players[current_player]
                    moved = False

                    # -------- SPAWN TOKEN --------
                    if dice_value == 6:
                        for token in player.tokens:
                            if token.path_index == -1:

                                start = start_index[current_player]
                                token.path_index = start
                                token.grid_pos = PATH[start]
                                moved = True
                                break

                    # -------- MOVE TOKEN --------
                    if not moved:

                        token = player.tokens[
                            player.active_token_index
                        ]

                        if token.finished:
                            pass

                        # -------- OUTER PATH --------
                        elif token.finish_index == -1:

                            token.path_index += dice_value

                            # Enter finish lane after full loop
                            if token.path_index >= len(PATH):

                                finish_step = (
                                    token.path_index - len(PATH)
                                )

                                if finish_step < len(
                                    FINISH_PATHS[current_player]
                                ):
                                    token.finish_index = finish_step
                                    token.grid_pos = FINISH_PATHS[
                                        current_player
                                    ][finish_step]
                                else:
                                    token.path_index -= dice_value

                            else:
                                token.grid_pos = PATH[
                                    token.path_index
                                ]

                        # -------- FINISH LANE --------
                        else:

                            token.finish_index += dice_value

                            if token.finish_index < len(
                                FINISH_PATHS[current_player]
                            ):
                                token.grid_pos = FINISH_PATHS[
                                    current_player
                                ][token.finish_index]

                            else:
                                token.finished = True

                        # Rotate token pointer
                        player.active_token_index = (
                            player.active_token_index + 1
                        ) % len(player.tokens)

                    # Movement done → check capture
                    check_capture(players, current_player)

                    # Turn switching
                    if dice_value != 6:
                        current_player = (
                            current_player + 1
                        ) % len(players)




        # Draw board
        board.draw(screen)

        # Draw players
        for p in players:
            p.draw(screen)

        # UI text (draw BEFORE update)
        dice_text = font.render(
            f"Dice: {dice.value}", True, BLACK
        )
        turn_text = font.render(
            f"Player Turn: {current_player + 1}", True, BLACK
        )

        screen.blit(dice_text, (10, 10))
        screen.blit(turn_text, (10, 50))
        pygame.display.flip()


        #pygame.display.update()

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
