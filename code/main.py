from re import X
from turtle import distance
import pygame
import sys
from player import Player
from tie import Tie
from random import choice 
from player_Laser import Player_Laser
from tie_Laser import Tie_Laser

class Game:
    def __init__(self):
        #player Character Setup
        player_sprite = Player((screen_width/2,screen_height),screen_width,5)
        self.player = pygame.sprite.GroupSingle(player_sprite)
        
        #Enemy Setup
        self.ties=pygame.sprite.Group()
        self.tie_fire = pygame.sprite.Group()
        self.tie_formation(rows=6,cols=8)
        self.tie_direction = 1


    def tie_formation(self,rows,cols,x_distance=60,y_distance=48,x_offset = 70, y_offset =100):
        for row_index, row in enumerate(range(rows)):
            for col_index, col in enumerate(range(cols)):
                x = col_index * x_distance + x_offset
                y = row_index * y_distance + y_offset

                if row_index == 0:                 
                    tie_sprite = Tie('TieI',x,y)
                elif 1 <= row_index <= 2: 
                    tie_sprite = Tie('TieB',x,y)
                else:
                    tie_sprite = Tie('TieF',x,y)
                self.ties.add(tie_sprite)
    
    def tie_position_checker(self):
        all_ties = self.ties.sprites()
        for tie in all_ties:
            if tie.rect.right >=screen_width:
                self.tie_direction =-1
                self.tie_strafe(2)
            elif tie.rect.left <= 0:
                self.tie_direction =1
                self.tie_strafe(2)
            

    def tie_strafe(self,distance):
        if self.ties:
            for tie in self.ties.sprites():
                tie.rect.y += distance

    def tie_shoot(self):
        if self.ties.sprites():
            random_tie = choice(self.ties.sprites())
            laser_sprite = Tie_Laser(random_tie.rect.center, 8, screen_height)
            self.tie_fire.add(laser_sprite)


    def run(self):
        
        self.player.update()
        self.ties.update(self.tie_direction)


        self.tie_position_checker()
        #self.tie_shoot()
        self.tie_fire.update()


        self.player.sprite.lasers.draw(screen)
        self.player.draw(screen)
        
        self.ties.draw(screen)
        self.tie_fire.draw(screen)
        #update all sprite groups
        #draw all sprite groups


if __name__ == '__main__':
    pygame.init()
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    game = Game()
    
    TIELASER = pygame.USEREVENT + 1
    pygame.time.set_timer(TIELASER, 200)
    pygame.time
    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == TIELASER:
                game.tie_shoot()

        screen.fill((30, 30, 30))
        game.run() 
        pygame.display.flip()
        clock.tick(60)
