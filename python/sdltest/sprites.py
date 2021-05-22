from abc import ABC
import pkg_resources
from pathlib import Path, PurePath
import importlib.resources
import pygame

# import pygame.sprite

class ActionImages():
    def __init__(self):
        self._action = 'idle'
        self._index = 0
        self.action_images = {}

    def add(self, action: str, image):
        """Adds a new image to an action (creating the action if need be)"""
        surface = pygame.Surface
        if action not in self.action_images.keys():
            self.action_images[action] = [image]
        self.action_images[action].append(image)

    def next(self):
        """Return the next frame in the action."""
        image = self.action_images[self._action][self._index]
        self._index = (self._index + 1) % len(self.action_images[self._action])
        # if self._index == 0:
        #     self._action = 'idle'
        return image

    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, new_action: str):
        # TODO - add check for bad action
        self._action = new_action
        self._index = 0
        print(f'Playing new action: {self._action}')

    def load_from_path(self, spritepath):
        respath = importlib.resources.files(__package__) / "assests" / spritepath
        actions = {}
        for res in respath.glob('*.png'):
            image = pygame.image.load(res)
            action = res.name[:-6]
            self.add(action, image)

class Sprite(pygame.sprite.Sprite):

    def __init__(self):
        self.action_images = ActionImages()
        self.action_images.load_from_path(self.spritepath)

    def get_image(self):
        return self.action_images.next()

    def load_from_sheet(self):
        try:
            source = pkg_resources.resource_filename('sdltest', f'assests/{self.spritesheet}')
            self.sheet = pygame.image.load(source).convert()
        except FileNotFoundError as e:
            print(f"Unable to load spritesheet image: {self.spritesheet}")
            raise SystemExit(e)
    
    def get_image_at(self, rectangle, colorkey = None):
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None: 
            if colorkey == -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image

    

class Assassin(Sprite):
    spritepath = PurePath('assassin')

class Barbarian(Sprite):
    spritepath = PurePath('barbarian')

class Centaur(Sprite):
    spritepath = PurePath('centaur')

class Necromancer(Sprite):
    spritepath = PurePath('necromancer')

class Sorceress(Sprite):
    spritepath = PurePath('sorceress')

class Warrior(Sprite):
    spritepath = PurePath('warrior')



class Bottle(Sprite):
    def __init__(self):
        pass
