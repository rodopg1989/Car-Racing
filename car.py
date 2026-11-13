import pygame

from settings import (
    WINDOW_HEIGHT,
    ROAD_X,
    LANE_WIDTH,
    CAR_WIDTH,
    CAR_HEIGHT,
    RED,
    WHITE,
    resource_path
)


class Car:

    def __init__(self):

        # Empezamos en el carril central
        self.lane = 1

        # Posición horizontal
        self.x = ROAD_X + self.lane * LANE_WIDTH + (
            LANE_WIDTH - CAR_WIDTH
        ) // 2

        # Posición vertical
        self.y = WINDOW_HEIGHT - CAR_HEIGHT - 30

        # Velocidad de movimiento
        self.speed = 8

        # Rectángulo que representa el coche
        self.rect = pygame.Rect(
            self.x,
            self.y,
            CAR_WIDTH,
            CAR_HEIGHT
        )

        self.image = pygame.image.load(
            resource_path("assets/player_car.png")
        ).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (CAR_WIDTH, CAR_HEIGHT)
        )

    def move_left(self):

        if self.lane > 0:
            self.lane -= 1

    def move_right(self):

        if self.lane < 2:
            self.lane += 1

    def update(self):

        # Calcular la posición horizontal según el carril
        target_x = ROAD_X + self.lane * LANE_WIDTH + (
            LANE_WIDTH - CAR_WIDTH
        ) // 2

        # Desplazarnos suavemente hacia el carril
        if self.x < target_x:
            self.x = min(self.x + self.speed, target_x)

        elif self.x > target_x:
            self.x = max(self.x - self.speed, target_x)

        # Actualizar el rectángulo
        self.rect.x = self.x

    # def draw(self, screen):

    #     # ==============================
    #     # CARROCERÍA
    #     # ==============================

    #     # Sombra de la carrocería
    #     pygame.draw.rect(
    #         screen,
    #         (100, 0, 0),
    #         self.rect,
    #         border_radius=12
    #     )

    #     # Carrocería principal
    #     pygame.draw.rect(
    #         screen,
    #         RED,
    #         (
    #             self.x + 3,
    #             self.y + 2,
    #             CAR_WIDTH - 6,
    #             CAR_HEIGHT - 4
    #         ),
    #         border_radius=12
    #     )

    #     # ==============================
    #     # RUEDAS
    #     # ==============================

    #     for wheel_y in (self.y + 17, self.y + 58):

    #         # Rueda izquierda
    #         pygame.draw.rect(
    #             screen,
    #             (15, 15, 15),
    #             (self.x - 3, wheel_y, 9, 17),
    #             border_radius=3
    #         )

    #         # Rueda derecha
    #         pygame.draw.rect(
    #             screen,
    #             (15, 15, 15),
    #             (self.x + CAR_WIDTH - 6, wheel_y, 9, 17),
    #             border_radius=3
    #         )

    #     # ==============================
    #     # PARABRISAS
    #     # ==============================

    #     pygame.draw.rect(
    #         screen,
    #         (30, 65, 85),
    #         (self.x + 9, self.y + 17, 32, 24),
    #         border_radius=7
    #     )

    #     pygame.draw.rect(
    #         screen,
    #         (100, 190, 220),
    #         (self.x + 12, self.y + 19, 26, 18),
    #         border_radius=5
    #     )

    #     # ==============================
    #     # TECHO / VENTANA TRASERA
    #     # ==============================

    #     pygame.draw.rect(
    #         screen,
    #         (30, 65, 85),
    #         (self.x + 10, self.y + 47, 30, 20),
    #         border_radius=5
    #     )

    #     pygame.draw.rect(
    #         screen,
    #         (100, 190, 220),
    #         (self.x + 13, self.y + 49, 24, 15),
    #         border_radius=4
    #     )

    #     # ==============================
    #     # LUCES DELANTERAS
    #     # ==============================

    #     pygame.draw.rect(
    #         screen,
    #         (255, 255, 180),
    #         (self.x + 7, self.y + 3, 10, 5),
    #         border_radius=2
    #     )

    #     pygame.draw.rect(
    #         screen,
    #         (255, 255, 180),
    #         (self.x + 33, self.y + 3, 10, 5),
    #         border_radius=2
    #     )

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def reset(self):

        # Volver al carril central
        self.lane = 1

        # Calcular la posición horizontal inicial
        self.x = ROAD_X + self.lane * LANE_WIDTH + (
            LANE_WIDTH - CAR_WIDTH
        ) // 2

        # Actualizar el rectángulo
        self.rect.x = self.x