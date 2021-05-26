WINDOW_COLOR = (255, 255, 255)

# Поворот одной точки
def turn_one_point(xc, yc, x, y, phi):
    x -= xc
    y -= yc
    t = x
    x = x * cos(phi) - y * sin(phi)
    y = t * sin(phi) + y * cos(phi)
    x += xc
    y += yc
    return x, y

# Поворот любого числа точек
def turn(x_dict, y_dict, phi, r):
    phi = radians(phi)
    for i in range(1, len(x_dict)):
        x_dict[f'x{i}'], y_dict[f'y{i}'] = turn_one_point(x_dict['xc'], y_dict['yc'], x_dict[f'x{i}'], y_dict[f'y{i}'], phi)

    return x_dict, y_dict

import pygame

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption('АААААААААААААААААА')

run = True
while run:
    pygame.time.delay(50)
    
    circle(window, R, x_dict, y_dict, COLORS)
    turn(x_dict, y_dict, PHI, R)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WINDOW_COLOR)
    pygame.display.update()

pygame.quit()
