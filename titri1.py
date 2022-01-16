#Импортируем необходимые библиотеки
import pygame

def titri1():
    # Создается окно
    pygame.init()
    pygame.display.set_caption("cyberpank 2077")
    screen = pygame.display.set_mode((1280, 500))
    screen.fill("white")
    points_sfx = pygame.mixer.Sound("data/Неплохая получилась история.mpeg")
    points_sfx.play()
    face_off = pygame.mixer.Sound("data/face off.mpeg")
    font = pygame.font.SysFont("data/PressStart2P-Regular.ttf", 32)
    tick = 0
    pygame.time.set_timer(tick, 1000)
    b = 0

    x, y = 50, 550
    FPS = 15

    text = font.render("Directed by", True, (0, 0, 0))
    text1 = font.render("Executive Producer -  Myznikov Alexander", True, (0, 0, 0))
    text2 = font.render("Co-Executive Producer - Zobov Arseniy", True, (0, 0, 0))
    text3 = font.render("Presenter - Lepenkin Michael", True, (0, 0, 0))
    text4 = font.render("We tried very hard, creating this game for you, we hope that you will become"
                        " a real Boss Of The Gym,",True,(0,0,0))
    text5 = font.render("You will find your slaves, your fingers will always be fine, and you will not forget "
                        "how to stick them in deep places,",True,(0,0,0))
    text6 = font.render("If you did not understand anything from this,",True,(0,0,0))
    text7 = font.render("Then we advise you to watch some movies with Billy and Van to enlighten your mind."
                        ,True,(0,0,0))
    text8 = font.render("Thank you for reading and good luck)",True,(0,0,0))
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit(0)
            elif event.type == tick:
                b += 1
            if b == 30:
                points_sfx.stop()
                face_off.play()
        clock.tick(FPS)
        y -= 1
        screen.fill("white")
        screen.blit(text, (x, y))
        screen.blit(text1, (x, y + 25))
        screen.blit(text2, (x, y + 50))
        screen.blit(text3, (x, y + 75))
        screen.blit(text4, (x, y + 100))
        screen.blit(text5, (x, y + 125))
        screen.blit(text6, (x, y + 150))
        screen.blit(text7, (x, y + 175))
        screen.blit(text8, (x, y + 200))
        pygame.display.update()