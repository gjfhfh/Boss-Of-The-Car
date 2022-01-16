#Импортируем необходимые библиотеки
import pygame
import sys
from main2_0 import main


def perehod():
    # Создается окно
    pygame.init()
    pygame.display.set_caption("cyberpank 2077")
    screen = pygame.display.set_mode((1280, 500))
    game_font = pygame.font.Font("data/PressStart2P-Regular.ttf", 14)
    screen.fill("white")
    k = 0
    n = 0

    while True:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:#При нажатии на пробел появляется новая фраза
                    if k == 0:
                        text = game_font.render("Van: Hi,Billy! What are you doing tonight? How about robbing the"
                                                " leather club?", True, (0, 0, 0))
                        textRect = text.get_rect(center=(550, 50))
                        screen.blit(text, textRect)
                        k += 1
                    elif k == 1:
                        text = game_font.render("Billy: Hi,Van! That sounds great.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(240, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 2:
                        text = game_font.render("Van: Ok. But I will help you remotely. Let's meet at 9:00 in the park."
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(500, 200))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 3:
                        text = game_font.render("Billy:Ok.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(75, 275))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 4:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 5 and n == 1:
                        text = game_font.render("*In the park*", True, (0, 0, 0))
                        textRect = text.get_rect(center=(640, 50))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 6 and n == 1:
                        text = game_font.render("Van: Well, are you ready?", True, (0, 0, 0))
                        textRect = text.get_rect(center=(180, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 7 and n == 1:
                        text = game_font.render("Billy: Yes. Let's go.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(150, 200))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 8:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 9 and n == 2:
                        text = game_font.render("*Near the leather club*", True, (0, 0, 0))
                        textRect = text.get_rect(center=(640, 50))
                        screen.blit(text, textRect)
                        k += 1
                    elif k == 10 and n == 2:
                        text = game_font.render("Van: By the way, can you download a file from the computer which"
                                                " is in their computer room? ", True, (0, 0, 0))
                        textRect = text.get_rect(center=(650, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 11 and n == 2:
                        text = game_font.render("Billy: No problem.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(130, 200))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 12:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 13 and n == 3:
                        text = game_font.render("*In the leather club*", True, (0, 0, 0))
                        textRect = text.get_rect(center=(640, 50))
                        screen.blit(text, textRect)
                        k += 1
                    elif k == 14 and n == 3:
                        text = game_font.render("Billy: Ok, I'm here.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(150, 125))
                        screen.blit(text, textRect)
                        k += 1
                    elif k == 15 and n == 3:
                        text = game_font.render("Van: Well, turn on the computer.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(225, 200))
                        screen.blit(text, textRect)
                        k += 1
                    elif k == 16 and n == 3:
                        text = game_font.render("Billy: I turned it on but the computer is locked. Give me a password."
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(490, 275))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 17:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 18 and n == 4:
                        text = game_font.render("Van: Password?", True, (0, 0, 0))
                        textRect = text.get_rect(center=(100, 50))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 19 and n == 4:
                        text = game_font.render("Billy: Out with it!", True, (0, 0, 0))
                        textRect = text.get_rect(center=(140, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 20 and n == 4:
                        text = game_font.render("Van: DungeonmasterDarkholm", True, (0, 0, 0))
                        textRect = text.get_rect(center=(200, 200))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 21 and n == 4:
                        text = game_font.render("Billy: 'DungeonmasterDarkholm'? Yeah, that fits.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(350, 275))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 22 and n == 4:
                        text = game_font.render("Billy: I've done everything, what should I do next?", True, (0, 0, 0))
                        textRect = text.get_rect(center=(365, 350))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 23:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 24 and n == 5:
                        text = game_font.render("Van: Now you need to find the safe.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(245, 50))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 25 and n == 5:
                        text = game_font.render("Billy: I found it. It isn't locked. Give me a password."
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(385, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 26 and n == 5:
                        text = game_font.render("Van: 1234"
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(75, 200))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 27 and n == 5:
                        text = game_font.render("Billy: Yeah, that fits. What kind of jerk made up this password?"
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(450, 275))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 28  and n == 5:
                        text = game_font.render("Van: It doesn't matter. Take the money and get out of there."
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(430, 350))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 29:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 30 and n == 6:
                        text = game_font.render("Billy: I see 3 hundred bucks. I'm getting out of here."
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(400, 50))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 31 and n == 6:
                        text = game_font.render("Van: I'm waiting for you near our car.Hurry up!", True, (0, 0, 0))
                        textRect = text.get_rect(center=(340, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 32 and n == 6:
                        text = game_font.render("Billy: I'm near our car. Where are you?", True, (0, 0, 0))
                        textRect = text.get_rect(center=(300, 200))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 33 and n == 6:
                        text = game_font.render("Van: It doesn't matter. Get out of there.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(300, 275))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 34:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1
                        

                    elif k == 35 and n == 7:
                        text = game_font.render("Billy: I see the cops. How did they know about robbing?"
                                                " I was very careful.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(530, 50))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 36 and n == 7:
                        text = game_font.render("Van: I've called them because you've already got me."
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(375, 125))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 37 and n == 7:
                        text = game_font.render("Van: I want to get rid of you. You've always been against leather"
                                                " men.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(500, 200))
                        screen.blit(text, textRect)
                        k += 1


                    elif k == 38 and n == 7:
                        text = game_font.render("Billy: I think you've chosen the wrong door, leather man. "
                                                , True, (0, 0, 0))
                        textRect = text.get_rect(center=(400, 275))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 39 and n == 7:
                        text = game_font.render("Billy: I'll show you who's the boss of this gym.", True, (0, 0, 0))
                        textRect = text.get_rect(center=(350, 350))
                        screen.blit(text, textRect)
                        k += 1

                    elif k == 40:
                        text = game_font.render("Press escape to continue", True, (0, 0, 0))
                        textRect = text.get_rect(center=(175, 400))
                        screen.blit(text, textRect)
                        k += 1

                if event.key == pygame.K_ESCAPE and (k == 5 or k == 9 or k == 13 or k == 18 or k == 24 or k == 30 or
                                                     k == 35):
                    screen.fill("white")
                    n += 1

                elif event.key == pygame.K_ESCAPE and k == 41:#При нажатии на escape появляется новое окно
                    main()