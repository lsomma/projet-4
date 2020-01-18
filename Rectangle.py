import pygame
from pygame.locals import *


class Rectangle:
    rect_colors = {2: (238, 228, 218), 4: (237, 224, 200), 8: (242, 177, 121), 16: (245, 149, 99),
                   32: (246, 124, 95), 64: (246, 94, 59), 128: (237, 207, 114), 256: (237, 204, 97),
                   512: (237, 200, 80), 1024: (237, 197, 63), 2048: (237, 194, 46)}
    text_colors = [(119, 110, 101), (249, 246, 242)]

    def __init__(self, window, position, x, y, value, rectangle_zone):
        self.window = window
        self.square_width = (pygame.display.get_surface().get_width() - 80) / 4
        self.square_height = (pygame.display.get_surface().get_height() - 80) / 4
        self.square_size = self.square_width, self.square_height
        self.position = int(position)
        self.x = x
        self.y = y
        self.value = value
        self.rectangle_zone = rectangle_zone

    def draw_rectangle(self):
        rect = pygame.draw.rect(self.window, self.rect_colors[self.value], (self.x, self.y, self.square_width, self.square_height))

        if self.value > 512:
            font = pygame.font.SysFont("Helvetica Neue", 45)
        else:
            font = pygame.font.SysFont("Helvetica Neue", 55)

        if self.value > 4:
            text = font.render(str(self.value), 1, self.text_colors[1])
        else:
            text = font.render(str(self.value), 1, self.text_colors[0])

        self.window.blit(text, ((self.square_width - text.get_width()) / 2 + rect.x, (self.square_width - text.get_height()) / 2 + rect.y))

    def key_down(self, key):
        if key == pygame.K_UP:
            if int(self.position)//10 > 0:
                self.position = self.position-10
                self.x = self.rectangle_zone[self.position].x
                self.y = self.rectangle_zone[self.position].y
        elif key == pygame.K_DOWN:
            if int(self.position)//10 < 3:
                self.position = self.position+10
                self.x = self.rectangle_zone[self.position].x
                self.y = self.rectangle_zone[self.position].y
        elif key == pygame.K_RIGHT:
            if int(self.position)%10 < 3:
                self.position += 1
                self.x = self.rectangle_zone[self.position].x
                self.y = self.rectangle_zone[self.position].y
        elif key == pygame.K_LEFT:
            if int(self.position)%10 > 0:
                self.position -= 1
                self.x = self.rectangle_zone[self.position].x
                self.y = self.rectangle_zone[self.position].y