import time
from lib.display import Display
from lib.userinput import UserInput
from apps.boo.feed_animation import feed_animation
from apps.boo.stats import feed, load_stats, save_stats
from apps.boo.game import play_higher_lower_game

def menu(display, input):
    """Display the menu and handle user selection."""
    while True:

        display.fill(0)

        display.text("Menu:", x=5, y=10, color=0xFFFF)
        display.text("1. Feed Boo Monster Munch", x=5, y=30, color=0xFFFF)
        display.text("2. Play High/low Number Game", x=5, y=50, color=0xFFFF)
        display.text("3. Return", x=5, y=70, color=0xFFFF)
        display.text("Choose an option:", x=5, y=100, color=0xFFFF)
        display.show()


        while True:
            keys = input.get_new_keys()
            if "1" in keys:

                stats = load_stats()


                feed_animation(display)


                feed(stats)
                save_stats(stats)
                break
            elif "2" in keys:

                play_higher_lower_game(display, input)
                break
            elif "3" in keys:
                return  

        time.sleep(0.1)
