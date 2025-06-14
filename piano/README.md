# Piano Simulator (Cardputer)

This is a simple piano simulator for the **M5Stack Cardputer**, created using the **MicroHydra** framework. It maps keyboard keys to musical notes and plays them using I2S audio output. The screen displays a layout of white and black keys for intuitive playing.

**[Read the blog post](https://randomboo.com/project/piano_simulator/)**

---

## Features

- **Plays notes from C4 to E5**
- **I2S Audio Output** for clean sine wave tones
- **QWERTY and number key mapping**
- **Graphical layout** of piano keys displayed on-screen
- Minimal dependencies: `userinput`, `display`, `I2S`

---

## Controls

- **White Keys**: `Q W E R T Y U I O P` → C4 to E5  
- **Black Keys (Sharps)**: `1 2 4 5 6 7 8 0` → C♯ to A♯  
- Plays sound when a mapped key is pressed

---

## Installation

1. Install **MicroHydra** on your Cardputer.
2. Upload files:
   - `__init__.py`
   - Required modules: `display`, `userinput`
3. Ensure your Cardputer supports I2S audio output (check wiring for `SCK`, `WS`, `SD`)
4. Run the program to start jamming!

---

## File Overview

- `__init__.py` – Handles I2S audio setup, note mapping, sine wave generation, and display layout
- Uses internal tone dictionary for note frequencies (C4 to AS5)

---

## Notes

- Notes are generated using sine waves for smooth sound.
- The app deinitializes I2S on exit.
- Good for demos or experimenting with embedded audio!

---

## License

MIT License — jam responsibly.
