#Импортируем необходимые библиотеки
import pygame
import sys
from suzhetka import V1Game

def main():
    # Создается окно
    pygame.init()
    pygame.display.set_caption("cyberpank 2077")
    game = V1Game()
    screen = pygame.display.set_mode((1280, 500))
    game_font = pygame.font.Font("data/PressStart2P-Regular.ttf", 24)
    screen.fill("white")

    death_count = 0
    while True:
        if death_count <= 0:
            text = game_font.render("Press any Key to Start", True, (0, 0, 0))
        elif death_count > 0:
            text = game_font.render("Press any Key to Restart", True, (0, 0, 0))
            score = game_font.render("Your Score: " + str(game.player_score), True, (0, 0, 0))
            scoreRect = score.get_rect(center=(1000, 1000))
            screen.blit(score, scoreRect)
            game.player_score = 0

        textRect = text.get_rect(center=(650, 300))
        screen.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:#При нажатии на любую кнопку открывается окно с игрой
                game.run()
                if game.game_over:
                    death_count += 1
                    game.game_over = False