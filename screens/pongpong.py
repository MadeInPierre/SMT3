import pygame
from bases import Screen


class PongPong(Screen):
    def __init__(self, size):
        super(PongPong, self).__init__(size)
        self.WHITE = (200, 200, 200)
        self.BLACK = (50, 50, 50)

        self.external_margin = 20

        self.up_pressed = False
        self.down_pressed = False

        self.paddle_size = (self.size[0] / 25, self.size[1] / 3)
        self.paddle_y = self.size[1] / 2
        self.paddle_direction = 0 # 1 is going down, -1 is up
        self.paddle_speed = self.size[1] * 0.05

        self.ball_size = int(self.size[0] / 30)
        self.ball_pos = (self.size[0] / 2, self.size[1] / 2)
        self.ball_speed = self.size[1] * 0.01
        self.ball_direction = [-1, -1] # 1 is going down of right, -1 is up or left

    def update(self, window, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.up_pressed = True
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.up_pressed = False
                elif event.key == pygame.K_DOWN:
                    self.down_pressed = False

        # Handle input
        if (self.up_pressed and self.down_pressed) or (not self.up_pressed and not self.down_pressed):
            self.paddle_direction = 0
        elif self.up_pressed:
            self.paddle_direction = -1
        elif self.down_pressed:
            self.paddle_direction = 1

        # Move the components
        self.paddle_y += self.paddle_direction * self.paddle_speed
        if self.paddle_y < self.external_margin:
            self.paddle_y = self.external_margin
            self.paddle_direction = 0
        elif self.paddle_y > self.size[1] - self.paddle_size[1] - self.external_margin:
            self.paddle_y = self.size[1] - self.paddle_size[1] - self.external_margin
            self.paddle_direction = 0
        
        if (self.ball_pos[0] < self.external_margin + self.paddle_size[0] or self.ball_pos[0] > self.size[0] - self.ball_size - self.external_margin - self.paddle_size[0]) and \
           (self.ball_pos[1] > self.paddle_y and self.ball_pos[1] < self.paddle_y + self.paddle_size[1] - self.ball_size):
            self.ball_direction[0] *= -1
        if self.ball_pos[1] < 0 or self.ball_pos[1] > self.size[1] - self.ball_size:
            self.ball_direction[1] *= -1
        self.ball_pos = (self.ball_pos[0] + self.ball_direction[0] * self.ball_speed,
                         self.ball_pos[1] + self.ball_direction[1] * self.ball_speed)
        if self.ball_pos[0] < 0 or self.ball_pos[0] > self.size[0] - self.ball_size:
            self.ball_pos = (self.size[0] / 2, self.size[1] / 2)


        # Render the components
        paddle_img = pygame.Surface(self.paddle_size)
        paddle_img.fill(self.WHITE)

        ball_img   = pygame.Surface((self.ball_size, self.ball_size))
        ball_img.fill(self.BLACK)
        pygame.draw.circle(ball_img, self.WHITE, (ball_img.get_rect().width / 2, ball_img.get_rect().width / 2), self.ball_size / 2)

        # Draw to the screen
        window.fill(self.BLACK)
        window.blit(paddle_img, (self.external_margin, self.paddle_y))
        window.blit(paddle_img, (self.size[0] - self.paddle_size[0] - self.external_margin, self.paddle_y))
        window.blit(ball_img, (self.ball_pos[0], self.ball_pos[1]))
