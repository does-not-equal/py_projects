import sys

# variables created for the text files
char_races = "charFiles\Races.txt"
charClasses = "charFiles\Classes.txt"
charFeats = "charFiles\Feats.txt"
charStats = "charFiles\Stats.txt"


def race_subtext():
    print('Press (y)es to confirm or (n)o to choose another race')
    
def class_subtext():
    print('Press (y)es to confirm or (n)o to choose another class')
    
def feats_subtext():
    print('These are your feats')
    
def stats_subtext():
    print('These are your stats')
    
def char_races():
    with open(char_races) as char_races_f:
        char_races_f = char_races_f.read()
        print(char_races)
        
def char_classes():
    char_classes_file = open(charClasses)
    contents = char_classes_file.read()
    print(contents)
    char_classes_file.close()

def char_feats():
    char_feats_file = open(charFeats)
    contents = char_feats_file.read()
    print (contents)
    char_feats_file.close()

def char_stats():
    char_stats_file = open(charStats)
    contents = char_stats_file.read()
    print (contents)
    char_stats_file.close()

def player_race_loop():
    while True:
        print('Please choose a class or type (q) to exit:', c_races())
        player_input = input()
        if player_input == 'q':
            sys.exit()
        if player_input == 'h':
            print('You chose human and receive a +1 to all stats.')
            race_subtext()
            player_input = input()
            if player_input == 'y':
                player_class_loop()
            elif player_input == 'n':
                player_race_loop()
            elif player_input != 'y' or 'n':
                sys.exit()
        elif player_input == 'he':
            print('You chose half elf and receive a +1 perception and +1 agility.')
            race_subtext()
            player_input = input()
            if player_input == 'y':
                player_class_loop()
            elif player_input == 'n':
                player_race_loop()
            elif player_input != 'y' or 'n':
                sys.exit()
        elif player_input == 'o':
            print('You chose orc and receive a +1 endurance, +1 strength, and -1 charisma.')
            race_subtext()
            player_input = input()
            if player_input == 'y':
                player_class_loop()
            elif player_input == 'n':
                player_race_loop()
            elif player_input != 'y' or 'n':
                sys.exit()
        elif player_input == 'g':
            print('You chose gnome and receive a -1 strength, +1 perception, and +1 intelligence.')
            race_subtext()
            player_input = input()
            if player_input == 'y':
                player_class_loop()
            elif player_input == 'n':
                player_race_loop()
            elif player_input != 'y' or 'n':
                sys.exit()
        elif player_input == 'ho':
            print('You chose hobgoblin and receive a +1 endurance, +2 strength, -2 charisma, and -1 intelligence.')
            race_subtext()
            player_input = input()
            if player_input == 'y':
                player_class_loop()
            elif player_input == 'n':
                player_race_loop()
            elif player_input != 'y' or 'n':
                sys.exit()
        elif player_input == 'f':
            print('You chose fae and receive a -2 strength, -1 endurance, +2 all other stats.')
            race_subtext()
            player_input = input()
            if player_input == 'y':
                player_class_loop()
            elif player_input == 'n':
                player_race_loop()
            elif player_input != 'y' or 'n':
                sys.exit()
            
player_race_loop()