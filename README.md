# Contador interactivo con Pygame

**Biblioteca:** Pygame (Python)

## Descripción
Pygame es una biblioteca gratuita y de código abierto para crear aplicaciones multimedia y videojuegos 2D con Python. Está basada en SDL. Este proyecto es una aplicación mínima: un **contador** que muestra un número y lo incrementa cuando el usuario hace clic en un botón (o presiona la barra espaciadora).

## Instalación y ejecución
Requisitos: Python 3.6 o superior y pip.

```bash
git clone <URL-DE-TU-REPOSITORIO>
cd pygame-contador
pip install -r requirements.txt

python contador_basico.py   # versión con funciones
python contador_poo.py      # versión con clases (reto adicional)
```

Controles: clic izquierdo sobre el botón o barra espaciadora = sumar +1. En la versión básica, **R** reinicia; en la versión POO hay un botón "Reiniciar".

## Archivos
| Archivo | Contenido |
|---|---|
| `contador_basico.py` | Ejemplo mínimo con funciones |
| `contador_poo.py` | Mismo ejemplo con programación orientada a objetos |
| `requirements.txt` | Dependencias |
| `capturas/` | Evidencia de funcionamiento |

## Evidencia
| Estado inicial | Después de varios clics |
|---|---|
| ![inicial](capturas/basico_inicial.png) | ![clics](capturas/basico_tras_5_clics.png) |
| ![inicial poo](capturas/poo_inicial.png) | ![clics poo](capturas/poo_tras_7_clics.png) |

## Explicación del ejemplo (`contador_basico.py`)
1. **Ventana:** `pygame.display.set_mode((480, 320))` crea la pantalla principal y `set_caption` le pone título.
2. **Componentes gráficos:** el número se crea con `fuente.render(str(contador), ...)` y se pega en pantalla con `blit`; el botón es un `pygame.Rect` dibujado con `pygame.draw.rect`. Todo se dibuja en la función `dibujar()` y se muestra con `pygame.display.flip()`.
3. **Evento implementado:** `MOUSEBUTTONDOWN` (clic del mouse) y también `KEYDOWN` (teclado). Se detectan en el bucle principal con `for evento in pygame.event.get()`. Para saber si el clic fue sobre el botón se usa `boton.collidepoint(evento.pos)`.
4. **Función que responde:** `procesar_evento(evento, contador)`; recibe el evento y devuelve el nuevo valor del contador.
5. **Cambio en la interfaz:** en cada vuelta del bucle se vuelve a llamar a `dibujar(contador)`, que borra la pantalla y renderiza el número actualizado. Además, el botón cambia de color al pasar el mouse.

## Funcionamiento del evento
Pygame guarda las acciones del usuario en una cola de eventos. Cada fotograma el programa la lee con `pygame.event.get()`. Cada evento tiene un `type` (por ejemplo `MOUSEBUTTONDOWN`) y datos asociados (`pos`, `button`, `key`). Si el tipo es clic izquierdo (`button == 1`) y la posición está dentro del botón, el contador aumenta en 1.

## Reto adicional: Programación Orientada a Objetos
Pygame **sí permite** construir interfaces con clases y objetos (incluye clases propias como `Rect`, `Surface`, `Clock` y `sprite.Sprite`, y puedes definir las tuyas). Implementado en `contador_poo.py`:

| Clase | Responsabilidad |
|---|---|
| `Contador` | Modelo: almacena el valor y lo modifica (`incrementar`, `reiniciar`). No dibuja nada. |
| `Boton` | Se dibuja, detecta clics sobre sí mismo (`manejar_evento`) y ejecuta la acción que se le asignó. |
| `Aplicacion` | Crea la ventana, los objetos, reparte los eventos, dibuja y mantiene el bucle principal. |

## Pygame frente a Tkinter
| | Pygame | Tkinter |
|---|---|---|
| Ventajas | Animación y tiempo real, control total del dibujo, sonido integrado | Widgets listos (botones, cajas de texto, menús), incluido con Python |
| Limitaciones | No trae widgets: los botones se programan a mano | Poco adecuado para juegos y animaciones fluidas |
| Eventos | Cola que el programa consulta | Callbacks (`command=`, `bind`) |

## Fuentes consultadas
- Documentación oficial de Pygame: https://www.pygame.org/docs/
- Pygame, guía de inicio: https://www.pygame.org/wiki/GettingStarted
- Pygame, módulo `event`: https://www.pygame.org/docs/ref/event.html
- Pygame, `Rect`: https://www.pygame.org/docs/ref/rect.html
- Pygame, `draw`: https://www.pygame.org/docs/ref/draw.html
- Pygame en PyPI: https://pypi.org/project/pygame/
- Documentación de Tkinter (Python): https://docs.python.org/3/library/tkinter.html
