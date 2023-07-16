#Importar bibliotecas
import pygame
import time
from pygame.locals import *
from sys import exit
from random import randint

#Iniciar PyGame
pygame.init()

#Estabelecer tamanho da tela
largura = 1280
altura = 720

#Posição dos elementos
x_cobra = largura / 2
y_cobra = altura / 2

x_controle = 20
y_controle = 0

x_maca = randint(1,largura-10)
y_maca = randint(1,altura-10)

lista_cobra = []
comprimentoInicial = 30

#Criação de fonte
fonte = pygame.font.SysFont('helvetica',40,False,False)

morreu = False

#Configurações de jogo
tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption('Playgame Test')
relogio = pygame.time.Clock()

#Estabelecer pontuação
pontos = 0

def aumentarCobra(lista_cobra):
    for item in lista_cobra :
        pygame.draw.rect(tela,(255,255,255),(item[0],item[1],20,20))

#Criar Loop
while True :
    #FPS DO JOGO
    relogio.tick(60)
    #Complemento de tela
    tela.fill((0,0,0))

    #Desenvolver texto em tela
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    #Apertar tecla
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_a :
                if x_controle > 0 :
                    pass
                else:
                    x_controle = -5
                    y_controle = 0
            if event.key == K_w :
                if y_controle > 0 :
                    pass
                else:
                    y_controle = -5
                    x_controle = 0
            if event.key == K_s :
                if y_controle < 0 :
                    pass
                else:
                    x_controle = 0
                    y_controle = 5
            if event.key == K_d :
                if x_controle < 0 :
                    pass
                else:
                    x_controle = 5
                    y_controle = 0
            if event.key == K_ESCAPE :
                pygame.quit()
                exit()
        if event.type == QUIT:
            pygame.quit()
            exit()


    #Botao pressionado
    x_cobra += x_controle
    y_cobra += y_controle
    if x_cobra > largura :
        x_cobra = 0
    if x_cobra < 0 :
        x_cobra = largura
    if y_cobra < 0 :
        y_cobra = altura
    if y_cobra > altura :
        y_cobra = 0
    #Criar formas
    cobra = pygame.draw.rect(tela, (255,255,255) , (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255,255,255) , (x_maca, y_maca, 20, 20))

    #Formula de colisão
    if cobra.colliderect(maca):
        pontos += 1
        x_maca = randint(1,largura-10)
        y_maca = randint(1,altura-10)
        comprimentoInicial += 1


    #Movimentação objetos
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)

    if len(lista_cobra) > 3 :
        cobra_restante = [item for item in lista_cobra]
        cobra_restante.pop(-1)
        if lista_cabeca in cobra_restante:
            morreu = True
            print("morreu fi")
            pygame.quit()
            exit()


    if len(lista_cobra) > comprimentoInicial:
        del lista_cobra[0]

    aumentarCobra(lista_cobra)
    #Desenhar texto
    tela.blit(texto_formatado,(largura - texto_formatado.get_width() - 10, 10))

    #update constante
    pygame.display.update()

