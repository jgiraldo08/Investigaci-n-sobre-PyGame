import pygame

# Inicializar Pygame
pygame.init()

# Crear ventana
ventana = pygame.display.set_mode((500, 300))
pygame.display.set_caption("Mi primera ventana")

# Crear fuente
fuente = pygame.font.SysFont("Arial", 30)

# Mensaje inicial
mensaje = "Hola, bienvenido"

# Crear botón
boton = pygame.Rect(150, 180, 200, 50)

# Función para cambiar el mensaje
def cambiar_mensaje():
    global mensaje
    mensaje = "¡Hiciste clic!"

# Mantener abierta la ventana
run = True

while run:

    for evento in pygame.event.get():

        # Cerrar ventana
        if evento.type == pygame.QUIT:
            run = False
        # Detectar clic
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(evento.pos):
                cambiar_mensaje()
    # Fondo blanco
    ventana.fill((255, 255, 255))

    # Mostrar mensaje
    texto = fuente.render(mensaje, True, (0, 0, 0))
    ventana.blit(texto, (130, 80))

    # Dibujar botón azul
    pygame.draw.rect(ventana, (0, 100, 255), boton)

    # Mostrar texto del botón
    texto_boton = fuente.render("Presiona Aquí", True, (255, 255, 255))
    ventana.blit(texto_boton, (165, 190))

    # Actualizar pantalla
    pygame.display.flip()

# Cerrar Pygame
pygame.quit()