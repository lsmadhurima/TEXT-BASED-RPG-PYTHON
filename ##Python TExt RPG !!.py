##Python TExt RPG !!
# Sai Madhurima LAnka!!
# Endora is the name of the world
import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 200
spaces = ' '


########### Player Setup ##########

class Player:
    def __init__(self):
        self.game = False
        self.name = ''
        self.job = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'Golwildom'


myplayer = Player()


#########  Title Screen ########
def title_screen_selections():
    option = input(" >> ")  # user input
    if option.lower() == "play":
        setup_game()
    elif option.lower() == "help":
        help_menu()
    elif option.lower() == "quit":
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("PLease enter valid command only !! ")
        option = input(" >> ")

        if option.lower() == "play":
            setup_game()
        elif option.lower() == "help":
            help_menu()
        elif option.lower() == "quit":
            sys.exit()


def title_screen():
    os.system('cls')
    print(spaces *5 +'╭── ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅  ─╮')
    print(spaces *5 +'|           ── ⋆⋅☆⋅⋆ ──      \t' + spaces * 2 + '|')
    print(spaces *5 +'|    WELCOME TO TEXT RPG GAME !' + spaces * 6+'|')
    print(spaces *5 +'|           ── ⋆⋅☆⋅⋆ ──      \t' + spaces * 2 + '|')
    print(spaces *5 +'|             - Play -         ' + spaces * 6+ '|')
    print(spaces *5 +'|             - Help -         ' + spaces * 6 + '|')
    print(spaces *5 +'|             - Quit -         ' + spaces * 6 + '|')
    print(spaces *5 +'|            ── ⋆⋅☆⋅⋆ ──    \t  '+ '|')
    print(spaces *5 +'╰── ⋅ ── ✩ ── ⋅⋅ ── ⋅ ⋅ ── ✩ ── ⋅  ──╯')
    title_screen_selections()


def help_menu():
    print(spaces *5 +'╭── ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅  ──╮')
    print(spaces *5 +'|           ── ⋆⋅☆⋅⋆ ──      \t ' + spaces * 5 + '|')
    print(spaces *5 +'|    WELCOME TO TEXT RPG GAME !' + spaces * 7 + '|')
    print(spaces *5 +'|           ── ⋆⋅☆⋅⋆ ──      \t ' + spaces * 5 + '|')
    print(spaces *5 +'|    - This is the help menu!! -  ' + spaces * 4 + '|')
    print(spaces *5 +'|   > Use move to naviagte' + spaces * 12 + '|')
    print(spaces *5 +'|          >>up,down,left,right ' + spaces * 6 + '|')
    print(spaces *5 +'|   > Use examine/look to interact' + spaces * 4 + '|')
    print(spaces *5 +'|             HAVE FUN !! ' + spaces * 12 + '|')
    print(spaces *5 +'|             ── ⋆⋅☆⋅⋆ ──      \t  ' + spaces * 4 + '|')
    print(spaces *5 +'|            ── ⋆⋅☆⋅⋆ ──      \t  ' + spaces * 4 + '|')
    print(spaces *5 +'╰── ⋅ ── ✩ ── ⋅ ⋅ ── ⋅ ⋅ ── ✩ ── ⋅  ──╯')
    title_screen_selections()


def map():
    print(spaces *5 +spaces *5 +"Opening Map....")
    print(spaces *5 +"----------------------------------------------------------------------------------------------------------------------------------------------")
    print(spaces *5 +"| Losfailey, The Spirit Valley | Elvgolsle, Isle ofthe Elves     | Poiwilion, Dominion of the Poison   | Elvgoltry, The Ancient City       |")
    print(spaces *5 +"----------------------------------------------------------------------------------------------------------------------------------------------")
    print(spaces *5 +"| 'Elvossea' , The Etheral Sea   | Golwildom , The Broken Kingdon  | Wartroles , Valees of the warriors    | Losspinds , Lands of the Lost     |")
    print(spaces *5 +"----------------------------------------------------------------------------------------------------------------------------------------------")
    print(spaces *5 +"| Elvwizest , THe magic Forset | Trokinrse , The Magic Universe  | Whions , THe White City ofthe Dragons | Spipoiary , The Ancient Sanctuary | ")
    print(spaces *5 +"----------------------------------------------------------------------------------------------------------------------------------------------")
    print(spaces *5 +"| Wardranet , THe dark PLanet  | Anggiaxus , Nexus of the Angels | Deawilder , Yonder of the DEad        | Devfrolam , Realm ofthe devils    |")
    print(spaces *5 +"----------------------------------------------------------------------------------------------------------------------------------------------")


########## Game functionality #########
def start_game():
    '''
a1  a2    a3   a4 #Player starts at b2
-----------------------
|   |   |   |   |       a4
--------------------
|   |   |   |   |       b4
--------------------
|   |   |   |   |       c4
--------------------
|   |   |   |   |       d4
--------------------'''


ZONENAME = ''
DESCRIPTION = 'description'
EXAMINATION = 'examine'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {'Losfailey': False, 'Elvgolsle': False, 'Poiwilion': False, 'Elvgoltry': False,
                 'Elvossea': False, 'Golwildom': False, 'Wartroles': False, 'Losspinds': False,
                 'Elvwizest': False, 'Trokinrse': False, 'Whions': False, 'Spipoiary': False,
                 'Wardranet': False, 'Anggiaxus': False, 'Deawilder': False, 'Devfrolam': False
                 }
zonemap = {'Losfailey': {ZONENAME: 'Losfailey',
                  DESCRIPTION: 'This is where the lost spirits lie...',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: '',
                  DOWN: 'Elvossea',
                  LEFT: '',
                  RIGHT: 'Elvgolsle',
                  },
           'Elvgolsle': {ZONENAME: 'Elvgolsle',
                  DESCRIPTION: 'It is rumored that there are pots of gold burries here...',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: '',
                  DOWN: 'Golwildom',
                  LEFT: 'Losfailey',
                  RIGHT: 'Poiwilion',
                  },
           'Poiwilion': {ZONENAME: 'Poiwilon',
                  DESCRIPTION: 'The deadliest poisons are found here... ',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: '',
                  DOWN: 'Wartroles',
                  LEFT: 'Elvgolsle',
                  RIGHT: 'Elvgoltry',
                  },
           'Elvgoltry': {ZONENAME: 'Elvgoltry',
                  DESCRIPTION:'The oldest city in the Endora to be known ',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: '',
                  DOWN: 'Elvossea',
                  LEFT: 'Poiwilion',
                  RIGHT: '',
                  },
           'Elvossea': {ZONENAME: 'Elvossea',
                  DESCRIPTION: 'The largest sea which sparkles all the time...',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Losfailey',
                  DOWN: 'Elvwizest',
                  LEFT: '',
                  RIGHT: 'Golwildom'
                  },
           'Golwildom': {ZONENAME: 'Golwildom',
                  DESCRIPTION: 'Everything just turned into dust... ',
                  EXAMINATION: 'You should head to other Zones',
                  SOLVED: False,
                  UP: 'Elvgolsle',
                  DOWN: 'Trokinrse',
                  LEFT: 'Elvossea',
                  RIGHT: 'Wartroles',
                  },
           'Wartroles': {ZONENAME: 'Wartroles',
                  DESCRIPTION: 'The greatest Warriors lived here.. but they are not the most friendly..',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Poiwilion',
                  DOWN: 'Whions',
                  LEFT: 'Golwildom',
                  RIGHT: 'Losspinds',
                  },
           'Losspinds': {ZONENAME: 'Losspinds',
                  DESCRIPTION: "No one has ever escaped this region... it's myterious ? oh and deadly..",
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Elvgoltry',
                  DOWN: 'Spipoiary',
                  LEFT: 'Wartroles',
                  RIGHT: '',
                  },
           'Elvwizest': {ZONENAME: 'Elvwizest',
                  DESCRIPTION: 'This is a forest.. ✨the magical one ✨',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Elvossea',
                  DOWN: 'Wardranet',
                  LEFT: '',
                  RIGHT: 'Trokinrse',
                  },
           'Trokinrse': {ZONENAME: 'Trokinrse',
                  DESCRIPTION: 'Here lies the secrets of the Endora',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Golwildom',
                  DOWN: 'Anggiaxus',
                  LEFT: 'Elvwizest',
                  RIGHT: 'Whions',
                  },
           'Whions': {ZONENAME: 'Whions',
                  DESCRIPTION: "The whole city is sparkling white... how do they do it it's still a mystery",
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Wartroles',
                  DOWN: 'Deawilder',
                  LEFT: 'Trokinrse',
                  RIGHT: 'Spipoiary',
                  },
           'Spipoiary': {ZONENAME: 'Spipoiary',
                  DESCRIPTION: 'You are ready to explore the town!!',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Losspinds',
                  DOWN: 'Devfrolam',
                  LEFT: 'Whions',
                  RIGHT: '',
                  },
           'Wardranet': {ZONENAME: 'Wardranet',
                  DESCRIPTION: 'You are ready to explore the town!!',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Elvwizest',
                  DOWN: '',
                  LEFT: '',
                  RIGHT: 'Anggiaxus',
                  },
           'Anggiaxus': {ZONENAME: 'Anggiaxus',
                  DESCRIPTION: 'You are ready to explore the town!!',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Trokinrse',
                  DOWN: '',
                  LEFT: 'Wardranet',
                  RIGHT: 'Deawilder',
                  },
           'Deawilder': {ZONENAME: 'Deawilder',
                  DESCRIPTION: 'You are ready to explore the town!!',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Whions',
                  DOWN: '',
                  LEFT: 'Anggiaxus',
                  RIGHT: 'Devfrolam',
                  },
           'Devfrolam': {ZONENAME: 'Devfrolam',
                  DESCRIPTION: 'You are ready to explore the town!!',
                  EXAMINATION: 'examine',
                  SOLVED: False,
                  UP: 'Spipoiary',
                  DOWN: '',
                  LEFT: 'Deawilder',
                  RIGHT: '',
                  },
           
           }


######### GAME INTERACTIVITY ###########
def print_location():
    print('\n' + ("#" * (4 + len(myplayer.location))))
    print('# ' + myplayer.location.upper() + ' #')
    print('# ' + zonemap[myplayer.location][DESCRIPTION] + ' # ')
    print('\n' + ("#" * (4 + len(myplayer.location))))


def prompt():
    print("\n " + '=====================================')
    print("What you would like to do ??")
    print("Avaliable Commands : \n \t move, go, travel, walk, quit, examine, inspect, interact, look, exit, map ")
    action = input("> ")
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look','map']
    while action.lower() not in acceptable_actions:
        print("Unknown action , try again later. \n")
        action = input("> ")
    if action.lower() == 'quit':
        print('\nExiting the game ........')
        sys.exit()
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move()
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine()
    elif action.lower() in ['map']:
        map()


def player_move():
    ask = 'Where do you wanna go ?? \n'
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myplayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myplayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myplayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myplayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + '.')
    myplayer.location = destination
    print_location()


def player_examine():
    if zonemap[myplayer.location][SOLVED]:
        print("Zone is Exhausted !!")
    else:
        print("You can trigger a puzzle here !! ")
        puzzles ()
        prompt()
    # GAME FUNCTIONALITY ########
def puzzles ():
    if zone[my.player.loaction] == 'Losfailey' :
        losfaily_gameplay ()
    elif zone[my.player.loaction] == 'Elvgolsle' :
        elvgolsle_gameplay ()
    elif zone[my.player.loaction] == 'Poiwilion' :
        poiwilion_gameplay ()
    elif zone[my.player.loaction] == 'Elvgoltry' :
        elvgoltry_gameplay ()
    elif zone[my.player.loaction] == 'Elvlossea' :
        elvlossea_gameplay ()
    elif zone[my.player.loaction] == 'Golwildom' :
        golwildom_gameplay ()
    elif zone[my.player.loaction] == 'Wartroles' :
        wartroles_gameplay ()
    elif zone[my.player.loaction] == 'Losspinds' :
        losspinds_gameplay ()
    elif zone[my.player.loaction] == 'Elvwizest' :
        elvwizest_gameplay ()
    elif zone[my.player.loaction] == 'Trokinrse' :
        elvgolsle_gameplay ()
    elif zone[my.player.loaction] == 'Whions' :
        whions_gameplay ()
    elif zone[my.player.loaction] == 'Spipoiary' :
        spipoiary_gameplay ()
    elif zone[my.player.loaction] == 'Wardranet' :
        wardranet_gameplay ()
    elif zone[my.player.loaction] == 'Anggiaxus' :
        anggiaxus_gameplay ()
    elif zone[my.player.loaction] == 'Trokinrse' :
        trokinrse_gameplay ()
    elif zone[my.player.loaction] == 'Deawilder' :
        deawilder_gameplay ()
    elif zone[my.player.loaction] == 'Devfrolam' :
        devfrolam_gameplay ()
def losfailty_gameplay ():
    
def start_game():
    return setup_game()


def main_game_loop():
    while myplayer.game is False:
        print("Here")
        prompt()
    # here handle if puzzles have been solved ,explored , boss defeated  etc

def setup_game():
    os.system('cls')
    question1 = "Hello, What's Your Name ? \n "
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    myplayer.name = player_name
    # JOB SETUP #######
    question2 = "Hello, What role u wanna play ? \n "
    question2added = "You can play as a warrior, ghost or a mage !! \n"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    for character in question2added:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.01)
    player_job = input("> ")
    valid_jobs = ['warrior', 'mage', 'ghost']
    if player_job.lower() in valid_jobs:
        myplayer.job = player_job
        print("You are now a " + player_job + ": \n")
    else:
        while player_job.lower() not in valid_jobs:
            player_job = input(" > ")
            if player_job.lower() in valid_jobs:
                myplayer.job = player_job
                print("You are now a " + player_job + " !! \n")
        # Player Status #########
        if myplayer.job == 'warrior':
            myplayer.hp = 120
            myplayer.mp = 20
        elif myplayer.job == 'mage':
            myplayer.hp = 40
            myplayer.mp = 120
        elif myplayer.job == 'ghost':
            myplayer.hp = 60
            myplayer.mp = 60

    # INTRODUCTION
    question3 = "\nWelcome !! " + player_name + " you are the " + player_job + ".\n "
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    myplayer.name = player_name

    speech1 = "Welcome to this fantasy world !!\n "
    speech2 = "I hope it treats you well ...\n "
    speech3 = "Just make sure you don't get lost ?!?!\n"
    speech4 = "Hehehehehe....\n"

    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)
    os.system('cls')
    print("###############################")
    print("#-Let's get started Shall We -#")
    print("###############################")
    main_game_loop()


title_screen()
