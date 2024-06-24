import os
import pygame
from constantes import *

def parse_csv(nombre_archivo:str): 
    lista_elementos = [] 
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo,"r", encoding= "utf-8") as archivo:
            primer_linea = archivo.readline()
            primer_linea = primer_linea.replace("\n","")
            lista_claves = primer_linea.split(",")
            for linea in archivo:
                linea_aux = linea.replace("\n","")
                lista_valores = linea_aux.split(",")
                diccionario_aux = {} 
                for i in range(len(lista_claves)):
                    diccionario_aux[lista_claves[i]] = lista_valores[i]

                
                lista_elementos.append(diccionario_aux)

        
        return lista_elementos
    
def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, False, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def crear_carta_pregunta(pregunta): #-> Carta pregunta
    '''Param pregunta, retorna la carta de la pregunta'''
    carta_pregunta = {"superficie":pygame.Surface(TAMANIO_PREGUNTA),"rectangulo":pygame.Rect(0,0,0,0)}
    carta_pregunta['superficie'].fill(COLOR_ROJO) # Le asigno un color a esa superficie

    fuente_pregunta = pygame.font.SysFont("Arial Narrow",30)
    blit_text(carta_pregunta['superficie'],pregunta,(20,20),fuente_pregunta)

    return carta_pregunta

def crear_carta_respuesta(respuesta):#-> Carta respuesta
    '''Param respuestas, retorna la carta de la respuesta'''
    carta_respuesta = {"superficie":pygame.Surface(TAMANIO_RESPUESTA),"rectangulo":pygame.Rect(0,0,0,0)}
    carta_respuesta['superficie'].fill(COLOR_AZUL)

    fuente_respuesta = pygame.font.SysFont("Arial Narrow",20)
    blit_text(carta_respuesta['superficie'],respuesta,(20,20),fuente_respuesta,COLOR_NEGRO)

    return carta_respuesta

def obtener_pregunta():
    pass
