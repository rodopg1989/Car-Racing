import pygame

import random

from settings import (
    WINDOW_HEIGHT,
    ROAD_X,
    ROAD_WIDTH,
    LANE_WIDTH,
    LANES,
    DARK_GRAY,
    WHITE,
    GREEN,
    WINDOW_WIDTH,
    resource_path
)


class Road:

    def __init__(self):

        # Desplazamiento de las líneas de la carretera
        self.line_offset = 0

        # Velocidad de movimiento de las líneas
        self.line_speed = 5

        self.scenery_offset = 0

        self.tree_small = pygame.image.load(
            resource_path("assets/tree_small.png")
        ).convert_alpha()

        self.tree_large = pygame.image.load(
            resource_path("assets/tree_large.png")
        ).convert_alpha()
        self.trees = []

        for y in range(-100, WINDOW_HEIGHT + 300, 150):

            # Árbol izquierdo
            self.trees.append({
                "x": 35,
                "y": y,
                "large": random.choice([True, False])
            })

            # Árbol derecho
            self.trees.append({
                "x": WINDOW_WIDTH - 35,
                "y": y + 50,
                "large": random.choice([True, False])
            })

    def update(self):

        self.line_offset += self.line_speed

        self.scenery_offset += self.line_speed

        if self.scenery_offset >= 150:
            self.scenery_offset = 0

        # Reiniciar el desplazamiento cuando las líneas
        # hayan recorrido cierta distancia
        if self.line_offset >= 80:
            self.line_offset = 0

    def draw(self, screen):

        # Dibujar el césped
        screen.fill(GREEN)

        for tree in self.trees:

            tree_y = (tree["y"] + self.scenery_offset) % (
                WINDOW_HEIGHT + 300
            ) - 100

            self.draw_tree(
                screen,
                tree["x"],
                tree_y,
                large=tree["large"]
            )
        # Dibujar la carretera
        pygame.draw.rect(
            screen,
            DARK_GRAY,
            (ROAD_X, 0, ROAD_WIDTH, WINDOW_HEIGHT)
        )

        # Dibujar las líneas divisorias
        for lane in range(1, LANES):

            x = ROAD_X + lane * LANE_WIDTH

            for y in range(-80, WINDOW_HEIGHT, 80):

                pygame.draw.rect(
                    screen,
                    WHITE,
                    (x - 2, y + self.line_offset, 4, 40)
                )

    def draw_tree(self, screen, x, y, large=False):

        if large:
            image = self.tree_large
            size = (65, 65)
        else:
            image = self.tree_small
            size = (40, 40)

        image = pygame.transform.scale(image, size)

        screen.blit(
            image,
            (x - size[0] // 2, y - size[1] // 2)
        )