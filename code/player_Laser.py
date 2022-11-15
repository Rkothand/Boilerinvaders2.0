from turtle import speed
import pygame

class Player_Laser(pygame.sprite.Sprite):
    def __init__(self,pos,speed,screen_height):
        super().__init__()
        self.image = pygame.Surface((2,20))
        self.image.fill('red')
        self.rect = self.image.get_rect(center = pos)
        self.speed =speed
        self.height_y_constraint = screen_height

    def destroy(self):
        if self.rect.y <= -50 or self.rect.y >= self.height_y_constraint +50:
            self.kill()


    def update(self):
        self.rect.y += self.speed
        self.destroy()