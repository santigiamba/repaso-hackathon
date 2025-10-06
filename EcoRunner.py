import pygame
import random

pygame.init()
pantalla = pygame.display.set_mode((800, 400))
pygame.display.set_caption("EcoRunner - Nivel 3")
reloj = pygame.time.Clock()
fuente = pygame.font.Font(None, 40)

jugador = pygame.Rect(100, 300, 40, 40)
salto = False
velocidad_salto = 0
obstaculos = []
puntos = 0
nivel = 1
velocidad_juego = 8

def mostrar_mensaje(texto, tamano=60):
    font = pygame.font.Font(None, tamano)
    render = font.render(texto, True, (0, 100, 0))
    rect = render.get_rect(center=(400, 200))
    pantalla.blit(render, rect)
    pygame.display.flip()

def pantalla_inicio():
    pantalla.fill((200, 255, 200))
    mostrar_mensaje("Presiona ESPACIO para comenzar")
    esperando = True
    while esperando:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                esperando = False
        reloj.tick(30)

def pantalla_final():
    pantalla.fill((200, 255, 200))
    mostrar_mensaje("🌿 ¡Felicidades, EcoRunner!")
    pygame.time.wait(3000)

pantalla_inicio()

corriendo = True
perdio = False
while corriendo:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            corriendo = False
        if e.type == pygame.KEYDOWN and not salto:
            salto = True
            velocidad_salto = -15

    if salto:
        jugador.y += velocidad_salto
        velocidad_salto += 1
    if jugador.y >= 300:
        jugador.y = 300
        salto = False

    if random.randint(1, 40) == 1:
        obstaculos.append(pygame.Rect(800, 320, 20, 30))

    for o in list(obstaculos):
        o.x -= velocidad_juego
        if o.x < 0:
            obstaculos.remove(o)
            puntos += 1
            if puntos % 50 == 0:
                nivel += 1
                velocidad_juego += 2

    for o in obstaculos:
        if jugador.colliderect(o):
            mostrar_mensaje("💥 GAME OVER – Intenta otra vez", 50)
            pygame.time.wait(2000)
            corriendo = False
            perdio = True

    pantalla.fill((200, 255, 200))
    pygame.draw.rect(pantalla, (0, 200, 0), jugador)
    for o in obstaculos:
        pygame.draw.rect(pantalla, (80, 80, 80), o)

    texto = fuente.render(f"Puntos: {puntos}  Nivel: {nivel}", True, (0, 0, 0))
    pantalla.blit(texto, (10, 10))

    pygame.display.flip()
    reloj.tick(30)

if not perdio:
    pantalla_final()
pygame.quit()
