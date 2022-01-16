#Импортируем необходимые библиотеки
import pygame
import sys
from titri import titri
from titri1 import titri1

def choice2_0():
    # Создается окно
    pygame.init()
    pygame.display.set_caption("cyberpank 2077")
    screen = pygame.display.set_mode((1280, 500))
    game_font = pygame.font.Font("data/PressStart2P-Regular.ttf", 18)
    screen.fill("white")
    k = 0

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and k == 0:

                    text = game_font.render("Make a choice!", True, (0, 0, 0))
                    textRect = text.get_rect(center=(650, 75))
                    screen.blit(text, textRect)

                    text = game_font.render("Forgive Van[1]", True, (0, 0, 0))
                    textRect = text.get_rect(center=(650, 200))
                    screen.blit(text, textRect)

                    text = game_font.render("Kill Van[2]", True, (0, 0, 0))
                    textRect = text.get_rect(center=(650, 325))
                    screen.blit(text, textRect)

                    k += 1

                if event.key == pygame.K_1 and k == 1:#При нажатии на 1 появляется новое окно
                    screen.fill("white")
                    text = game_font.render("I think you're stupid because he betrayed Billy, and you forgive him.",
                                            True, (0, 0, 0))
                    textRect = text.get_rect(center=(625, 75))
                    screen.blit(text, textRect)

                    text = game_font.render("But it is your choice.", True, (0, 0, 0))
                    textRect = text.get_rect(center=(200, 150))
                    screen.blit(text, textRect)

                    text = game_font.render("Press space to continue.", True, (0, 0, 0))
                    textRect = text.get_rect(center=(640, 450))
                    screen.blit(text, textRect)

                    k += 1

                if event.key == pygame.K_2 and k == 1:#При нажатии на 2 появляется новое окно
                    screen.fill("white")
                    text = game_font.render("I think you made the right choice because Van betrayed Billy.",
                                            True, (0, 0, 0))
                    textRect = text.get_rect(center=(575, 75))
                    screen.blit(text, textRect)

                    text = game_font.render("Press space to continue.", True, (0, 0, 0))
                    textRect = text.get_rect(center=(640, 450))
                    screen.blit(text, textRect)

                    k += 2

                elif event.key == pygame.K_SPACE and k == 2:#При нажатии на пробел появляется новое окно
                    titri()

                elif event.key == pygame.K_SPACE and k == 3:#При нажатии на пробел появляется новое окно
                    titri1()