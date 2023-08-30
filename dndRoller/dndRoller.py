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

def char_read():
    player_input = input()
    if player_input == 'h':
        with open(char_races) as char_races_h:
            char_races_h = char_races_h.read()
            print(char_races)
    elif player_input == 'he':
        with open(char_races) as char_races_he:
            char_races_he = char_races_he.read()
            print(char_races)
    elif player_input == 'o':
        with open(char_races) as char_races_o:
            char_races_o = char_races_o.read()
            print(char_races)
    elif player_input == 'g':
        with open(char_races) as char_races_g:
            char_races_g = char_races_g.read()
            print(char_races)
    elif player_input == 'ho':
        with open(char_races) as char_races_ho:
            char_races_ho = char_races_ho.read()
            print(char_races)
    elif player_input == 'f':
        with open(char_races) as char_races_f:
            char_races_f = char_races_f.read()
            print(char_races)


def player_race_loop():
    while True:
        print('Please choose a class or type (q) to exit:')
        player_input = input()
        if player_input == 'q':
            sys.exit()
        elif player_input == 'h' or 'he' or 'o' or 'g' or 'ho' or 'f':
            char_read()
            
player_race_loop()