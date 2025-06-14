import utime
from lib.display import Display
from lib.userinput import UserInput


DEFAULT_HAPPINESS = 100
DEFAULT_HUNGER = 100
HAPPINESS_DECREASE_PER_DAY = 50
HUNGER_DECREASE_PER_DAY = 50


def load_stats():
    """Load stats from the file."""
    try:
        with open('/apps/boo/data.txt', 'r') as f:
            lines = f.readlines()
            stats = {}
            if len(lines) >= 5:
                try:
                    stats['age_start_timestamp'] = int(lines[0].strip())
                    stats['last_game_timestamp'] = int(lines[1].strip())
                    stats['last_feed_timestamp'] = int(lines[2].strip())
                    stats['happiness'] = int(lines[3].strip())
                    stats['hunger'] = int(lines[4].strip())
                except ValueError as e:
                    print("Error converting file content to integer:", e)
                    print("File content:", lines)
                    stats = get_default_stats()
            else:
                stats = get_default_stats()
    except OSError as e:
        print("Error reading file:", e)
        stats = get_default_stats()
    except Exception as e:
        print("Unexpected error:", e)
        stats = get_default_stats()
    return stats

def save_stats(stats):
    """Save stats to the file."""
    try:
        with open('/apps/Boo/data.txt', 'w') as f:
            f.write(f"{stats['age_start_timestamp']}\n")
            f.write(f"{stats['last_game_timestamp']}\n")
            f.write(f"{stats['last_feed_timestamp']}\n")
            f.write(f"{stats['happiness']}\n")
            f.write(f"{stats['hunger']}\n")
    except Exception as e:
        print("Error saving stats:", e)

def get_default_stats():
    """Return default stats."""
    now = utime.time()
    return {
        'age_start_timestamp': now,
        'last_game_timestamp': now,
        'last_feed_timestamp': now,
        'happiness': DEFAULT_HAPPINESS,
        'hunger': DEFAULT_HUNGER
    }

def calculate_age(stats):
    """Calculate age in days with validation."""
    now = utime.time()
    seconds_per_day = 86400


    if stats['age_start_timestamp'] > now:

        stats['age_start_timestamp'] = now
    
    return (now - stats['age_start_timestamp']) // seconds_per_day


def update_stats(stats):
    """Update happiness and hunger based on elapsed time."""
    now = utime.time()
    seconds_per_day = 86400
    days_since_last_game = (now - stats['last_game_timestamp']) // seconds_per_day
    days_since_last_feed = (now - stats['last_feed_timestamp']) // seconds_per_day


    stats['happiness'] = max(0, stats['happiness'] - days_since_last_game * HAPPINESS_DECREASE_PER_DAY)
    stats['hunger'] = max(0, stats['hunger'] - days_since_last_feed * HUNGER_DECREASE_PER_DAY)

def stats(display, input):
    """Display the stats on the screen."""
    stats = load_stats()
    update_stats(stats)


    display.fill(0)


    age_days = calculate_age(stats)
    display.text(text="Boo Stats:", x=5, y=10, color=0xFFFF)
    display.text(text=f"Age: {age_days} days", x=5, y=30, color=0xFFFF)
    display.text(text=f"Happiness: {stats['happiness']}", x=5, y=50, color=0xFFFF)
    display.text(text=f"Hunger: {stats['hunger']}", x=5, y=70, color=0xFFFF)
    display.text(text="Press 1 to return", x=5, y=100, color=0xFFFF)
    display.show()


    while True:
        keys = input.get_new_keys()
        if "1" in keys:
            break


    display.fill(0)
    display.show()


def feed(stats):
    """Handle feeding the Tamagotchi."""
    stats['hunger'] = DEFAULT_HUNGER
    stats['last_feed_timestamp'] = utime.time()
    save_stats(stats)

def play_game(stats):
    """Handle playing a game with the Tamagotchi."""

    stats['happiness'] = min(DEFAULT_HAPPINESS, stats['happiness'] + 10) 
    stats['last_game_timestamp'] = utime.time()
    save_stats(stats)
