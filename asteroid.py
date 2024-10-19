from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS
import random as rd

class Asteroid(CircleShape):
    """Asteroid Class 

    """
    
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        
    
    def draw(self,screen):
        pygame.draw.circle(screen,color="white",center=self.position,radius=self.radius,width=2)
    
    def update(self,dt):
        self.position += self.velocity*dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        # spawning 2 new asteroids
        angle = rd.uniform(20,50)
        vel_ast1 = self.velocity.rotate(angle)
        vel_ast2 = self.velocity.rotate(-angle)
        
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        ast1 = Asteroid(self.position[0],self.position[1],new_radius)
        ast1.velocity = vel_ast1*1.2
        ast2 = Asteroid(self.position[0],self.position[1],new_radius)
        ast2.velocity = vel_ast2*1.2
        
    
    