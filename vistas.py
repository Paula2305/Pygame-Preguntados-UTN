import pygame 
import datetime
from constantes import *
from funciones import *
import pygame_textinput

pantalla = pygame.display.set_mode(TAMANIO_VENTANA)
pygame.display.set_caption("Juego PREGUNTADOS")

def vista_inicio():
    pantalla.fill(COLOR_FONDO_VISTA_VIOLETA)

    boton_inicio = pygame.Surface((200, 75), pygame.SRCALPHA)  # Superficie del botón de inicio con transparencia
    pygame.draw.rect(boton_inicio, COLOR_BLANCO, boton_inicio.get_rect(), border_radius = 20)

    boton_config = pygame.transform.scale(pygame.image.load("img/config.png").convert_alpha(),(30,30))

    font = pygame.font.SysFont("Arial Narrow",50)
    texto = font.render("Iniciar", True, COLOR_NEGRO)

    boton_inicio.blit(texto,(45,25))

    pantalla.blit(boton_inicio,(100,220)) # eje x, eje y
    pantalla.blit(boton_config,(360,10))

    return boton_inicio,boton_config

def vista_juego(lista_preguntas:list):
    fecha_actual = datetime.datetime.today().strftime("%d-%m-%Y")
    vidas = 3
    puntuacion = 0
    indice_pregunta = 0  # Índice para rastrear la pregunta actual
   
    while vidas > 0 and indice_pregunta < len(lista_preguntas):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                posicion_mouse = event.pos
                # Comprobamos si alguna respuesta fue clicada
                if respuesta_rects[0].collidepoint(posicion_mouse):
                    if respuesta_correcta == 1:
                        puntuacion += 50
                        print("Respuesta correcta! +50 puntos")
                    else:
                        vidas -= 1
                        puntuacion -= 50
                        print("Respuesta incorrecta! -50 puntos")
                    indice_pregunta += 1  # Pasar a la siguiente pregunta
                elif respuesta_rects[1].collidepoint(posicion_mouse):
                    if respuesta_correcta == 2:
                        puntuacion += 50
                        print("Respuesta correcta! +50 puntos")
                    else:
                        vidas -= 1
                        puntuacion -= 50
                        print("Respuesta incorrecta! -50 puntos")
                    indice_pregunta += 1  # Pasar a la siguiente pregunta
                elif respuesta_rects[2].collidepoint(posicion_mouse):
                    if respuesta_correcta == 3:
                        puntuacion += 50
                        print("Respuesta correcta! +50 puntos")
                    else:
                        vidas -= 1
                        puntuacion -= 50
                        print("Respuesta incorrecta! -50 puntos")
                    indice_pregunta += 1  # Pasar a la siguiente pregunta       

        if indice_pregunta < len(lista_preguntas):
            pregunta = lista_preguntas[indice_pregunta]
            carta_pregunta = crear_carta_pregunta(pregunta['pregunta'])
            carta_respuesta_1 = crear_carta_respuesta(pregunta['respuesta_1'])
            carta_respuesta_2 = crear_carta_respuesta(pregunta['respuesta_2'])
            carta_respuesta_3 = crear_carta_respuesta(pregunta['respuesta_3'])
            respuesta_correcta = int(pregunta['respuesta_correcta'])

            # Limpiar la pantalla antes de dibujar
            pantalla.fill(COLOR_BLANCO)
            
            #VIDAS
            corazon_vida = pygame.transform.scale(pygame.image.load("img/vidas.png").convert_alpha(),(40,40))
            eje_x = 5
            for vida in range(vidas):
                pantalla.blit(corazon_vida,(eje_x,5))
                eje_x += 30
            # Dibujar la pregunta y las respuestas
            pantalla.blit(carta_pregunta['superficie'], (25, 50))
            respuesta_rects = [
                pantalla.blit(carta_respuesta_1['superficie'], (75, 215)),
                pantalla.blit(carta_respuesta_2['superficie'], (75, 285)),
                pantalla.blit(carta_respuesta_3['superficie'], (75, 355))
            ]
            
            pygame.display.flip()

    print("Juego terminado")
    print("Puntuación final:", puntuacion)
    # vista_pedir_nombre() 
    # vista_ranking(nombre_user,puntuacion,fecha_actual)

# def vista_pedir_nombre():
#     pantalla.fill(COLOR_NEGRO)
#     textinput = pygame_textinput.TextInputVisualizer()
#     clock = pygame.time.Clock()
#     user_text = ""  # Variable para almacenar el texto ingresado
#     events = pygame.event.get()

#     # Feed it with events every frame
#     textinput.update(events)
#     # Blit its surface onto the screen
#     pantalla.blit(textinput.surface, (10, 10))
#     for event in events:
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             exit()
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RETURN:
#                 # Cuando se presiona Enter, guardar el texto ingresado
#                 user_text = textinput.get_text()  # Obtener el texto ingresado
#                 print("Texto ingresado:", user_text)  # Solo para propósitos de demostración

#     pygame.display.update()
#     clock.tick(30)            

def vista_configuracion():
    pantalla.fill(COLOR_FONDO_VISTA_VIOLETA)

    boton_flecha_atras = pygame.transform.scale(pygame.image.load("img/atras.png").convert_alpha(),(30,30))
    pantalla.blit(boton_flecha_atras,(10,20))

    pantalla.fill(COLOR_FONDO_VISTA_VIOLETA)

    boton_volumen = pygame.Surface((200, 75), pygame.SRCALPHA)
    pygame.draw.rect(boton_volumen, COLOR_BLANCO, boton_volumen.get_rect(), border_radius = 20)

    rectangulo = pygame.Surface((350,150), pygame.SRCALPHA)
    pygame.draw.rect(rectangulo,COLOR_BLANCO, rectangulo.get_rect())

    font = pygame.font.SysFont("Arial Narrow",50)
    texto = font.render("Música", True, COLOR_NEGRO)

    boton_volumen.blit(texto,(45,25))

    pantalla.blit(boton_volumen,(100,220))
    pantalla.blit(boton_flecha_atras,(360,10))

    return boton_flecha_atras
    