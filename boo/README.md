# Boogotchi (Virtual Pet Ghost)

Boogotchi is a Tamagotchi-style virtual pet game designed for the **M5Stack Cardputer**, featuring a ghostly companion named **Boo**. Unlike traditional pets, Boo is already dead—so don’t worry about keeping him alive—but he does crave your attention through food and games.

 **[Watch a video demo on my blog](https://randomboo.com/blog/31-august-2024/)**

Original blog post - [Boogotchi](https://randomboo.com/project/boogotchi/)
---

## Features

- **Animated Ghost** – Boo blinks and bounces across the screen using frame buffers.
- **Feeding** – Feed Boo "Monster Munch" and watch a quirky animation.
- **Mini Game** – Play a "Higher or Lower" number game to boost Boo's happiness.
- **Stats Screen** – View Boo's age, hunger, and happiness stats.
- **Persistent Data** – Stats are saved and loaded from a file (`data.txt`).
- **Real-Time Aging** – Boo's stats degrade over real-world time.

---

## Controls

- `1` – Open Menu (Feed or Play)
- `2` – View Stats
- `ESC` – Exit menus

---

## Installation

1. Install the **MicroHydra** framework on your Cardputer.
2. Copy the `apps/boo` folder and required image assets (`ghost.raw`, `ghost_blink.raw`, etc.) to your device.
3. Run the `__init__.py` to start the app.

---

## File Overview

- `__init__.py` – Main app loop with Boo's animation.
- `stats.py` – Handles loading/saving stats and age calculation.
- `menu.py` – Displays feed/game menu.
- `feed_animation.py` – Plays animated "OM NOM NOM" sequence.
- `game.py` – Implements the Higher/Lower number guessing game.

---

## Notes

- Boo’s happiness and hunger decrease daily unless you interact.
- Boo cannot die, but he may become *very* grumpy.
- The app attempts to sync time using NTP if Wi-Fi is available.

---

## License

MIT License – do whatever you want, just don’t blame Boo.
