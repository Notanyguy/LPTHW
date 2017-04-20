
class Miyamoto(Scene):
    def enter(self):
        print "\nFeudal Japan, 1584. "
        print "You were born in the small village  village, in the Yoshino district."
        print "From a young age you have been taught to live by two things:"
        time.sleep(1)
        print "Buddah and the Sword.\n"
        time.sleep(1)
        print "%s, Time is not on your side. " % player_name
        print "Bandits are attacking Yoji, at the Armory!"
        print "Will you help save him?"
        choice = raw_input("yes/no ?\n> ")

        if choice == "yes" or choice == "Yes":
            print "You run towards the Armory."
            return 'armory'
        if choice == "no" or choice == "No":
            print "You cowrdly hide under your bed."
            print "GAME OVER"
            exit(1)

class Armory(Scene):

    def enter(self):
        pass

class Meadows(Scene):
    def enter(self):
        fight("Osamu Kitajima",1 ,10 , 1, 10)

class Castle(Scene):

    def enter(self):
        pass

class Death(Scene):
    death_print = [
    "Sayonara.",
    "You died an honourable death.",
    "GAME OVER.",
    ]
    def enter(self):
        print death_print[randint(0, len(death_print)-1)]
        exit(2)

class Celebration(Scene):
    celeb_print = [
    "%s: Sayonara, Kisama." % player_name,
    "Yay! I win !",
    "GAME OVER.",
    ]
    def enter(self):
        print celeb_print[randint(0, len(celeb_print)-1)]
        exit(1)
class Ending(Scene):
    def enter(self):
        print "It is time %s." % player_name
        print "After living as a Ronin for so long, you have no place in this world any longer."
        print "Harakiri is the only honourable death for you."
        time.sleep(2)
        print "You take your sword \"%s\" and put it on your stomach." % sword_name
        time.sleep(1)
        print "Any last words?"
        last_words = raw_input("\n> ")
        print "The blade cuts through your intestines, and you finally find peace."
        return 'death'
