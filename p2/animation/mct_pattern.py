WINDOW_COLOR = (255, 255, 255)

import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('АААААААААААААААААА')

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WINDOW_COLOR)
    pygame.display.update()

pygame.quit()
