import pygame
import random


def on_grid_random():
    x = random.randint(20, 600)
    y = random.randint(50, 630)
    return (x // 10 * 10, y // 10 * 10)


def colisao(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


pygame.init()
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3
stop = 4
# posição 0 = UP, posição 1 = DOWN, posição 2 = RIGHT, posição 3 = LEFT
CONTADOR = [1, 0, 2, 3]
TESTE = False


tela = pygame.display.set_mode((630, 660))
tela2 = pygame.display.set_caption('Cobra')
cor_cobra = pygame.Surface((10, 10))  # define o tamanho e cor da cobra
cor_cobra.fill(("blue"))
maca_posi = on_grid_random()
maca = pygame.Surface((10, 10))
maca.fill((255, 0, 0))
cobra = [(200, 200), (210, 200), (220, 200)]
direcao = stop
tempo = pygame.time.Clock()
while True:
    tempo.tick(15)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_UP:
                if CONTADOR[0] == 1:
                    direcao = UP
                CONTADOR[1] = 1
                CONTADOR[2] = 2
                CONTADOR[3] = 3
            if evento.key == pygame.K_DOWN:
                if CONTADOR[1] == 0:
                    direcao = DOWN
                CONTADOR[0] = 3
                CONTADOR[2] = 2
                CONTADOR[3] = 3
            if evento.key == pygame.K_LEFT:
                if CONTADOR[2] == 2:
                    direcao = LEFT
                CONTADOR[0] = 1
                CONTADOR[1] = 0
                CONTADOR[3] = 0
            if evento.key == pygame.K_RIGHT:
                if CONTADOR[3] == 3:
                    direcao = RIGHT
                CONTADOR[0] = 1
                CONTADOR[1] = 0
                CONTADOR[2] = 0

    if colisao(cobra[0], maca_posi):
        maca_posi = on_grid_random()
        cobra.append((0, 0))

    for i in range(len(cobra) - 1, 0, -1):
        cobra[i] = (cobra[i - 1][0], cobra[i - 1][1])

    if direcao == UP:
        cobra[0] = (cobra[0][0], cobra[0][1] - 10)
    if direcao == DOWN:
        cobra[0] = (cobra[0][0], cobra[0][1] + 10)
    if direcao == RIGHT:
        cobra[0] = (cobra[0][0] + 10, cobra[0][1])
    if direcao == LEFT:
        cobra[0] = (cobra[0][0] - 10, cobra[0][1])
    if direcao == stop:
        cobra[0] = (cobra[0][0], cobra[0][1])

    tela.fill("white")
    tela.blit(maca, maca_posi)

    # colisao da cobra com o proprio corpo
    y = 0
    for x in range(len(cobra)):
        if x >= 1:
            if (cobra[0] == cobra[x]) or (cobra[x] == cobra[0]):
                if direcao == RIGHT or direcao == LEFT or direcao == UP or direcao == DOWN:
                    TESTE = True

    # o if ta verificando se a colisao ocorreu mesmo e resetando
    if TESTE == True:
        cobra = [[200, 200], (210, 200), (220, 200)]
        maca_posi = on_grid_random()
        direcao = stop
        TESTE = False
        CONTADOR = [1, 0, 2, 3]

    for posi in cobra:
        tela.blit(cor_cobra, posi)

    if (cobra[0][0] >= 620) or (cobra[0][0] <= 10) or (cobra[0][1] >= 650) or (
            cobra[0][1] <= 40):
        cobra = [[200, 200], (210, 200), (220, 200)]
        direcao = stop
        maca_posi = on_grid_random()
        CONTADOR = [1, 0, 2, 3]

    for i in range(4):
        t_y = 30
        t_x = 0
        if i == 0:
            for j in range(66):
                pygame.draw.rect(tela, "black", [t_x, t_y, 10, 10], 2)
                t_y += 10

        if i == 1:
            for j in range(63):
                pygame.draw.rect(tela, "black", [t_x, t_y, 10, 10], 2)
                t_y = 30
                t_x += 10
        if i == 2:
            for j in range(63):
                pygame.draw.rect(tela, "black", [t_x, t_y, 10, 10], 2)
                t_y = 650
                t_x += 10
        if i == 3:
            for j in range(66):
                pygame.draw.rect(tela, "black", [t_x, t_y, 10, 10], 2)
                t_y += 10
                t_x = 620
    valorC = len(cobra) - 3
    txt = 'Pontos: ' + str(valorC)
    pygame.font.init()
    fonte = pygame.font.get_default_font()
    fontesys = pygame.font.SysFont(fonte, 30)
    txttela = fontesys.render(txt, 1, ("red"))
    tela.blit(txttela, (0, 10))
    pygame.display.flip()
    pygame.display.update()
