import pygame
import random

# iniciando o pygame
pygame.init()

# definir as dimensões da tela em pixels
screen_width, screen_height = 800, 600
# cria a janela para o jogo com as dimensões especificadas
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Spaceship fallen")

# definir as cores usadas em rgb
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# variáveis do jogador
player_width = 60
player_height = 40
player_speed = 10

# dimensões do sprite
spr_width = 60
spr_height = 40

# classe para o player
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("sprite.png").convert_alpha()  # carrega o sprite
        self.image = pygame.transform.scale(self.image,(spr_width, spr_height))
        self.rect = self.image.get_rect(center=(screen_width // 2, screen_height - self.image.get_height() - 10))  


# variáveis do item
obj_width = 30
obj_height = 30
obj_x = random.randint(0, screen_width - obj_width)  # random spawn
obj_y = -obj_height
obj_speed = 2  # randomizer speed 

# score
score = 0

# var de controle do jogo
playing = True  # quando falso o jogo para 
clock = pygame.time.Clock()

# criar o jogador
player = Player()

# game looping, mantem em execução enquanto playing for true
while playing:
    screen.fill(black)

    # events check
    for event in pygame.event.get():  # verifica eventos no jogo, como o fechamento da janela 
        if event.type == pygame.QUIT:
            playing = False

    # movimentação do jogador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.rect.x > 0:
        player.rect.x -= player_speed
    if keys[pygame.K_RIGHT] and player.rect.x < screen_width - player_width:
        player.rect.x += player_speed
    if keys[pygame.K_UP] and player.rect.y > 0:
        player.rect.y -= player_speed
    if keys[pygame.K_DOWN] and player.rect.y < screen_height - player_height:
        player.rect.y += player_speed

    # posição do objeto
    obj_y += obj_speed  # faz com que o objeto caia em vertical

    # posição do objeto reset
    if obj_y > screen_height:
        obj_y = -obj_height
        obj_x = random.randint(0, screen_width - obj_width)

    # colisão 
    if (player.rect.x < obj_x + obj_width and 
        player.rect.x + player_width > obj_x and 
        player.rect.y < obj_y + obj_height and 
        player.rect.y + player_height > obj_y):
        score += 1
        obj_y = -obj_height
        obj_x = random.randint(0, screen_width - obj_width)
        obj_speed += 1

    # desenhar jogador
    screen.blit(player.image, player.rect)

    # desenhar objeto
    pygame.draw.rect(screen, white, (obj_x, obj_y, obj_width, obj_height))

    # mostrar score
    font = pygame.font.Font(None, 30)
    text = font.render("score: " + str(score), True, white)
    screen.blit(text, (10, 10))

    # tela e fps
    pygame.display.flip()
    clock.tick(30)

# fechar jogo 
pygame.quit()