import time
import secrets

items = []


def story(story_to_print):
    print(story_to_print)
    time.sleep(3)


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response.lower():
            break
        elif option2 == response.lower():
            break
        else:
            story("Sorry, I don't understand.")
    return response


def intro():
    story('You are walking along a path, heading\n '
          'into a large and very old forest.\n')
    story('You have heard that this forest is full of magical\n '
          'creatures both beautiful and dangerous.\n')
    story('Being the experienced sorcerer you are\n '
          'you do not fear the creatures ahead.\n')
    story('After journying deep into the forest\n '
          'you see two paths before you.\n')
    story('The path to the left leads to a bright meadow,\n '
          'and the path to the right is darkened by tightly grown trees.')


def bright_meadow():
    story('You make your way down the path and into the green meadow.\n')
    if "elf" in items:
        story('You take in the beauty of the meadow again and vow\n '
              'to come back someday.\n')
    else:
        story('You admire the sun glistening up from the stream\n'
              ' when you hear a syrinx playing nearby.\n')
        story('An elf is playing a tune that beckons you\n'
              'as though a unique magic lives in the flute.\n')
        story('You learn the elf is named Cara. You invite her to join you\n'
              ' on your travels and she agrees.')
        items.append('elf')
    story('You and Cara head back up the path.')
    path_choice()


def dark_path():
    monsters = ["troll", "giant spider", "warewolf"]
    monsters = monsters[secrets.SystemRandom().randint(0, 2)]
    story('You make your way down the dark path\n '
          'full of tightly grown trees.\n')
    story('As you fight through the entangled branches\n'
          ' a ' + monsters + ' hears you and blocks your path!\n')
    while True:
        while True:
            response = valid_input('Would you prefer to fight or flee?\n',
                                   'fight', 'flee')
            if 'flee' in response:
                story('You turn and run back up the path,\n '
                      'beyond the creatures grasp!\n')
                path_choice()
            elif 'fight' in response:
                if 'elf' in items:
                    story('Cara takes her flute and plays a climactic tune\n'
                          'and the beast turns to stone!\n')
                    story('You thank Cara for saving you both\n'
                          'and vow to be in her debt.\n')
                    story('You and Cara head back up the path.\n')
                else:
                    story('You pull your wand from your cloak\n'
                          'and move to stun the beast!\n')
                    story('The beast is too powerful and you are defeated.\n')
            break
        break


def path_choice():
    response = valid_input('\n\nWhich path would you like to take?\n'
                           'Bright or Dark?\n', 'bright', 'dark')
    if 'bright' in response:
        bright_meadow()
    elif 'dark' in response:
        dark_path()


def play_again():
    response = valid_input('Would you like to play again? Yes or No...\n',
                           'yes', 'no')
    while True:
        if 'yes' in response:
            items.clear()
            return play_game()
        elif 'no' in response:
            print("Thanks for playing!")
        break


def play_game():
    intro()
    path_choice()
    play_again()


play_game()
