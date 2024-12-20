import pygame
from src.object import Object
from src.spriteLoader import load_sprite_sheets


class Food(Object):
    ANIMATION_DELAY = 2

    def __init__(self, x, y, name_food):
        super().__init__(x, y, 72, 72, name="food")
        self.all_sprites = load_sprite_sheets("Items", "Fruits", 32, 32, False)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.animation_count = 0
        self.sprites = self.all_sprites[name_food]
        self.image = self.sprites[0]
        self.mask = pygame.mask.from_surface(self.image)

    def loop(self):
        if self.animation_count // self.ANIMATION_DELAY >= len(self.sprites):
            self.animation_count = 0

        idx_sprite = (self.animation_count // self.ANIMATION_DELAY) % len(self.sprites)
        self.image = self.sprites[idx_sprite]
        self.animation_count += 1

        self.mask = pygame.mask.from_surface(self.image)


class Banana(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Bananas")


class Apple(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Apple")


class Strawberry(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Strawberry")


class Melon(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Melon")

class Kiwi(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Kiwi")

class Orange(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Orange")

class Pineapple(Food):
    def __init__(self, x, y):
        super().__init__(x, y, "Pineapple")