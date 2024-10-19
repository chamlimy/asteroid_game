from circleshape import CircleShape
import pygame
from constants import SHOT_RADIUS, PLAYER_TURN_SPEED

class Shot(CircleShape):
    """bullet shot class

    """
    
    def __init__(self,x,y):
        super().__init__(x,y,SHOT_RADIUS)
        self.rotation  = 0
    
    def draw(self,screen):
        pygame.draw.circle(screen,color="white",center=self.position,radius=self.radius,width=2)
    
    def update(self,dt):
        self.position += self.velocity*dt
    
    
    