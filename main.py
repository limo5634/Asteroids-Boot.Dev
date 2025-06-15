# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import  *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0

    # Groups erstellen
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Container für die Klassen setzen
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    # Objekte erstellen
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()


    while True:
        # Event-Handling für das Schließen des Fensters
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Bildschirm schwarz füllen
        screen.fill("black")
        
        # Alle updatable Objekte aktualisieren
        updatable.update(dt)


        # Kollisionserkennung: Spieler vs Asteroiden
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                print("Game over!")
                sys.exit()
        
        # Kollisionserkennung: Schüsse vs Asteroiden
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    asteroid.split()  # Asteroid aufteilen statt nur entfernen
                    shot.kill()      # Schuss entfernen
        
        # Alle drawable Objekte zeichnen
        for obj in drawable:
            obj.draw(screen)
        
        # Bildschirm aktualisieren
        pygame.display.flip()
        
        # Delta time berechnen
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()