import pygame
import random

from settings import (
    FUEL_CAN_AMOUNT,
    FUEL_CONSUMPTION,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    FPS,
    WHITE,
    TARGET_DISTANCE,
    DISTANCE_PER_SECOND,
    YELLOW,
    GREEN,
    RED
)

from road import Road

from car import Car

from enemy import Enemy

from gas import Gas


# Inicializar Pygame
pygame.init()

# Crear ventana
screen = pygame.display.set_mode(
    (WINDOW_WIDTH, WINDOW_HEIGHT)
)

pygame.display.set_caption(WINDOW_TITLE)

# Control del tiempo
clock = pygame.time.Clock()

# Crear carretera
road = Road()

# Crear coche
car = Car()

# Crear enemigos

enemies = []

# Bidones de gasolina
gas_cans = []

# Temporizador para generar gasolina
gas_spawn_timer = 0

# Tiempo entre apariciones (milisegundos)
gas_spawn_interval = 5000

#Tiempo para generar enemigos
spawn_timer = 0

#Tiempo entre enemigos (en milisegundos)
spawn_interval = 1200

# Bucle principal
running = True

game_over = False

distance = 0.0

# Gasolina inicial
fuel = 100.0

# Mensaje al recoger gasolina
fuel_message_timer = 0

difficulty_level = 0

game_won = False

# Fuente para mostrar Game Over
font = pygame.font.SysFont(None, 64)

hud_font = pygame.font.SysFont("consolas", 22, bold=True)
small_font = pygame.font.SysFont("consolas", 16)

while running:

    dt = clock.tick(FPS)

    # Procesar eventos
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if game_over or game_won:

                if event.key == pygame.K_r:
                    car.reset()

                    enemies = []
                    spawn_timer = 0
                    distance = 0.0
                    game_over = False
                    difficulty_level = 0
                    spawn_interval = 1200
                    game_won = False
                    gas_cans = []
                    gas_spawn_timer = 0
                    fuel = 100.0

            else:

                if event.key == pygame.K_LEFT:
                    car.move_left()

                elif event.key == pygame.K_RIGHT:
                    car.move_right()

    if not game_over and not game_won:

        # Actualizar
        road.update()
        car.update()

        # Acumular tiempo para generar enemigos
        spawn_timer += dt

        # Actualizar la distancia recorrida
        distance += DISTANCE_PER_SECOND * (dt / 1000.0)

        # Consumir gasolina progresivamente
        fuel -= FUEL_CONSUMPTION * (dt / 1000.0)

        # Actualizar mensaje de gasolina
        if fuel_message_timer > 0:
            fuel_message_timer -= dt

        fuel = max(fuel, 0)

        if fuel <= 0:
            game_over = True

        # Comprobar si hemos alcanzado la meta
        if distance >= TARGET_DISTANCE:
            game_won = True

        # Calcular nivel de dificultad
        difficulty_level = int(distance)

        # Reducir tiempo entre enemigos
        spawn_interval = max(
            500,
            1200 - difficulty_level * 100
        )

        # Generar nuevos enemigos
        if spawn_timer >= spawn_interval:
            # Elegir un carril aleatorio
            lane = random.randint(0, 2)

            # Crear enemigo
            enemy = Enemy(lane)

            # Aumentar velocidad según la dificultad
            enemy.speed = 5 + difficulty_level

            enemies.append(enemy)

            spawn_timer = 0

        # Generar bidones de gasolina
        gas_spawn_timer += dt

        if gas_spawn_timer >= gas_spawn_interval:

            gas_can = Gas(enemies)

            if gas_can.valid:
                gas_cans.append(gas_can)

            gas_spawn_timer = 0

        # Actualizar enemigos
        for enemy in enemies:
            enemy.update()

        # Actualizar bidones de gasolina
        for gas_can in gas_cans:
            gas_can.update()

        # Comprobar colisiones
        for enemy in enemies:

            if car.rect.colliderect(enemy.rect):

                game_over = True
                break

        # Comprobar recogida de gasolina
        for gas_can in gas_cans[:]:

            if car.rect.colliderect(gas_can.rect):

                # Recuperar gasolina
                fuel = min(100, fuel + FUEL_CAN_AMOUNT)

                fuel_message_timer = 1500

                # Eliminar bidón recogido
                gas_cans.remove(gas_can)

        # Eliminar enemigos que han salido de la pantalla
        enemies = [enemy for enemy in enemies if enemy.y < WINDOW_HEIGHT]

    # Dibujar
    # Calcular progreso de la carrera
    progress = min(distance / TARGET_DISTANCE, 1.0)

    # Calcular kilómetros restantes
    remaining = max(TARGET_DISTANCE - distance, 0)

    road.draw(screen)
    car.draw(screen)
    for enemy in enemies:
        enemy.draw(screen)

    for gas_can in gas_cans:
        gas_can.draw(screen)

    # Mostrar la distancia recorrida
    # Crear panel del HUD
    hud = pygame.Surface((200, 115), pygame.SRCALPHA)

    pygame.draw.rect(
        hud,
        (0, 0, 0, 190),
        (0, 0, 200, 115),
        border_radius=10
    )


    # Mostrar porcentaje de gasolina
    fuel_text = small_font.render(
        f"FUEL: {fuel:.0f}%",
        True,
        WHITE
    )

    hud.blit(fuel_text, (12, 82))

    # Dibujar fondo de la barra de gasolina
    pygame.draw.rect(
        hud,
        (90, 90, 90),
        (100, 84, 88, 12),
        border_radius=6
    )

    # Calcular porcentaje de combustible
    fuel_progress = fuel / 100

    # Elegir color según combustible
    if fuel > 50:
        fuel_color = GREEN
    elif fuel > 20:
        fuel_color = YELLOW
    else:
        fuel_color = RED

    # Dibujar combustible disponible
    pygame.draw.rect(
        hud,
        fuel_color,
        (100, 84, int(88 * fuel_progress), 12),
        border_radius=6
    )

    # Mostrar distancia actual y meta
    distance_text = hud_font.render(
        f"{distance:.1f} / {TARGET_DISTANCE} km",
        True,
        WHITE
    )

    hud.blit(distance_text, (12, 8))

    # Mostrar distancia restante
    remaining_text = small_font.render(
        f"Faltan {remaining:.1f} km",
        True,
        WHITE
    )

    hud.blit(remaining_text, (12, 35))

    # Dibujar fondo de la barra
    pygame.draw.rect(
        hud,
        (90, 90, 90),
        (12, 61, 176, 12),
        border_radius=6
    )

    # Dibujar progreso
    pygame.draw.rect(
        hud,
        YELLOW,
        (12, 61, int(176 * progress), 12),
        border_radius=6
    )

    # Mostrar HUD arriba a la derecha
    screen.blit(hud, (WINDOW_WIDTH - 210, 10))

    # Mostrar mensaje al recoger gasolina
    if fuel_message_timer > 0:

        fuel_message = hud_font.render(
            f"+{FUEL_CAN_AMOUNT}% FUEL",
            True,
            YELLOW
        )

        fuel_rect = fuel_message.get_rect(
            center=(WINDOW_WIDTH // 2, 150)
        )

        screen.blit(fuel_message, fuel_rect)

    if game_over:
        message = font.render(
            "GAME OVER",
            True,
            WHITE
        )

        text_rect = message.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        screen.blit(
            message,
            text_rect
        )

        restart_message = font.render(
            "Press R to Restart",
            True,
            WHITE
        )

        restart_rect = restart_message.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 60)
        )

        screen.blit(
            restart_message,
            restart_rect
        )

    if game_won:
        message = font.render(
            "YOU WIN!",
            True,
            WHITE
        )

        text_rect = message.get_rect(
            center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        )

        screen.blit(
            message,
            text_rect
        )

    pygame.display.flip()


pygame.quit()