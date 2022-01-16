#Импортируем необходимые библиотеки
import pygame
import sys
import random
from choice2_0 import choice2_0

#Создаем класс Cloud
class Cloud(pygame.sprite.Sprite):
    def __init__(self, image, x_pos, y_pos):
        super().__init__()
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.x -= 1

#Создаем класс Hero
class Hero(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.jump_sfx = pygame.mixer.Sound("data/jump.mp3")
        self.running_sprites = []
        self.ducking_sprites = []

        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("data/mainhero.png"), (80, 100)))
        self.running_sprites.append(pygame.transform.scale(
            pygame.image.load("data/mainhero.png"), (80, 100)))

        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("data/mainhero.png"), (110, 60)))
        self.ducking_sprites.append(pygame.transform.scale(
            pygame.image.load("data/mainhero.png"), (110, 60)))

        self.x_pos = x_pos
        self.y_pos = y_pos
        self.current_image = 0
        self.image = self.running_sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.velocity = 50
        self.gravity = 4.5
        self.ducking = False

    def jump(self):
        self.jump_sfx.play()
        if self.rect.centery >= 360:
            while self.rect.centery - self.velocity > 40:
                self.rect.centery -= 1

    def duck(self):
        self.ducking = True
        self.rect.centery = 380

    def unduck(self):
        self.ducking = False
        self.rect.centery = 360

    def apply_gravity(self):
        if self.rect.centery <= 360:
            self.rect.centery += self.gravity

    def update(self):
        self.animate()
        self.apply_gravity()

    def animate(self):
        self.current_image += 0.05
        if self.current_image >= 2:
            self.current_image = 0

        if self.ducking:
            self.image = self.ducking_sprites[int(self.current_image)]
        else:
            self.image = self.running_sprites[int(self.current_image)]

#Создаем класс Police
class Police(pygame.sprite.Sprite):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.sprites = []
        for i in range(1, 7):
            current_sprite = pygame.transform.scale(
                pygame.image.load(f"data/police.png"), (80, 80))
            self.sprites.append(current_sprite)
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, game_speed):
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

#Создаем класс vertushka
class vertushka(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x_pos = 1300
        self.y_pos = random.choice([280, 295, 350])
        self.sprites = []
        self.sprites.append(
            pygame.transform.scale(
                pygame.image.load("data/vertushka.png"), (84, 62)))
        self.sprites.append(
            pygame.transform.scale(
                pygame.image.load("data/vertushka.png"), (84, 62)))
        self.current_image = 0
        self.image = self.sprites[self.current_image]
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self, game_speed):
        self.animate()
        self.x_pos -= game_speed
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def animate(self):
        self.current_image += 0.025
        if self.current_image >= 2:
            self.current_image = 0
        self.image = self.sprites[int(self.current_image)]

#Создаем главный класс(V1Game)
class V1Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((1280, 500))
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.Font("data/PressStart2P-Regular.ttf", 24)
        self.obstacle_group = pygame.sprite.Group()
        self.game_speed = 8
        self.jump_count = 10
        self.player_score = 0
        self.game_over = False

    def run(self):
        death_sfx = pygame.mixer.Sound("data/lose.mpeg")
        points_sfx = pygame.mixer.Sound("data/100points.mp3")
        obstacle_timer = 0
        obstacle_spawn = False
        obstacle_cooldown = 1000

        # Surfaces
        ground = pygame.image.load("data/ground.png")
        ground = pygame.transform.scale(ground, (2980, 40))
        ground_x = 0
        ground_rect = ground.get_rect(center=(1000, 720))

        mainhero_group = pygame.sprite.GroupSingle()
        vertushka_group = pygame.sprite.Group()

        car = Hero(50, 360)
        mainhero_group.add(car)

        while True:
            keys = pygame.key.get_pressed()
            if self.player_score > 2022:#После достижения 2022 очков появляется новое окно
                choice2_0()
            if keys[pygame.K_DOWN]:
                car.duck()
            else:
                if car.ducking:
                    car.unduck()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                        car.jump()
                        if self.game_over:
                            self.game_over = False
                            self.game_speed = 5
                            self.player_score = 0

            self.screen.fill("white")

            if pygame.sprite.spritecollide(mainhero_group.sprite, self.obstacle_group, False):
                self.game_over = True
                death_sfx.play()
            if self.game_over:
                self.end_game()
                return

            if not self.game_over:
                self.game_speed += 0.0025
                if round(self.player_score, 1) % 100 == 0 and int(self.player_score) > 0:
                    points_sfx.play()

                if pygame.time.get_ticks() - obstacle_timer >= obstacle_cooldown:
                    obstacle_spawn = True

                if obstacle_spawn:
                    obstacle_random = random.randint(1, 50)
                    if obstacle_random in range(1, 7):
                        new_obstacle = Police(1280, 340)
                        self.obstacle_group.add(new_obstacle)
                        obstacle_timer = pygame.time.get_ticks()
                        obstacle_spawn = False
                    elif obstacle_random in range(7, 10):
                        new_obstacle = vertushka()
                        self.obstacle_group.add(new_obstacle)
                        obstacle_timer = pygame.time.get_ticks()
                        obstacle_spawn = False

                self.player_score += 0.1
                player_score_surface = self.game_font.render(
                        str(f'Points:{int(self.player_score)}'), True, "black")
                self.screen.blit(player_score_surface, (1000, 10))

                vertushka_group.update()
                vertushka_group.draw(self.screen)

                mainhero_group.update()
                mainhero_group.draw(self.screen)

                self.obstacle_group.update(self.game_speed)
                self.obstacle_group.draw(self.screen)

                ground_x -= self.game_speed

                self.screen.blit(ground, (ground_x, 360))
                self.screen.blit(ground, (ground_x + 1280, 720))

                if ground_x <= -1280:
                    ground_x = 0

            self.clock.tick(120)
            pygame.display.update()

    def end_game(self):
        game_over_text = self.game_font.render("you are slave!", True, "black")
        game_over_rect = game_over_text.get_rect(center=(640, 200))
        score_text = self.game_font.render(f"Score: {int(self.player_score)}", True, "black")
        score_rect = score_text.get_rect(center=(640, 240))
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(score_text, score_rect)
        self.game_speed = 5
        self.obstacle_group.empty()