import random
import time
from lib.display import Display
from lib.userinput import UserInput
from apps.boo.stats import load_stats, save_stats, play_game

def show_message(display, message_lines):
    """Display a series of messages on the screen."""
    display.fill(0)
    y = 10
    for line in message_lines:
        display.text(text=line, x=5, y=y, color=0xFFFF)
        y += 20
    display.show()

def play_higher_lower_game(display, input):
    """Play the Higher or Lower game."""
    stats = load_stats()
    play_game(stats)  

    while True:

        current_number = random.randint(1, 9)
        next_number = random.randint(1, 9)


        show_message(display, [
            f"Current number: {current_number}",
            "What will the next number be?",
            "1. Higher",
            "2. Lower"
        ])

        while True:
            keys = input.get_new_keys()
            if "1" in keys or "2" in keys:
                break
            time.sleep(0.1)

        if (next_number > current_number and "1" in keys) or (next_number < current_number and "2" in keys):

            show_message(display, [
                f"Correct! The number was {next_number}.",
                "1. Play again?",
                "2. Return"
            ])
        else:

            show_message(display, [
                f"Incorrect. The number was {next_number}.",
                "1. Play again?",
                "2. Return"
            ])

        while True:
            keys = input.get_new_keys()
            if "1" in keys:
                break
            elif "2" in keys:
                return  
            time.sleep(0.1)

        time.sleep(0.1)  

