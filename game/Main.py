import tkinter
from tkinter import Tk, Canvas
import random

WIDTH = 1024
HEIGHT = 640
SEG_SIZE = 32
MAX_VALUE = 100
GAS_LIMIT = 64
EAT_LIMIT = 80
VENTIL_LIMIT = 98
TAB_LIMIT = 98

IN_GAME = True


class Tablet(object):
    def __init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.form = "oval"
        self.color = "blue"

    def reset(self):
        c.delete(self.block)


class Tablets(object):
    def __init__(self):
        self.lst = []
        self.selected = None

    def is_exist(self, x, y):
        for tab in self.lst:
            if tab.x == x and tab.y == y:
                self.selected = tab
                return 1
        self.selected = None
        return 0

    def delete(self):
        if self.selected is not None:
            self.selected.reset()
            self.lst.remove(self.selected)
            self.selected = None

    def clear(self):
        for tab in self.lst:
            tab.reset()
        self.lst.clear()


class Ventil(object):
    def __init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.form = "oval"
        self.color = "green"

    def reset(self):
        c.delete(self.block)


class Ventils(object):
    def __init__(self):
        self.lst = []
        self.selected = None

    def is_exist(self, x, y):
        for v in self.lst:
            if v.x == x and v.y == y:
                self.selected = v
                return 1
        self.selected = None
        return 0

    def delete(self):
        if self.selected is not None:
            self.selected.reset()
            self.lst.remove(self.selected)
            self.selected = None

    def clear(self):
        for v in self.lst:
            v.reset()
        self.lst.clear()


class Dog(object):
    def __init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.form = "rect"
        self.color = "white"
        self.power = 5
        self.totals = 0
        self.mapping = {"Down": (0, 1), "Right": (1, 0), "Up": (0, -1), "Left": (-1, 0), "space": (0, 0)}
        self.vector = self.mapping["space"]

    def dec_power(self):
        self.power = self.power - 1 if self.power > 0 else 0

    def rest_power(self):
        self.power = 5

    def inc_totals(self, delta):
        self.totals = self.totals + delta

    def change_direction(self, event):
        if event.keysym in self.mapping:
            self.vector = self.mapping[event.keysym]

    def move(self):
        self.reset()
        self.x = self.x + self.vector[0]
        self.y = self.y + self.vector[1]
        if self.x == 0:
            self.x = 32
        if self.x == 33:
            self.x = 1
        if self.y == 1:
            self.y = 20
        if self.y == 21:
            self.y = 2
        # self.block = draw(self.x, self.y, self.form, self.color)
        self.block = draw_image(self.x, self.y, "dog")

    def reset(self):
        c.delete(self.block)


class Eat(object):
    def __init__(self, x, y, kind, block):
        self.x = x
        self.y = y
        self.block = block
        self.form = "oval"
        self.color = "yellow"
        self.kind = kind
        self.price = 5 if self.kind == "meat" else 1

    def reset(self):
        c.delete(self.block)


class Eats(object):
    def __init__(self):
        self.lst = []
        self.selected = None

    def is_exist(self, x, y):
        for eat in self.lst:
            if eat.x == x and eat.y == y:
                self.selected = eat
                return 1
        self.selected = None
        return 0

    def draw(self):
        for eat in self.lst:
            draw(eat.x, eat.y, eat.form, eat.color)

    def delete(self):
        if self.selected is not None:
            c.delete(self.selected.block)
            self.lst.remove(self.selected)
            self.selected = None

    def clear(self):
        for eat in self.lst:
            eat.reset()
        self.lst.clear()


class Gas(object):
    def __init__(self, x, y, block):
        self.x = x
        self.y = y
        self.block = block
        self.form = "rect"
        self.color = "gray"


class Gases(object):
    def __init__(self):
        self.lst = []

    def is_exist(self, x, y):
        for gas in self.lst:
            if gas.x == x and gas.y == y:
                return 1
        return 0

    def draw(self):
        for gas in self.lst:
            gas.block = draw(gas.x, gas.y, gas.form, gas.color)

    def size(self):
        return len(self.lst)

    def clear(self):
        for gas in self.lst:
            c.delete(gas.block)
        self.lst.clear()


def draw(x, y, form, color):
    if form == "rect":
        return c.create_rectangle((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, x * SEG_SIZE, y * SEG_SIZE, fill=color)
    if form == "oval":
        return c.create_oval((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, x * SEG_SIZE, y * SEG_SIZE, fill=color)


def draw_image(x, y, kind):
    if kind == "dog":
        return c.create_image((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, anchor="nw", image=dog_image)
    if kind == "gas":
        return c.create_image((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, anchor="nw", image=gas_image)
    if kind == "apple":
        return c.create_image((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, anchor="nw", image=apple_image)
    if kind == "meat":
        return c.create_image((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, anchor="nw", image=meat_image)
    if kind == "ventil":
        return c.create_image((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, anchor="nw", image=ventil_image)
    if kind == "tablet":
        return c.create_image((x - 1) * SEG_SIZE, (y - 1) * SEG_SIZE, anchor="nw", image=tab_image)


def is_free(x, y):
    if gases.is_exist(x, y) == 0 and ventils.is_exist(x, y) == 0 and tabs.is_exist(x, y) == 0 and eats.is_exist(x, y) == 0:
        return 1
    else:
        return 0


def add_gas():
    if random.randint(1, MAX_VALUE) > GAS_LIMIT:
        x = random.randint(1, 32)
        y = random.randint(2, 20)
        if is_free(x, y) == 1:
            gases.lst.append(Gas(x, y, draw_image(x, y, "gas")))


def add_eat():
    if random.randint(1, MAX_VALUE) > EAT_LIMIT:
        x = random.randint(1, 32)
        y = random.randint(2, 20)
        kind = "meat" if random.randint(1, 10) > 6 else "apple"
        if is_free(x, y) == 1:
            eats.lst.append(Eat(x, y, kind, draw_image(x, y, kind)))


def add_ventil():
    if random.randint(1, MAX_VALUE) > VENTIL_LIMIT:
        x = random.randint(1, 32)
        y = random.randint(2, 20)
        if is_free(x, y) == 1:
            ventils.lst.append(Ventil(x, y, draw_image(x, y, "ventil")))


def add_tablet():
    if random.randint(1, MAX_VALUE) > TAB_LIMIT:
        x = random.randint(1, 32)
        y = random.randint(2, 20)
        if is_free(x, y) == 1:
            tabs.lst.append(Tablet(x, y, draw_image(x, y, "tablet")))


def main():
    global IN_GAME
    if IN_GAME:
        if dog.block is None:
            dog.block = draw(dog.x, dog.y, dog.form, dog.color)
        dog.move()
        if eats.is_exist(dog.x, dog.y) == 1:
            dog.inc_totals(eats.selected.price)
            eats.delete()
        if tabs.is_exist(dog.x, dog.y) == 1:
            dog.power = 5
            tabs.delete()
        if ventils.is_exist(dog.x, dog.y):
            dog.inc_totals(10)
            gases.clear()
            ventils.delete()
        if gases.is_exist(dog.x, dog.y) == 1:
            dog.dec_power()
            IN_GAME = dog.power > 0

        display()

        add_gas()
        add_eat()
        add_ventil()
        add_tablet()

        root.after(150, main)
    else:
        dog.reset()
        gases.clear()
        eats.clear()
        ventils.clear()
        tabs.clear()

        set_state(restart_text, "normal")
        set_state(game_over_text, "normal")


def set_state(item, state):
    c.itemconfigure(item, state=state)


def new_game(event):
    global IN_GAME
    IN_GAME = True
    c.itemconfigure(restart_text, state='hidden')
    c.itemconfigure(game_over_text, state='hidden')
    start()


def display():
    c.create_rectangle(0, 0, 1024, 32, fill="#aaaaaa")
    c.create_text(64, 16, text="Счет: " + "{0:,d}".format(dog.totals),
                  font='Arial 16', fill='green',
                  state='normal')
    for idx in range(dog.power):
        x = 920 + 18 * (idx - 1)
        color = "green" if dog.power > 3 else "yellow" if dog.power > 1 else "red"
        c.create_rectangle(x, 8, x + 16, 24, fill=color)

def start():
    global gases, eats, dog, ventils, tabs, total
    gases = Gases()
    eats = Eats()
    ventils = Ventils()
    tabs = Tablets()
    total = 0

    dog = Dog(1, 2, None)

    c.bind("<KeyPress>", dog.change_direction)
    main()


root = Tk()
root.title("")

global tab_image, meat_image, apple_image, ventil_image, gas_image, dog_image
tab_image = tkinter.PhotoImage(file='tablet.png')
meat_image = tkinter.PhotoImage(file="meat.png")
apple_image = tkinter.PhotoImage(file="apple.png")
ventil_image = tkinter.PhotoImage(file="ventil.png")
gas_image = tkinter.PhotoImage(file="gas.png")
dog_image = tkinter.PhotoImage(file="dog.png")

c = Canvas(root, width=WIDTH, height=HEIGHT, bg="#aaaaaa")
c.grid()

c.focus_set()
game_over_text = c.create_text(WIDTH/2, HEIGHT/2, text="Игра закончена",
                               font='Arial 20', fill='red',
                               state='hidden')
restart_text = c.create_text(WIDTH/2, HEIGHT-HEIGHT/3,
                             font='Arial 30',
                             fill='white',
                             text="Для продолжения нажмите здесь",
                             state='hidden')
c.tag_bind(restart_text, "<Button-1>", new_game)

start()
root.mainloop()
