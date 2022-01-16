#Импортируем необходимые библиотеки
import pygame
from start import start

def disclaimer():
    #Создается окно
    pygame.init()
    pygame.display.set_caption("cyberpank 2077")
    screen = pygame.display.set_mode((1280, 500))
    screen.fill("black")
    font = pygame.font.SysFont("data/PressStart2P-Regular.ttf", 100)
    fontt = pygame.font.SysFont("data/PressStart2P-Regular.ttf", 32)


    text = font.render("Дисклеймер", True, (255, 0, 0))
    textRect = text.get_rect(center=(650, 75))
    screen.blit(text, textRect)

    text = fontt.render("ВСЕ СОБЫТИЯ И ПЕРСОНАЖИ В ДАННОЙ ИГРЕ ВЫМЫШЛЕНЫ.", True, (255, 255, 255))
    textRect = text.get_rect(center=(650, 200))
    screen.blit(text, textRect)

    text = fontt.render("ЛЮБЫЕ СОВПАДЕНИЯ С РЕАЛЬНЫМ МИРОМ ЯВЛЯЮТСЯ ВАШЕЙ ФАНТАЗИЕЙ.", True, (255, 255, 255))
    textRect = text.get_rect(center=(650, 250))
    screen.blit(text, textRect)

    text = fontt.render("В ДАННОЙ ИГРЕ ВЫ БОЛЬШЕ НЕ НАЙДЕТЕ РУССКОГО ТЕКСТА, ПОТОМУ ЧТО НАДО УЧИТЬ АНГЛИЙСКИЙ)",
                        True, (255, 255, 255))
    textRect = text.get_rect(center=(650, 300))
    screen.blit(text, textRect)

    text = fontt.render("ЖЕЛАЕМ ПРИЯТНОЙ ИГРЫ)",
                        True, (255, 255, 255))
    textRect = text.get_rect(center=(650, 350))
    screen.blit(text, textRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:#При нажатии на пробел появляется новое окно
                    start()
        pygame.display.update()
disclaimer()