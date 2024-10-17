import pygame as pg
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    pg.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pg.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
    while 1:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill(color="black")
        pg.display.flip()
if __name__=="__main__":
    main()