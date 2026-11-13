# ==============================
# VENTANA
# ==============================

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700

WINDOW_TITLE = "Car Racing - Python Arcade"


# ==============================
# JUEGO
# ==============================

FPS = 60


# ==============================
# CARRETERA
# ==============================

ROAD_WIDTH = 360
ROAD_X = (WINDOW_WIDTH - ROAD_WIDTH) // 2

LANES = 3
LANE_WIDTH = ROAD_WIDTH // LANES


# ==============================
# COCHES
# ==============================

CAR_WIDTH = 50
CAR_HEIGHT = 90


# ==============================
# VELOCIDAD
# ==============================

INITIAL_SPEED = 5


# ==============================
# COLORES RGB
# ==============================

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

GRAY = (90, 90, 90)
DARK_GRAY = (40, 40, 40)

GREEN = (30, 130, 50)
RED = (220, 30, 30)
BLUE = (30, 100, 220)
YELLOW = (255, 220, 0)

# ==============================
# PROGRESO
# ==============================

TARGET_DISTANCE = 10
DISTANCE_PER_SECOND = 0.1

# ==============================
# GASOLINA
# ==============================

INITIAL_FUEL = 100

FUEL_CONSUMPTION = 2

FUEL_CAN_AMOUNT = 30

GAS_SPAWN_TIME = 5

import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)