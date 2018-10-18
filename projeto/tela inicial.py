import pygame
import sys
from pygame.locals import *

largura, altura = 800 , 500

relogio = pygame.time.Clock()
branco=(255,255,255)
preto=(0,0,0)
vermelho=(255,0,0)
verde=(0,255,0)
azul=(0,0,255)
tela = pygame.display.set_mode((largura,altura))
def tela_inicial(cor):
    baner = pygame.image.load('imagens/imagem.jpg')
    gato = pygame.image.load('imagens/gato.png')
    pygame.init()
    tela = pygame.display.set_mode((largura,altura))
    def texto(msg, cor, tam, x, y):
        font = pygame.font.SysFont(None, tam)
        texto1 = font.render(msg, True, cor)
        tela.blit(texto1, [x, y])
    while True:
        relogio.tick(60)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if (x >= 177 and y >= 302) and (x < 319 and y < 349 ):
                    break
                elif (x >= 500 and y >= 302) and (x <624  and y <349 ):
                    pygame.quit()
                    sys.exit()
                    quit()
                    
        tela.blit(baner,(0,0))
        tela.blit(gato,(70,50))
        texto('BEM VINDO AO SAD CAT SPACE', cor, 40, 250, 100 )
        pygame.draw.rect(tela,(0,0,0),[177,302,141,47])
        pygame.draw.rect(tela,(0,0,0),[500,302,125,47])
        texto("jogar(C)", cor, 50, 180, 307)
        texto("Sair(S)", cor, 50, 505, 307)
        pygame.display.update()
        
        
        
    def texto(msg, cor, tam, x, y):
        font = pygame.font.SysFont(None, tam)
        texto1 = font.render(msg, True, cor)
        tela.blit(texto1, [x, y])
        
tela_inicial(vermelho)
