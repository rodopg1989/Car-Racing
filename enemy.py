import pygame
import random

from settings import (
    ROAD_X,
    LANE_WIDTH,
    CAR_WIDTH,
    CAR_HEIGHT,
    WINDOW_HEIGHT,
    BLUE,
    YELLOW,
    WHITE,
    resource_path
)


class Enemy:

    def __init__(self, lane):

        # Carril donde aparece el enemigo
        self.lane = lane

        # Posición horizontal según el carril
        self.x = ROAD_X + lane * LANE_WIDTH + (
            LANE_WIDTH - CAR_WIDTH
        ) // 2

        # Aparece por encima de la pantalla
        self.y = -CAR_HEIGHT

        # Velocidad vertical
        self.speed = 5

        # Elegir un color aleatorio
        self.color = random.choice([BLUE, YELLOW])

        # Rectángulo para detectar colisiones
        self.rect = pygame.Rect(
            self.x,
            self.y,
            CAR_WIDTH,
            CAR_HEIGHT
        )

        car_images = [
            "assets/enemy_blue.png",
            "assets/enemy_yellow.png",
            "assets/enemy_green.png"
        ]

        image_path = random.choice(car_images)

        self.image = pygame.image.load(
            resource_path(image_path)
        ).convert_alpha()

        self.image = pygame.transform.scale(
            self.image, (CAR_WIDTH, CAR_HEIGHT)
        )
    def update(self):

        # Mover el coche hacia abajo
        self.y += self.speed

        # Actualizar el rectángulo
        self.rect.y = self.y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # def draw(self, screen):

    #     # Dibujar el cuerpo
    #     pygame.draw.rect(
    #         screen,
    #         self.color,
    #         self.rect,
    #         border_radius=8
    #     )

    #     # Dibujar el parabrisas
    #     pygame.draw.rect(
    #         screen,
    #         WHITE,
    #         (
    #             self.x + 8,
    #             self.y + 15,
    #             CAR_WIDTH - 16,
    #             20
    #         ),
    #         border_radius=4
    #     )