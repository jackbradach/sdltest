import pygame
from pygame.locals import *

from .sprites import Assassin, Barbarian, Centaur, Necromancer, Sorceress, Warrior

def main():
    pygame.init()
    screen = pygame.display.set_mode((1024, 768))
    pygame.display.set_caption('SDL Test (Python)')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()

    characters = [
        Assassin(),
        Barbarian(),
        Centaur(),
        Necromancer(),
        Sorceress(),
        Warrior()
    ]
    character_idx = 0
    c = characters[character_idx]
    
    actions = list(c.action_images.action_images.keys())
    action_idx = 0
   

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == K_SPACE:
                    c.action_images.action = actions[action_idx]
                    action_idx = (action_idx + 1) % len(actions)
                if event.key == K_n:
                    character_idx = (character_idx + 1) % len(characters)
                    c = characters[character_idx]
                    actions = list(c.action_images.action_images.keys())
                    action_idx = 0
                    print(f"New character = {c.spritepath}!")

        # img = s.get_image_at((320 * i, 0, 320, 320))
        background.fill((100, 100, 100))
        background.blit(c.get_image(), (0,0))
        screen.blit(background, (0, 0))
        pygame.display.flip()
        pygame.time.wait(100)