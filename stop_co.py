import pygame
import random

WIDTH, HEIGHT = 600, 400

pygame.init()
pantalla = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stop CO Challenge - Nivel 2")
fuente = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 72)
reloj = pygame.time.Clock()

auto = pygame.Rect(300, 350, 50, 30)
humo = pygame.Rect(random.randint(0, WIDTH - 20), 0, 20, 20)
puntos = 0
humo_speed = 5
auto_speed = 5

corriendo = True
nivel_completado = False

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    if not nivel_completado:
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            auto.x -= auto_speed
        if teclas[pygame.K_RIGHT]:
            auto.x += auto_speed

        if auto.left < 0:
            auto.left = 0
        if auto.right > WIDTH:
            auto.right = WIDTH

        humo.y += humo_speed
        if humo.y > HEIGHT:
            humo.y = 0
            humo.x = random.randint(0, WIDTH - humo.width)
            puntos += 1

        if auto.colliderect(humo):
            print("💨 ¡Contaminación detectada!")
            puntos = 0
            humo.y = 0
            humo.x = random.randint(0, WIDTH - humo.width)

    pantalla.fill((180, 220, 255))
    pygame.draw.rect(pantalla, (0, 255, 0), auto)
    pygame.draw.rect(pantalla, (80, 80, 80), humo)
    texto = fuente.render(f"Puntos: {puntos}", True, (0, 0, 0))
    pantalla.blit(texto, (10, 10))
    pygame.display.flip()

    if puntos >= 10 and not nivel_completado:
        nivel_completado = True
        start = pygame.time.get_ticks()
        while pygame.time.get_ticks() - start < 3000 and corriendo:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    corriendo = False
            mensaje = big_font.render("¡Nivel completado!", True, (255, 255, 255))
            rect = mensaje.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            pantalla.blit(mensaje, rect)
            pygame.display.flip()
            reloj.tick(30)
        corriendo = False

    reloj.tick(30)

pygame.quit()

