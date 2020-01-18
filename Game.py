import sys, pygame
from pygame.locals import *
from Rectangle import *
from Zone import *
from Grid import *


class Game:
    size = width, height = 500, 500
    window = pygame.display.set_mode(size)

    background = (205, 193, 180)
    rectangle_list = {}
    rectangle_zone = {}

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("2048")
        self.window.fill(Color(187, 173, 160))

        self.square_width = (pygame.display.get_surface().get_width() - 80) / 4
        self.square_height = (pygame.display.get_surface().get_height() - 80) / 4
        self.square_size = self.square_width, self.square_height

        self.grille = Grid()

    def draw_background(self):
        for i in range(4):
            self.rectangle_list[i*10] = pygame.draw.rect(self.window, self.background, (15, 15*(i+1) + i * self.square_height, self.square_width, self.square_height))
            self.rectangle_list[i*10+1] = pygame.draw.rect(self.window, self.background, (15 * 2 + self.square_width, 15*(i+1) + i * self.square_height, self.square_width, self.square_height))
            self.rectangle_list[i*10+2] = pygame.draw.rect(self.window, self.background, (15 * 3 + 2 * self.square_width, 15*(i+1) + i * self.square_height, self.square_width, self.square_height))
            self.rectangle_list[i*10+3] = pygame.draw.rect(self.window, self.background, (15 * 4 + 3 * self.square_width, 15*(i+1) + i * self.square_height, self.square_width, self.square_height))

            for key, rectangle in self.rectangle_list.items():
                self.rectangle_zone[key] = Zone(int(key), rectangle.x, rectangle.y)

    def draw_grid(self):
        for coord in self.grille.cells:
            value = self.grille.cells[coord]
            if value != 0:
                rect = Rectangle(self.window, self.rectangle_zone[coord].position, self.rectangle_zone[coord].x,
                                 self.rectangle_zone[coord].y, value, self.rectangle_zone)
                rect.draw_rectangle()


game = Game()
game.draw_background()
game.draw_grid()

while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                isWin, isLose = game.grille.calculState()
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    if isLose == True:
                        game.draw_background()
                        game.draw_grid()
                        font = pygame.font.SysFont("Helvetica Neue", 45)
                        text = font.render("Perdu", 1, (0,0,0))
                        game.window.blit(text, ((game.window.get_width() - text.get_width()) / 2,
                                                (game.window.get_height() - text.get_height()) / 2))
                        pygame.display.update()
                    elif isWin == True:
                        game.draw_background()
                        game.draw_grid()
                        font = pygame.font.SysFont("Helvetica Neue", 45)
                        text = font.render("Gagné", 1, (0,0,0))
                        game.window.blit(text, ((game.window.get_width() - text.get_width()) / 2,
                                                (game.window.get_height() - text.get_height()) / 2))
                        pygame.display.update()
                    else:
                        game.grille.move(event.key)
                        game.grille.addRandomTile(game.grille.cells)
                        game.draw_background()
                        game.draw_grid()
                        pygame.display.update()

                elif event.key == pygame.K_RETURN:
                    if isWin == True or isLose == True:
                        game = Game()
                        game.draw_background()
                        game.grille = Grid()
                        game.draw_grid()
                        pygame.display.update()

                elif event.key == pygame.K_ESCAPE:
                    exit()

        pygame.display.update()
