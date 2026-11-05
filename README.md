## Descripción
Pygame es una biblioteca gratuita y de código abierto para crear aplicaciones multimedia y videojuegos 2D con Python. Está basada en SDL. ideal tanto para principiantes que quieren aprender programación orientada a objetos y lógica de juegos, como para desarrolladores experimentados que desean crear prototipos rápidos. 
## Qué permite desarrollar? 
•	Videojuegos 2D: Desde simples juegos de arcade, plataformas y rompecabezas hasta prototipos más complejos. 
•	Aplicaciones Multimedia: Demos interactivos, visualizaciones de algoritmos, simulaciones físicas y arte generativo. 
•	Herramientas Educativas: Programas interactivos para enseñanza, quizzes y visualizaciones de datos en tiempo real.
•	Prototipos de Juegos: Herramientas rápidas para probar mecánicas de juego antes de migrar a motores más pesados como Unity.

## Instalación y ejecución
Como esta librería no viene incluida en el lenguaje a diferencia de otras, La instalación de esta librería se puede realizar mediante comandos en la terminal, eso sí, teniendo en cuenta un par de requisitos previos y es tener la versión de Python 3.8 o superior a esa, y también el gestor de paquetes pip.
Despues de eso, abrimos la terminal y ejecutamos este comando: pip install pygame (en algunos dispositivos será necesario escribir pip3 install pygame) e inmediatamente descargará la librería, para comprobarlo escribiremos esta vez: Python -m pygame –version y nos va a imprimir algo como esto: pygame 2.x.x

## ¿Cuáles son sus principales componentes o elementos gráficos?
Los principales componentes gráficos de Pygame se basan en el objeto Surface, que actúa como un lienzo donde se renderizan las imágenes, formas geométricas y texto antes de mostrarse en pantalla. 
Superficies (Surface): Son los objetos fundamentales que representan áreas rectangulares de memoria para dibujar, ya sea la ventana del juego, fondos o sprites individuales. 
Módulo de dibujo (draw): Permite renderizar formas básicas como rectángulos, círculos, elipses, líneas y polígonos directamente sobre las superficies. 
Gestión de imágenes (image): Facilita la carga, guardado y transferencia de archivos de imagen (como PNG o JPG) para convertirlos en superficies utilizables.
Renderizado de texto (font): Convierte cadenas de texto en superficies de imagen utilizando fuentes TrueType, permitiendo su visualización mediante el método blit().
Sprites: Objetos de alto nivel (clase pygame.sprite.Sprite) que agrupan imágenes y datos de posición para simplificar la gestión de objetos móviles, animaciones y detección de colisiones.
Transformaciones (transform): Ofrece métodos para modificar superficies gráficas, como redimensionar, rotar o voltear imágenes y formas existentes. 

## ¿Cómo maneja los eventos del usuario, por ejemplo, los clics del mouse o las pulsaciones del teclado?
Pygame maneja la entrada del usuario mediante un bucle de eventos que procesa una cola de acciones como clics y pulsaciones de teclas. El método central es pygame.event.get(), que devuelve una lista de objetos evento; cada uno tiene un atributo type que indica la acción (ej. KEYDOWN, MOUSEBUTTONDOWN, QUIT)

## Pygame frente a Tkinter: Ventajas y Limitaciones
| | Pygame | Tkinter |
|---|---|---|
| Ventajas | Animación y tiempo real, control total del dibujo, sonido integrado | Widgets listos (botones, cajas de texto, menús), incluido con Python |
| Limitaciones | No trae widgets: los botones se programan a mano | Poco adecuado para juegos y animaciones fluidas |
| Eventos | Cola que el programa consulta | Callbacks (`command=`, `bind`) |

## Explicación del funcionamiento
Para nosotros empezar a crear interfaces graficas mediante Pygame, creamos los elementos basicos como se realizó en clase usando Tkinter.

Para crear ventanas: pygame.display.set_mode crea la pantalla principal con ancho y alto, y display.set_caption le da el título

Para demás componentes graficos, establecemos la fuente con pygame.font.Sysfont 
creacion del boton: mediante pygame.Rect este define forma, tamaño y posicion, luego se usa pygame.draw.rect que dibuja el visual del botón 

## Que evento se implementó?
Aqui utilice el MOSEBUTTONDOWN que detecta cuando el usuario presiona un boton por medio del mouse y en el codigo es gracias a 
if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton.collidepoint(evento.pos):
                cambiar_mensaje()

A su vez este evento responde a la funcion de cambiar el mensaje cuando se haga un clic en el boton, reescribiendo el texto anterior y se modifica lo que aparece en la ventana despues de dicho click sobre el boton azul, el programa detecta el evento y se ejecuta en la función

## Reto adicional: Programación Orientada a Objetos
Pygame **sí permite** construir interfaces con clases y objetos (incluye clases propias como `Rect`, `Surface`, `Clock` y `sprite.Sprite`, y puedes definir las tuyas).

## Fuentes consultadas
https://es.wikipedia.org/wiki/Pygame
https://librerialatijera.com.ar/libreria-pygame/
https://ayudayformacion.com/python/pygame/instalar-configurar-pygame/

