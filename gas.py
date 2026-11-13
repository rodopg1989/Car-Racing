
import pygame
import random

from settings import (
    ROAD_X,
    LANE_WIDTH,
    YELLOW,
    BLACK
)


class Gas:

    def __init__(self, enemies):

        # Buscar carriles disponibles
        available_lanes = []

        for lane in range(3):

            occupied = False

            for enemy in enemies:

                # Comprobar si hay un enemigo cerca
                if enemy.lane == lane and enemy.y < 150:

                    occupied = True
                    break

            if not occupied:
                available_lanes.append(lane)

        # Si no hay carriles disponibles, no crear bidón
        if not available_lanes:
            self.valid = False
            return

        self.valid = True

        # Elegir un carril disponible
        self.lane = random.choice(available_lanes)

        # Posición horizontal
        self.width = 30
        self.height = 40

        self.x = (
            ROAD_X
            + self.lane * LANE_WIDTH
            + (LANE_WIDTH - self.width) // 2
        )

        self.y = -50

        self.speed = 5

        self.rect = pygame.Rect(
            self.x,
            self.y,
            self.width,
            self.height
        )

    def update(self):

        self.y += self.speed
        self.rect.y = self.y

    def draw(self, screen):

        pygame.draw.rect(
            screen,
            YELLOW,
            self.rect,
            border_radius=5
        )

        pygame.draw.rect(
            screen,
            BLACK,
            (self.x + 10, self.y - 4, 10, 5)
        )
