import pygame
import sys
from pygame.locals import *

largura = 800
altura = 500
## posx, posy = 285, 380
relogio = pygame.time.Clock()

#cores
azul = (48,154,233)
amarelo = (248,237,41)
verde = (44,213,19)
vermelho = (255,13,13)
preto = (0,0,0)
branco = (255,255,255)


#Telas teste
##sup_1 = pygame.Surface((620,460))
##sup_1.fill(vermelho)
##sup_2 = pygame.Surface((620,50))
##sup_2.fill(preto)
class alien(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load ('imagens/alien.png')
        self.image2 = pygame.image.load ('imagens/alien.png')
        self.image3 = pygame.image.load ('imagens/alien.png')
        self.image4 = pygame.image.load ('imagens/alien.png')

        self.lista_imagens = [self.image1,self.image2,self.image3,self.image4]
        self.pos_imagem = 0
        self.image_alien = self.lista_imagens[self.pos_imagem]
        
        self.rect = self.image_alien.get_rect()

        self.listaDisparo = []
        self.vel_alien = 20
        self.rect.top = posy
        self.rect.left = posx

        self.configtime = 1
        

    def comportamento(self,tempo):
        if self.configtime == tempo:
            self.pos_imagem += 1
            self.confitime += 1 
        if self.pos_imagem > len(self.lista_imagens)-1:
            self.pos_imagem = 0
    def colocar(self,sp):
        self.image_alien = self.lista_imagens[self.pos_imagem]
        
        sp.blit(self.image1,self.rect)

class projetil(pygame.sprite.Sprite):
    def __init__(self,posx,posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemProjetil = pygame.image.load ('imagens/rato.png')

        self.rect = self.ImagemProjetil.get_rect()
        self.vel_proj = 4
        self.rect.top = posy
        self.rect.left = posx

    def caminho(self):
        self.rect.top = self.rect.top - self.vel_proj
    def colocar_tiros(self,sp2):
        
        sp2.blit(self.ImagemProjetil,self.rect)
        
                                                     
class nave(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.transform.scale(pygame.image.load ('imagens/cat_icon.png'),(50,50))
        

        self.rect = self.ImagemNave.get_rect()
        self.rect.centerx = largura/2
        self.rect.centery = altura - 50

        self.listaDisparo = []
        self.vida = True
        self.velocidade = 8
        
    def movimento(self):
        if self.vida == True:
            if self.rect.left <= 0:
                self.rect.left = 0
            elif self.rect.right >= 800:
                self.rect.right = 800
    def disparo(self,x,y):
        rato_bala = projetil(x,y)
        self.listaDisparo.append(rato_bala)
    def colocar(self,sp):
        sp.blit(self.ImagemNave,self.rect)

def jogo():
    pygame.init()
    tela = pygame.display.set_mode((largura,altura))
    pygame.display.set_caption("SAD CAT SPACE  - ADVENTURE")

    jogador = nave()
    fundo_tela = pygame.image.load('imagens/space.jpg')
    jogando = True

    inimigo = alien(100,100)
    rato = projetil(largura/2, altura - 60)
    while True:
        relogio.tick(60)
        tempo = pygame.time.get_ticks()/1000
        rato.caminho()
        jogador.movimento()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                x,y = jogador.rect.center
                jogador.disparo(x,y)
                
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            jogador.rect.left -= jogador.velocidade
        elif keys[pygame.K_d]:
            jogador.rect.left += jogador.velocidade
             
        tela.blit(fundo_tela,(0,0))
        jogador.colocar(tela)
        inimigo.colocar(tela)
        inimigo.comportamento(tempo)
        #rato.colocar_tiros(tela) 
        if len(jogador.listaDisparo)> 0:
            for x in jogador.listaDisparo:
                x.colocar_tiros(tela)
                x.caminho()
                if x.rect.top <-10:
                    jogador.listaDisparo.remove(x)
        pygame.display.update()
jogo()
