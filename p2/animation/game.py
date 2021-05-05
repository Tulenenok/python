import pygame
import random

class Wheel:
    def __init__(self, cx, cy, r, speed=5, color1='#523637', color2=(0, 0, 0)):
        self.__cx = cx
        self.__cy = cy
        self.__r = r
        self.__speed = speed

        self.__color1 = color1  # color1 - цвет колеса
        self.__color2 = color2  # color2 - цвет оси

        self.__left_x_1, self.__left_y_1 = self.__cx - self.__r, self.__cy
        self.__right_x_1, self.__right_y_1 = self.__cx + self.__r, self.__cy

        self.__left_x_2, self.__left_y_2 = self.__cx, self.__cy - self.__r
        self.__right_x_2, self.__right_y_2 = self.__cx, self.__cy + self.__r

    def create(self):
        pygame.draw.circle(window, self.__color1, (self.__cx, self.__cy), self.__r)

        t = self.rotateLine(self.__left_x_1, self.__left_y_1, self.__right_x_1, self.__right_y_1)
        self.__left_x_1, self.__left_y_1, self.__right_x_1, self.__right_y_1 = t

        t = self.rotateLine(self.__left_x_2, self.__left_y_2, self.__right_x_2, self.__right_y_2)
        self.__left_x_2, self.__left_y_2, self.__right_x_2, self.__right_y_2 = t

        self.update()

    @staticmethod
    def rotateLine(left_x, left_y, right_x, right_y):

        pygame.draw.line(window, (0, 0, 0), (left_x, left_y), (right_x, right_y))

        s = 0.5
        if left_x < right_x and left_y < right_y:
            left_x += s
            left_y -= s
            right_x -= s
            right_y += s
        elif left_x >= right_x and left_y < right_y:
            left_x += s
            left_y += s
            right_x -= s
            right_y -= s
        elif left_x >= right_x and left_y >= right_y:
            left_x -= s
            left_y += s
            right_x += s
            right_y -= s
        else:
            left_x -= s
            left_y -= s
            right_x += s
            right_y += s

        return left_x, left_y, right_x, right_y

    def update(self):
        self.__cx += self.__speed
        self.__left_x_1 += self.__speed
        self.__left_x_2 += self.__speed
        self.__right_x_1 += self.__speed
        self.__right_x_2 += self.__speed

class Truck:
    def __init__(self, x, y, width=70, height=40, r=12, speed = 5,
                 color1='#a1ae25', color2='#bb8918', color3='#e1dc6b', color4='#523637', color5='#f2b9cc'):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__r = r
        self.__speed = speed

        self.__color1 = color1              # color1 - цвет кузова
        self.__color2 = color2              # color2 - цвет кабины
        self.__color3 = color3              # color3 - цвет нижней панели
        self.__color4 = color4              # color4 - цвет колес
        self.__color5 = color5              # color5 - цвет фона

        # Параметры для колес
        self.__cx_1 = self.__x + 1.5 * self.__width
        self.__cx_2 = self.__x + 0.4 * self.__width
        self.__cy = self.__y + self.__height

        self.__wheel_1 = Wheel(self.__cx_1, self.__cy, self.__r, self.__speed, color1=self.__color4)
        self.__wheel_2 = Wheel(self.__cx_2, self.__cy, self.__r, self.__speed, color1=self.__color4)

    @staticmethod
    def rotateLine(left_x, left_y, right_x, right_y):

        pygame.draw.line(window, (0, 0, 0), (left_x, left_y), (right_x, right_y))

        s = 0.5
        if left_x < right_x and left_y < right_y:
            left_x += s
            left_y -= s
            right_x -= s
            right_y += s
        elif left_x >= right_x and left_y < right_y:
            left_x += s
            left_y += s
            right_x -= s
            right_y -= s
        elif left_x >= right_x and left_y >= right_y:
            left_x -= s
            left_y += s
            right_x += s
            right_y -= s
        else:
            left_x -= s
            left_y -= s
            right_x += s
            right_y += s

        return left_x, left_y, right_x, right_y

    def drawTruck(self):

        pygame.draw.rect(window, self.__color1, (self.__x, self.__y, self.__width, self.__height))
        pygame.draw.rect(window, self.__color2, (self.__x + self.__width, self.__y, self.__width - 10, self.__height))

        pygame.draw.rect(window, self.__color2, (self.__x + self.__width,
                                                 self.__y - self.__height + 10, self.__width // 2, self.__height))
        pygame.draw.rect(window, self.__color5, (self.__x + self.__width + 6,
                                                 self.__y - self.__height + 17, self.__width // 3, self.__height // 2))

        self.__wheel_1.create()
        self.__wheel_2.create()

        result = self.update()
        pygame.display.update()
        return result

    def update(self):
        if self.__x <= 1000:
            self.__x += self.__speed
        else:
            return 1
        self.__cx_1 = self.__x + 1.5 * self.__width
        self.__cx_2 = self.__x + 0.4 * self.__width
        return 0

class Car(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.image = pygame.image.load(filename).convert_alpha()

    def draw(self):
        self.rect = self.image.get_rect(center=(self.__x, self.__y))
        window.blit(self.image, self.rect)
        self.update()

    def update(self):
        if self.__x >= 0:
            self.__x += self.__speed
        else:
            self.__speed = - random.randint(1, 7)
            self.image = pygame.image.load(random.choice(['img/car.png', 'img/car2.png', 'img/careta.png'])).convert_alpha()
            self.__x = 1000

class Cloud:
    def __init__(self, x, y, color, speed):
        self._x = x
        self._y = y
        self._color = color
        self._speed = speed

    def draw(self):
        pygame.draw.circle(window, self._color, (self._x, self._y), 30)
        pygame.draw.circle(window, self._color, (self._x - 30, self._y + 10), 30)
        pygame.draw.circle(window, self._color, (self._x + 30, self._y + 10), 30)
        pygame.draw.circle(window, self._color, (self._x, self._y + 20), 30)

        self.update()

    def edge(self):
        if self._speed > 0:
            if self._x < 0:
                self._x = random.randint(1000, 1200)
                self._y = random.randint(0, 200)

        else:
            if self._x > 1000:
                self._x = random.randint(-100, 10)
                self._y = random.randint(0, 200)

    def update(self):
        self._x -= self._speed
        self.edge()

class Rain(Cloud):
    def __init__(self, x, y, color1, speed, color2):
        super().__init__(x, y, color1, speed)
        self.__color1 = color1
        self.__color2 = color2
        self.__rain_x = random.randint(100, 900)
        self.__flag = False
        self.__dig_flag = 0
        self.__i = 1

    def update(self):
        if not self.__flag:
            self._x -= self._speed
        self.edge()
        self.rain()

    def rain(self):
        if self._x == self.__rain_x:
            self._color = self.__color2
            self.__flag = True

            if self.__i < 4:
                for j in range(1, self.__i + 1):
                    Rain.drop(self._x + 30, self._y + j * 60, self.__color2)
                    Rain.drop(self._x - 30, self._y + j * 60, self.__color2)
                    Rain.drop(self._x, self._y + j * 70, self.__color2)

            self.__i += 1
            self.__dig_flag += 1

        if self.__dig_flag % 5 == 0:
            self.__i = 0

        if self.__dig_flag == 100:
            self._x += self._speed
            self.__rain_x = random.randint(100, 900)
            self.__flag = False
            self.__i = 1
            self._color = self.__color1
            self.__dig_flag = 0


    @staticmethod
    def drop(x, y, color):
        pygame.draw.polygon(window, color, ((x - 6, y), (x + 6, y), (x - 1, y - 13)))
        pygame.draw.circle(window, color, (x, y), 6)

pygame.init()
window = pygame.display.set_mode((1000, 600))
pygame.display.set_caption('Машинки')

truck_1_x = 50
truck_2_x = 0
truck_1_y = 520
truck_2_y = 430
speed1 = 5
speed2 = 3
cx = 50
cy = 50
r = 25

background = pygame.image.load('img/bg.jpg').convert()
background = pygame.transform.smoothscale(background, window.get_size())

truck1 = Truck(truck_1_x, truck_1_y, width=100, height=60, r=20, speed=5)
truck2 = Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
               color1='#d2afae', color4='#5e6464', color2='#f4c88c', color5='#a5c6b1')
truck3 = Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
               color1='#c7aabc', color4='#02334a', color2='#513e5c', color5='#b8e3ea', color3='#02334a')

car1 = Car(1000, truck_2_y, -random.randint(2, 5), 'img/car.png')
car2 = Car(1700, truck_2_y + 30, -random.randint(2, 5), 'img/car.png')


cloud1 = Cloud(random.randint(50, 950), random.randint(50, 250), (255, 255, 255), 2)
cloud2 = Cloud(random.randint(50, 950), random.randint(50, 250), '#f6fafb', -2)
cloud3 = Cloud(random.randint(50, 950), random.randint(50, 250), (255, 255, 255), 2)
rain1 = Rain(random.randint(50, 950), random.randint(50, 250), '#b8e3ea', -2, '#5e6668')
rain2 = Rain(random.randint(50, 950), random.randint(50, 250), '#b8e3ea', -2, '#5e6668')

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.blit(background, (0, 0))
    car1.draw()
    car2.draw()
    r1 = truck1.drawTruck()
    r2 = truck2.drawTruck()
    if r1 == 1:
        truck1 = random.choice([Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
               color1='#c7aabc', color4='#02334a', color2='#513e5c', color5='#b8e3ea', color3='#02334a'),
                                Truck(-400, truck_1_y, width=100, height=60, r=20, speed=5),
                                Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
               color1='#c7aabc', color4='#02334a', color2='#513e5c', color5='#b8e3ea', color3='#02334a'),
                                Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
                                      color1='#9db33e', color4='#264e2c', color2='#55761a', color5='#f6f7cd',
                                      color3='#02334a'),
                                Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
                                      color1='#a96562', color4='#264e2c', color2='#4e7851', color5='#ccb8a8',
                                      color3='#02334a')
                                ])
        r1 = 0
    if r2 == 1:
        truck2 = random.choice([Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
               color1='#c7aabc', color4='#02334a', color2='#513e5c', color5='#b8e3ea', color3='#02334a'),
                                Truck(-400, truck_1_y, width=100, height=60, r=20, speed=5),
                                Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
               color1='#c7aabc', color4='#02334a', color2='#513e5c', color5='#b8e3ea', color3='#02334a'),
                                Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
                                      color1='#9db33e', color4='#264e2c', color2='#55761a', color5='#f6f7cd',
                                      color3='#02334a'),
                                Truck(truck_2_x - 200, truck_1_y - 20, width=100, height=60, r=20, speed=speed2,
                                      color1='#a96562', color4='#264e2c', color2='#4e7851', color5='#ccb8a8',
                                      color3='#02334a')
        ])
        r2 = 0
    cloud1.draw()
    cloud2.draw()
    cloud3.draw()
    rain1.draw()
    rain2.draw()
    pygame.display.update()

pygame.quit()
