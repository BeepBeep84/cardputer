# Note Taking App (Cardputer)

This is a simple note-taking application built for the **M5Stack Cardputer** using the **MicroHydra** framework. It lets you type short notes, save them to an SD card, and scroll through them later using the Cardputer keyboard.

**[Read the blog post](https://randomboo.com/project/m5-stack_cardputer/)**

---

## Features

- **Write Notes** – Type and save quick notes to `notes.txt` on an SD card.
- **Read Notes** – View saved notes with scrolling.
- **Persistent Storage** – Notes are saved to `/sd/notes.txt`.
- **Custom Font** – Uses a VGA-style font for readability.

---

## Controls

- `1` – Write a new note  
- `2` – Read saved notes  
- `UP` / `DOWN` – Scroll through notes  
- `ESC` – Exit reading mode  
- `ENT` – Save the current note  
- `BSPC` – Delete last character  
- `SPC` – Add space  
- Letter keys – Input text

---

## Installation

1. Install **MicroHydra** on your Cardputer.
2. Insert an SD card and ensure it’s mounted to `/sd/`.
3. Upload the app files, including:
   - `__init__.py`
   - `font.py` (with `vga1_8x16` font)
   - Dependencies from `lib`: `display`, `userinput`, `sdcard`
4. Run the app.

---

## File Overview

- `__init__.py` – Main app logic
- `notes.txt` – Automatically created and used for storing notes
- `font.py` – Custom font module

---

## License

MIT License — take notes, not excuses.
