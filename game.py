import random
import pygame
from pygame.locals import *
from pygame.time import Clock


class Game:
    def main(self):
        up = 0
        right = 1
        down = 2
        left = 3

        # creating the window
        pygame.init()
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('Snake')

        # creating the snake
        snake = [(200, 200), (210, 200), (220, 200)]
        skin_snake = pygame.Surface((10, 10))
        skin_snake.fill((0, 153, 51))

        # creating the apple
        apple_position = self.on_grid_random()
        apple = pygame.Surface((10, 10))
        apple.fill((255, 255, 255))

        # initial direction where the face of the snake is
        direction = left

        # FPS
        clock = pygame.time.Clock()

        font = pygame.font.Font('freesansbold.ttf', 18)
        score = 0
        clock.tick(10)
        game_over = False
        while not game_over:
            clock.tick(10 + (score * 2) if score != 0 else 20)
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()

                #key press analysis
                if event.type == KEYDOWN:
                    if event.key == K_UP and direction != down:
                        direction = up
                    if event.key == K_DOWN and direction != up:
                        direction = down
                    if event.key == K_LEFT and direction != right:
                        direction = left
                    if event.key == K_RIGHT and direction != left:
                        direction = right


            # collision with the apple
            if self.collision(snake[0], apple_position):
                apple_position = self.on_grid_random()
                snake.append((0, 0))
                score = score + 1

            # collision with the wall
            if snake[0][0] == 600 or snake[0][1] == 600 or snake[0][0] < 0 or snake[0][1] < 0:
                game_over = True
                break

            # collision with own body
            for i in range(1, len(snake) - 1):
                if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                    game_over = True
                    break

            if game_over:
                break

            # body follows the position of the head
            for i in range(len(snake) - 1, 0, -1):
                snake[i] = (snake[i - 1][0], snake[i - 1][1])

            # Movement
            if direction == up:
                snake[0] = (snake[0][0], snake[0][1] - 10)
            if direction == down:
                snake[0] = (snake[0][0], snake[0][1] + 10)
            if direction == right:
                snake[0] = (snake[0][0] + 10, snake[0][1])
            if direction == left:
                snake[0] = (snake[0][0] - 10, snake[0][1])

            screen.fill((0, 0, 0))
            screen.blit(apple, apple_position)

            fontscore = font.render('Score: %s' % score, True, (255, 255, 255))
            rectscore = fontscore.get_rect()
            rectscore.topright = (600 - 120, 10)
            screen.blit(fontscore, rectscore)

            for pos in snake:
                screen.blit(skin_snake, pos)

            pygame.display.update()

        while True:
            game_over_font = pygame.font.Font('freesansbold.ttf', 75)
            game_over_screen = game_over_font.render('Game Over', True, (255, 0, 0))
            game_over_rect = game_over_screen.get_rect()
            game_over_rect.midtop = (600 / 2, 10)
            screen.blit(game_over_screen, game_over_rect)
            pygame.display.update()
            pygame.time.wait(0)
            while True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        exit()

    def on_grid_random(self):
        x = random.randint(0, 590)
        y = random.randint(0, 590)
        return x // 10 * 10, y // 10 * 10

    def collision(self, c1, c2):
        return (c1[0] == c2[0]) and (c1[1] == c2[1])


if __name__ == '__main__':
    p = Game()
    p.main()
