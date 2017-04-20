import random
from sys import exit
import time
from gamemodules import fight
print '*' * 79
print '\n'
print '\t\tHello and welcome to'
print '\t\t" Musashi: Ronin Legend."'
print '\t\tProgrammed poorly by Guy Bahat'
print '\n'
print '*' * 79

print "What is your name? please type it."
global player_name
player_name = raw_input("\n> ")
print "Good Choice."

class items(object):
    pass

class weapons(items):
    pass

class armor(items):
    pass

class Scene(object):

    def enter(self):
        print "This function is not defined."
        exit(0)


class Map(object):
        scenes = {'death' : Death(),
        'celebration' : Celebration(),
        'ending' : Ending(),
        'miyamoto' : Miyamoto(),
        'armory' : Armory(),
        'meadows' : Meadows(),
        'castle' : Castle()
        }
        def __init__(self, start_scene):
            self.start_scene = start_scene

        def play(self, scene_name):
            scene_name.enter()


a_map = Map('miyamoto')
a_map.play(Miyamoto)
