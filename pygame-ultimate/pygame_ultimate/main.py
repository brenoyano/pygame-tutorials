import pygame
from sys import exit


pygame.init()

game_conf = {
    'screen_conf_width': 800,
    'screen_conf_height': 400,
    'title': 'Runner',
    'fps': 60
}
screen = pygame.display.set_mode((
    game_conf['screen_conf_width'],
    game_conf['screen_conf_height']
))

game_title =  pygame.display.set_caption(game_conf['title'])

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
    clock.tick(game_conf['fps'])