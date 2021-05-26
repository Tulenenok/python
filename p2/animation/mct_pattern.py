import pygame

pygame.init()
window = pygame.display.set_mode((300, 200))
pygame.display.set_caption('АААААААААААААААААА')

run = True
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
