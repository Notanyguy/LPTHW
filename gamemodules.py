from random import randint
import time
from sys import exit

def fight(enemy_name, enemy_mindmg, enemy_maxdmg, player_mindmg, player_maxdmg):
    print "You sharpen your swords before the battle."
    print "Are you ready?"
    time.sleep(2)
    enemy_dmg_dealt = randint(enemy_mindmg, enemy_maxdmg)
    player_dmg_dealt = randint(player_mindmg, player_maxdmg)

    print "\nFIGHT !\n"

    time.sleep(2)
    fight_scene_player = [
    "You hack and slash %s. HEYA!!!" %(enemy_name),
    "You jumpkick and hit %s. AGHHH!" %(enemy_name),
    "You punch %s and then stab him in the back." %(enemy_name),
    "You swing your sword over %s, you miss!" %(enemy_name),
    ]

    fight_scene_enemy = [
    "%s throws a knife at you." %(enemy_name),
    "%s punches your groin." %(enemy_name),
    "you recieve a slap from %s" %(enemy_name),
    "%s swings his sword under your legs and misses!" %(enemy_name),
    ]

    print fight_scene_player[randint(0, len(fight_scene_player)-1)]
    time.sleep(2)
    print fight_scene_enemy[randint(0, len(fight_scene_enemy)-1)]
    time.sleep(2)
    print fight_scene_player[randint(0, len(fight_scene_player)-1)]
    time.sleep(2)
    print fight_scene_enemy[randint(0, len(fight_scene_enemy)-1)]
    time.sleep(2)
    if enemy_dmg_dealt > player_dmg_dealt:
        print "%s has defeated you. your body is now food for worms" % (enemy_name)
        return 'death'
    elif enemy_dmg_dealt < player_dmg_dealt:
        print "You have defeated %s, you pray for their soul." % (enemy_name)
        return 'celebration'
    elif enemy_dmg_dealt == player_dmg_dealt:
        print "It's a draw! you have to fight again."
    else:
        print "Does not Compute."
        exit(0)
