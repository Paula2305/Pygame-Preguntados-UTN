import pygame
import random
from constantes import *
from vistas import *
from funciones import*

pygame.init() # Se inicializa el programa
lista_preguntas = parse_csv("preguntas.csv")  
random.shuffle(lista_preguntas)

correr_programa = True
iniciar_juego = True

EVENTO_CAMBIAR_A_JUEGO = pygame.USEREVENT + 1
EVENTO_CAMBIAR_A_CONFIGURACION = pygame.USEREVENT + 2
EVENTO_CAMBIAR_A_PRINCIPAL = pygame.USEREVENT + 3

vista_actual = "principal"

while correr_programa:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            correr_programa = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            posicion_mouse = event.pos
            if vista_actual == "principal":
                boton_inicio,boton_config = vista_inicio()
                if boton_inicio.get_rect(topleft=(100, 220)).collidepoint(posicion_mouse):
                    pygame.event.post(pygame.event.Event(EVENTO_CAMBIAR_A_JUEGO))
                if boton_config.get_rect(topleft=(370,10)).collidepoint(posicion_mouse):
                    pygame.event.post(pygame.event.Event(EVENTO_CAMBIAR_A_CONFIGURACION))
            elif vista_actual == "vista_configuracion":
                boton_flecha_atras = vista_configuracion()
                if(boton_flecha_atras.get_rect(topleft=(370,10)).collidepoint(posicion_mouse)):
                   pygame.event.post(pygame.event.Event(EVENTO_CAMBIAR_A_PRINCIPAL))

        if event.type == EVENTO_CAMBIAR_A_JUEGO:
            vista_actual = "vista_juego"
        elif event.type == EVENTO_CAMBIAR_A_CONFIGURACION:
            vista_actual = "vista_configuracion"
        elif event.type == EVENTO_CAMBIAR_A_PRINCIPAL:
            vista_actual = "principal"

    if vista_actual == "principal":
        vista_inicio()
    elif vista_actual == "vista_juego":
        vista_juego(lista_preguntas)
    elif vista_actual == "vista_configuracion":
        vista_configuracion()

    pygame.display.flip()
    
pygame.quit()