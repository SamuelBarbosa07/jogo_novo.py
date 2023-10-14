import pygame
import sys

def animacao_personagem():
    global jogador_index
    jogador_index += 0.11
    if jogador_index > len(jogador_parado_superficies) - 1:
        jogador_index = 0
    
    janela.blit(jogador_parado_superficies[int(jogador_index)], jogador_retangulo.topleft)

# Inicializa o Pygame
pygame.init()

# Defina as dimensões da janela
largura = 1530
altura = 800

# Inicialize a janela
janela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Zombies")

# Carrega a imagem de fundo
fundo_imagem = pygame.image.load("cenarios.py/novos/Battleground4/Bright/Battleground4.png").convert()
fundo_imagem = pygame.transform.scale(fundo_imagem, (largura, altura))

# Carrega as imagens do personagem
jogador_index = 0
jogador_parado_superficies = []

# Carrega o Personagem parado
for imagem in range(1, 7):
    img = pygame.image.load(f'personagem.py/parado1/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (300, 300))
    jogador_parado_superficies.append(img)

for imagem in range(1, 6):
    img = pygame.image.load(f'personagem.py/parado2/tile{imagem}.png').convert_alpha()
    img = pygame.transform.scale(img, (300, 300))
    jogador_parado_superficies.append(img)

# Velocidade do movimento do personagem
movimento_personagem = 5

# Posição inicial do jogador
jogador_x = largura // 2  # Posição X inicial do jogador
jogador_y = altura - 400   # Posição Y inicial do jogador
jogador_retangulo = pygame.Rect(jogador_x, jogador_y, 300, 400)

relogio = pygame.time.Clock()

# Loop principal do jogo
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Detecta as teclas de seta pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        jogador_x -= movimento_personagem
    if keys[pygame.K_RIGHT]:
        jogador_x += movimento_personagem

    # Desenha a imagem de fundo na posição
    janela.blit(fundo_imagem, (0, 0))

    # Atualiza a posição do jogador
    jogador_retangulo.topleft = (jogador_x, jogador_y)

  
    if movimento_personagem != 0:
        animacao_personagem()
        for imagem in range(1, 8):
            img = pygame.image.load(f'personagem.py/andando/tile{imagem}.png').convert_alpha()
            img = pygame.transform.scale(img, (300, 300))
            jogador_parado_superficies.append(img)
    



    # Atualiza a tela
    pygame.display.update()
    relogio.tick(60)
