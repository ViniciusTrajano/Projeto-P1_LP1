import pygame
from random import randrange

def texto(msg, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(msg, True, cor)
    tela.blit(texto1, [x, y])
    
def jogo ():
    #Palheta Cores:
    azul = (48,154,233)
    amarelo = (248,237,41)
    verde = (44,213,19)
    vermelho = (255,13,13)
    preto = (0,0,0)
    branco = (255,255,255)

    #Definições(Variáveis)
    largura = 640
    altura = 480
    
    posx, posy = 285, 380
    alien_x = randrange(0,largura - 60,10)
    alien_y = -10
    
    relogio = pygame.time.Clock()
    x = 200

    pygame.init()
    tela = pygame.display.set_mode((largura,altura))
    #superfícies
    sup_1 = pygame.Surface((620,460))
    sup_1.fill(vermelho)
    sup_2 = pygame.Surface((620,50))
    sup_2.fill(preto)
    element = pygame.transform.scale(pygame.image.load("imagens/cat_icon.png"), (50, 50))
    element_rect = element.get_rect()   
    pygame.display.set_caption("Jogo Desconhecido - Iago FDP")
    sair = False
    
    while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
        if posy > 480:
            posy = posy - altura
        if posx > 640:
            posx = posx - largura
        if posy < 0:
            posy += altura
        if posx < 0:
            posx += largura
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            posy -= 5
        elif keys[pygame.K_s]:
            posy += 5
        elif keys[pygame.K_a]:
            posx -= 5
        elif keys[pygame.K_d]:
            posx += 5
        relogio.tick(65)
        tela.fill(branco)
        tela.blit(sup_1,[10,10])
        tela.blit(sup_2,[10,430])
        tela.blit(element, (posx, posy))
        #if posx != 285 or posy != 380:

        pygame.display.update()
        
    
    pygame.quit()
    


jogo()
quit()


keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
    posx -= 20

