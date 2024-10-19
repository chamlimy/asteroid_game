import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    pg.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pg.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    clock = pg.time.Clock()
    dt = 0
    updatable = pg.sprite.Group()
    drawable = pg.sprite.Group()
    Player.containers = (updatable,drawable)
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    updatable.add(player)
    drawable.add(player)
    asteroids = pg.sprite.Group()
    Asteroid.containers = (asteroids,updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField()
    shots = pg.sprite.Group()
    Shot.containers = (shots,updatable,drawable)
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill(color="black")
        dt = clock.tick()/1000
        for pl in updatable:
            pl.update(dt)
        for asteroid in asteroids:
            if asteroid.is_collision(player):
                print('Game Over!')
                sys.exit(0)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.is_collision(shot):
                    shot.kill()
                    asteroid.split()
        for pl in drawable:
            pl.draw(screen)
        pg.display.flip()
if __name__=="__main__":
    main()