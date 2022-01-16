#Импортируем необходимые библиотеки
import pygame
import sys
from choice import choice

def start():
    # Создается окно
    pygame.init()
    pygame.display.set_caption("cyberpank 2077")
    screen = pygame.display.set_mode((1280, 500))
    game_font = pygame.font.Font("data/PressStart2P-Regular.ttf", 24)
    screen.fill("white")

    while True:
        text = game_font.render("Welcome!", True, (0, 0, 0))
        textRect = text.get_rect(center=(650, 75))
        screen.blit(text, textRect)

        text1 = game_font.render("Play[1]", True, (0, 0, 0))
        text1Rect = text1.get_rect(center=(650, 200))
        screen.blit(text1, text1Rect)

        text2 = game_font.render("Exit[2]", True, (0, 0, 0))
        text2Rect = text2.get_rect(center=(650, 325))
        screen.blit(text2, text2Rect)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:#При нажатии на 1 появляется новое окно
                    choice()
                if event.key == pygame.K_2:#При нажатии на 2 закрывается программа
                    pygame.quit()
                    sys.exit()