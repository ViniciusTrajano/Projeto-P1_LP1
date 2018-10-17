import pygame
branco = (255,255,255)
azul_burguesa = (0,127,255)
verde = (0,205,0)

try:
    pygame.init()
except:
    print('Algo deu errado')
larg = 640
alt = 480
pygame.display.set_mode((larg,alt))
pygame.display.set_caption('Testando a Cobrinha')

#Definições do loop:
saida = True

#loop da tela:
while saida:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            saida = False
        print(event)
    pygame.display.update()
    
    pygame.event.EventType

pygame.quit()
quit()
